import orjson
import xml.etree.ElementTree as ET
from xml.dom import minidom
from src.sdk.sdk import sdk_list
from src.localize_creater.localize_creater_builder import LocalizeCreaterBuilder
import os

def create_android():
    """
    Main function to generate Android XML localization files
    """
    localize_creater_builder = LocalizeCreaterBuilder()
    localize_creater_builder.set_language_code_list(["ja", "ar", "de"])
    localize_creater_builder.set_base_language_code("en")
    localize_creater_builder.set_sdk("android_studio")
    localize_creater = localize_creater_builder.build()

    print(f"Target language code list: {localize_creater.target_language_code_list}")
    print(f"Base language code: {localize_creater.base_language_code}")
    print(f"SDK: {localize_creater.sdk}")

    android_output_dir = "./sample_output/android"
    os.makedirs(android_output_dir, exist_ok=True)

    # Generate base language (default) strings.xml
    with open(f"./sample_data/sample_{localize_creater.base_language_code}.json", "r") as f:
        data_base = orjson.loads(f.read())
        xml_content = create_android_xml(data_base, localize_creater.base_language_code)
        with open(f"{android_output_dir}/strings.xml", "w", encoding="utf-8") as g:
            g.write(xml_content)

    # Generate localized strings.xml files for each target language
    for target_language_code in localize_creater.target_language_code_list:
        with open(f"./sample_data/sample_{target_language_code}.json", "r") as f:
            data_target = orjson.loads(f.read())            
            xml_content = create_android_xml(data_target, target_language_code)
            lang_dir = f"{android_output_dir}/values-{target_language_code}"
            os.makedirs(lang_dir, exist_ok=True)
            with open(f"{lang_dir}/strings.xml", "w", encoding="utf-8") as g:
                g.write(xml_content)
    print("Android XML localization files generated successfully!")
    print(f"Files created in: {android_output_dir}")
    print("- strings.xml (default/base language)")
    for lang in localize_creater.target_language_code_list:
        print(f"- values-{lang}/strings.xml")


def create_android_xml(data, language_code):
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