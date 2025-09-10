import orjson
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom


class LocalizeCreater:
    def __init__(self):
        self.target_language_code_list = []
        self.base_language_code = None
        self.sdk = None

    def create_flutter(self):
        print(f"Target language code list: {self.target_language_code_list}")
        print(f"Base language code: {self.base_language_code}.json")
        print(f"SDK: {self.sdk}")
        with open(f"./sample_data/sample_{self.base_language_code}.json", "r") as f:
            data_base = orjson.loads(f.read())
            new_data = {}
            new_data["@@locale"] = self.base_language_code
            converted_data = {}
            for key, value in data_base.items():
                converted_data[key] = self.convert_parameters_for_platform(value, 'flutter')            
            new_data = { **new_data, **converted_data }
            new_data = self._add_flutter_parameter_placeholders(new_data)
            with open(f"./sample_output/dart/app_{self.base_language_code}.arb", "w") as g:
                g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))
        for target_language_code in self.target_language_code_list:
            with open(f"./sample_data/sample_{target_language_code}.json", "r") as f:
                data_base = orjson.loads(f.read())
                new_data = {}
                new_data["@@locale"] = target_language_code
                
                # Convert parameters for Flutter platform
                converted_data = {}
                for key, value in data_base.items():
                    converted_data[key] = self.convert_parameters_for_platform(value, 'flutter')
                
                new_data = { **new_data, **converted_data }
                
                # Add parameter placeholders for Flutter ARB format
                new_data = self._add_flutter_parameter_placeholders(new_data)
                
                with open(f"./sample_output/dart/app_{target_language_code}.arb", "w") as g:
                    g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))
        
        print("Flutter ARB files with unified parameters generated successfully!")
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

    def convert_parameters_for_platform(self, text, platform):
        """
        Convert Android-style parameters to platform-specific format
        
        Args:
            text (str): Text with Android-style parameters (%1$s, %2$d, etc.)
            platform (str): Target platform ('android', 'flutter', 'xcode')
            
        Returns:
            str: Text with platform-specific parameters
        """
        import re
        
        if platform == 'android':
            # Android format - no conversion needed
            return text
        elif platform == 'flutter':
            # Convert Android format to Flutter format
            # %1$s, %2$s, %3$s -> {param1}, {param2}, {param3}
            # %1$d, %2$d, %3$d -> {param1}, {param2}, {param3}
            # %1$.2f, %2$.3f -> {param1}, {param2}
            
            # Find all Android-style parameters
            android_pattern = r'%(\d+)\$[sd]'
            android_float_pattern = r'%(\d+)\$\.\d+[f]'
            
            # Replace integer/string parameters
            def replace_int_string(match):
                param_num = match.group(1)
                return f"{{param{param_num}}}"
            
            # Replace float parameters
            def replace_float(match):
                param_num = match.group(1)
                return f"{{param{param_num}}}"
            
            # Apply replacements
            text = re.sub(android_pattern, replace_int_string, text)
            text = re.sub(android_float_pattern, replace_float, text)
            
            return text
        elif platform == 'xcode':
            # Convert Android format to Xcode format
            # %1$s, %2$s, %3$s -> %@, %@, %@
            # %1$d, %2$d, %3$d -> %@, %@, %@
            # %1$.2f, %2$.3f -> %@, %@
            
            # Find all Android-style parameters
            android_pattern = r'%(\d+)\$[sd]'
            android_float_pattern = r'%(\d+)\$\.\d+[f]'
            
            # Replace with Xcode format
            text = re.sub(android_pattern, '%@', text)
            text = re.sub(android_float_pattern, '%@', text)
            
            return text
        elif platform == 'react':
            # Convert Android format to React Native format
            # %1$s, %2$s, %3$s -> {0}, {1}, {2}
            # %1$d, %2$d, %3$d -> {0}, {1}, {2}
            # %1$.2f, %2$.3f -> {0}, {1}
            
            # Find all Android-style parameters
            android_pattern = r'%(\d+)\$[sd]'
            android_float_pattern = r'%(\d+)\$\.\d+[f]'
            
            # Replace with React Native format (convert to 0-based index)
            def replace_react(match):
                param_num = int(match.group(1)) - 1  # Convert to 0-based index
                return f"{{{param_num}}}"
            
            text = re.sub(android_pattern, replace_react, text)
            text = re.sub(android_float_pattern, replace_react, text)
            
            return text
        else:
            return text

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

    def create_android(self, use_unified=True):
        """
        Create Android XML string resources files with unified parameter handling
        
        Args:
            use_unified (bool): If True, use the unified JSON files with Android-style parameters
        """
        print(f"Target language code list: {self.target_language_code_list}")
        print(f"Base language code: {self.base_language_code}")
        print(f"SDK: {self.sdk}")
        
        file_suffix = "_unified" if use_unified else ""
        android_output_dir = "./sample_output/android"
        os.makedirs(android_output_dir, exist_ok=True)

        # Generate base language (default) strings.xml
        with open(f"./sample_data/sample_{self.base_language_code}{file_suffix}.json", "r") as f:
            data_base = orjson.loads(f.read())
            # Convert parameters for Android platform (no conversion needed, but for consistency)
            converted_data = {}
            for key, value in data_base.items():
                converted_data[key] = self.convert_parameters_for_platform(value, 'android')
            
            xml_content = self.create_android_xml(converted_data, self.base_language_code)
            with open(f"{android_output_dir}/strings.xml", "w", encoding="utf-8") as g:
                g.write(xml_content)

        # Generate localized strings.xml files for each target language
        for target_language_code in self.target_language_code_list:
            with open(f"./sample_data/sample_{target_language_code}{file_suffix}.json", "r") as f:
                data_target = orjson.loads(f.read())
                # Convert parameters for Android platform (no conversion needed, but for consistency)
                converted_data = {}
                for key, value in data_target.items():
                    converted_data[key] = self.convert_parameters_for_platform(value, 'android')
                
                xml_content = self.create_android_xml(converted_data, target_language_code)
                lang_dir = f"{android_output_dir}/values-{target_language_code}"
                os.makedirs(lang_dir, exist_ok=True)
                with open(f"{lang_dir}/strings.xml", "w", encoding="utf-8") as g:
                    g.write(xml_content)
        
        print("Android XML localization files with unified parameters generated successfully!")
        print(f"Files created in: {android_output_dir}")
        print("- strings.xml (default/base language)")
        for lang in self.target_language_code_list:
            print(f"- values-{lang}/strings.xml")

    def create_xcode(self, use_unified=True):
        """
        Create Xcode .xcstrings localization files with unified parameter handling
        
        Args:
            use_unified (bool): If True, use the unified JSON files with Android-style parameters
        """
        print(f"Target language code list: {self.target_language_code_list}")
        print(f"Base language code: {self.base_language_code}")
        print(f"SDK: {self.sdk}")

        file_suffix = "_unified" if use_unified else ""
        xcode_output_dir = "./sample_output/xcode"
        os.makedirs(xcode_output_dir, exist_ok=True)

        # Create the main .xcstrings structure
        xcstrings_data = {
            "sourceLanguage": self.base_language_code,
            "strings": {},
            "version": "1.0"
        }

        # Process all target languages
        all_languages = [self.base_language_code] + self.target_language_code_list
        
        for lang_code in all_languages:
            with open(f"./sample_data/sample_{lang_code}{file_suffix}.json", "r") as f:
                lang_data = orjson.loads(f.read())
                
            # Add each string to the xcstrings structure
            for key, value in lang_data.items():
                if key not in xcstrings_data["strings"]:
                    xcstrings_data["strings"][key] = {
                        "localizations": {}
                    }
                
                # Convert parameters for Xcode platform
                converted_value = self.convert_parameters_for_platform(value, 'xcode')
                
                # Add localization for this language
                xcstrings_data["strings"][key]["localizations"][lang_code] = {
                    "stringUnit": {
                        "state": "translated",
                        "value": converted_value
                    }
                }

        # Write the .xcstrings file
        output_file = f"{xcode_output_dir}/Localizable.xcstrings"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(orjson.dumps(xcstrings_data, option=orjson.OPT_INDENT_2).decode("utf-8"))

        print("Xcode .xcstrings localization file with unified parameters generated successfully!")
        print(f"File created: {output_file}")
        print(f"Languages included: {', '.join(all_languages)}")

    def create_react(self):
        """
        Create React Native localization JavaScript files
        """
        print(f"Target language code list: {self.target_language_code_list}")
        print(f"Base language code: {self.base_language_code}")
        print(f"SDK: {self.sdk}")

        react_output_dir = "./sample_output/javascript"
        os.makedirs(react_output_dir, exist_ok=True)

        # Create the main localization object
        localization_data = {}
        all_languages = [self.base_language_code] + self.target_language_code_list
        
        for lang_code in all_languages:
            with open(f"./sample_data/sample_{lang_code}.json", "r") as f:
                lang_data = orjson.loads(f.read())
                
            # Convert parameters for React Native platform
            converted_data = {}
            for key, value in lang_data.items():
                converted_data[key] = self.convert_parameters_for_platform(value, 'react')
            
            localization_data[lang_code] = converted_data

        # Generate JavaScript file content
        js_content = self._generate_react_js_content(localization_data)

        # Write the JavaScript file
        output_file = f"{react_output_dir}/LocalizedStrings.js"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(js_content)

        print("React Native localization JavaScript file generated successfully!")
        print(f"File created: {output_file}")
        print(f"Languages included: {', '.join(all_languages)}")

    def _generate_react_js_content(self, localization_data):
        """
        Generate JavaScript content for React Native localization
        
        Args:
            localization_data (dict): Dictionary containing all language data
            
        Returns:
            str: JavaScript file content
        """
        import json
        
        # Start building the JavaScript content
        js_lines = [
            "import LocalizedStrings from 'react-native-localization';",
            "",
            "// CommonJS syntax",
            "// let LocalizedStrings = require('react-native-localization');",
            "",
            "let strings = new LocalizedStrings({"
        ]
        
        # Add each language
        for lang_code, lang_data in localization_data.items():
            js_lines.append(f'  "{lang_code}": {{')
            
            # Add each key-value pair
            for key, value in lang_data.items():
                # Escape quotes in the value
                escaped_value = value.replace('"', '\\"')
                js_lines.append(f'    {key}: "{escaped_value}",')
            
            # Remove trailing comma from last item
            if js_lines[-1].endswith(','):
                js_lines[-1] = js_lines[-1][:-1]
            
            js_lines.append('  },')
        
        # Remove trailing comma from last language
        if js_lines[-1].endswith(','):
            js_lines[-1] = js_lines[-1][:-1]
        
        # Close the object and export
        js_lines.extend([
            "});",
            "",
            "export default strings;",
            "",
            "// Usage example:",
            "// import strings from './LocalizedStrings';",
            "// console.log(strings.greeting);",
            "// console.log(strings.formatString(strings.welcome_message, ['John']));"
        ])
        
        return '\n'.join(js_lines)


