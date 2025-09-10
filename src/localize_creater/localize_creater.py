import orjson
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom


class LocalizeCreater:
    def __init__(self):
        self.target_language_code_list = []
        self.base_language_code = None
        self.sdk = None

    # def create_flutter(self):
    #     print(f"Target language code list: {self.target_language_code_list}")
    #     print(f"Base language code: {self.base_language_code}.json")
    #     print(f"SDK: {self.sdk}")
    #     with open(f"./sample_data/sample_{self.base_language_code}.json", "r") as f:
    #         data_base = orjson.loads(f.read())
    #         new_data = {}
    #         new_data["@@locale"] = self.base_language_code
    #         new_data = { **new_data, **data_base }
    #         with open(f"./sample_output/dart/sample_{self.base_language_code}.arb", "w") as g:
    #             g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))


    #     # Output dart code
    #     with open(f"./sample_data/sample_{self.base_language_code}.json", "r") as f:
    #         data_base = orjson.loads(f.read())
    #         new_data = {}
    #         new_data["@@locale"] = self.base_language_code
    #         new_data = { **new_data, **data_base }
    #         with open(f"./sample_output/dart/app_{self.base_language_code}.arb", "w") as g:
    #             g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))
    #     for target_language_code in self.target_language_code_list:
    #         with open(f"./sample_data/sample_{target_language_code}.json", "r") as f:
    #             data_base = orjson.loads(f.read())
    #             new_data = {}
    #             new_data["@@locale"] = target_language_code
    #             new_data = { **new_data, **data_base }
    #             with open(f"./sample_output/dart/app_{target_language_code}.arb", "w") as g:
    #                 g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))

    def create_flutter(self):
        """
        Create Flutter ARB files with proper parameter handling
        
        Args:
            use_param_files (bool): If True, use the _with_params.json files
        """
        print(f"Target language code list: {self.target_language_code_list}")
        print(f"Base language code: {self.base_language_code}.json")
        print(f"SDK: {self.sdk}")
        with open(f"./sample_data/sample_{self.base_language_code}.json", "r") as f:
            data_base = orjson.loads(f.read())
            new_data = {}
            new_data["@@locale"] = self.base_language_code
            new_data = { **new_data, **data_base }
            
            # Add parameter placeholders for Flutter ARB format
            new_data = self._add_flutter_parameter_placeholders(new_data)
            
            with open(f"./sample_output/dart/app_{self.base_language_code}.arb", "w") as g:
                g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))

        # Process target languages
        for target_language_code in self.target_language_code_list:
            with open(f"./sample_data/sample_{target_language_code}.json", "r") as f:
                data_base = orjson.loads(f.read())
                new_data = {}
                new_data["@@locale"] = target_language_code
                new_data = { **new_data, **data_base }
                
                # Add parameter placeholders for Flutter ARB format
                new_data = self._add_flutter_parameter_placeholders(new_data)
                
                with open(f"./sample_output/dart/app_{target_language_code}.arb", "w") as g:
                    g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))
        
        print("Flutter ARB files with parameters generated successfully!")
        print("Files created in: ./sample_output/dart/")
        print("- app_en.arb (base language)")
        for lang in self.target_language_code_list:
            print(f"- app_{lang}.arb")

    def _add_flutter_parameter_placeholders(self, data):
        """
        Add Flutter ARB parameter placeholders for strings with parameters
        
        Args:
            data (dict): Dictionary containing localization data
            
        Returns:
            dict: Updated dictionary with parameter placeholders
        """
        import re
        
        # Create a copy of items to avoid changing dict during iteration
        items_to_process = list(data.items())
        
        for key, value in items_to_process:
            if key == "@@locale":
                continue
                
            # Find all {parameter} patterns in the string
            param_pattern = r'\{(\w+)\}'
            params = re.findall(param_pattern, str(value))
            
            if params:
                # Create parameter placeholders for Flutter ARB format
                param_placeholders = {}
                for param in params:
                    param_placeholders[f"{param}"] = f"String{param.capitalize()}"
                
                # Add the parameter placeholders to the data
                data[f"{key}@parameter"] = param_placeholders
        
        return data

    def create_android_xml(self, data, language_code):
        """
        Create Android XML string resources from JSON data
        
        Args:
            data (dict): Dictionary containing key-value pairs for localization
            language_code (str): Language code for the localization
        
        Returns:
            str: Formatted XML string for Android string resources
        """
        root = ET.Element("resources")
        for key, value in data.items():
            string_elem = ET.SubElement(root, "string")
            string_elem.set("name", key)
            string_elem.text = value
        rough_string = ET.tostring(root, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="    ")

    def create_android(self):
        """
        Create Android XML string resources files
        
        Args:
            use_param_files (bool): If True, use the _android_params.json files
        """
        print(f"Target language code list: {self.target_language_code_list}")
        print(f"Base language code: {self.base_language_code}")
        print(f"SDK: {self.sdk}")
        android_output_dir = "./sample_output/android"
        os.makedirs(android_output_dir, exist_ok=True)

        # Generate base language (default) strings.xml
        with open(f"./sample_data/sample_{self.base_language_code}.json", "r") as f:
            data_base = orjson.loads(f.read())
            xml_content = self.create_android_xml(data_base, self.base_language_code)
            with open(f"{android_output_dir}/strings.xml", "w", encoding="utf-8") as g:
                g.write(xml_content)

        # Generate localized strings.xml files for each target language
        for target_language_code in self.target_language_code_list:
            with open(f"./sample_data/sample_{target_language_code}.json", "r") as f:
                data_target = orjson.loads(f.read())            
                xml_content = self.create_android_xml(data_target, target_language_code)
                lang_dir = f"{android_output_dir}/values-{target_language_code}"
                os.makedirs(lang_dir, exist_ok=True)
                with open(f"{lang_dir}/strings.xml", "w", encoding="utf-8") as g:
                    g.write(xml_content)
        print("Android XML localization files generated successfully!")
        print(f"Files created in: {android_output_dir}")
        print("- strings.xml (default/base language)")
        for lang in self.target_language_code_list:
            print(f"- values-{lang}/strings.xml")


