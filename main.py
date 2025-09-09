from textwrap import indent
import orjson
from src.sdk.sdk import sdk_list
from src.localize_creater.localize_creater_builder import LocalizeCreaterBuilder
def main():

    localize_creater_builder = LocalizeCreaterBuilder()
    localize_creater_builder.set_language_code_list(["ja", "ar", "de"])
    localize_creater_builder.set_base_language_code("en")
    localize_creater_builder.set_sdk("xcode")
    localize_creater = localize_creater_builder.build()

    print(f"Target language code list: {localize_creater.target_language_code_list}")
    print(f"Base language code: {localize_creater.base_language_code}.json")
    print(f"SDK: {localize_creater.sdk}")

    with open(f"./sample_data/sample_{localize_creater.base_language_code}.json", "r") as f:
        data_base = orjson.loads(f.read())
        new_data = {}
        new_data["@@locale"] = localize_creater.base_language_code
        new_data = { **new_data, **data_base }
        with open(f"./sample_output/dart/sample_{localize_creater.base_language_code}.arb", "w") as g:
            g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))


    # Output dart code
    with open(f"./sample_data/sample_{localize_creater.base_language_code}.json", "r") as f:
        data_base = orjson.loads(f.read())
        new_data = {}
        new_data["@@locale"] = localize_creater.base_language_code
        new_data = { **new_data, **data_base }
        with open(f"./sample_output/dart/app_{localize_creater.base_language_code}.arb", "w") as g:
            g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))
    for target_language_code in localize_creater.target_language_code_list:
        with open(f"./sample_data/sample_{target_language_code}.json", "r") as f:
            data_base = orjson.loads(f.read())
            new_data = {}
            new_data["@@locale"] = target_language_code
            new_data = { **new_data, **data_base }
            with open(f"./sample_output/dart/app_{target_language_code}.arb", "w") as g:
                g.write(orjson.dumps(new_data, option=orjson.OPT_INDENT_2).decode("utf-8"))


if __name__ == "__main__":
    main()