from src.localize_creater.localize_creater_builder import LocalizeCreaterBuilder
def main():
    localize_creater_builder = LocalizeCreaterBuilder()
    localize_creater_builder.set_language_code_list(["ja", "ar", "de"])
    localize_creater_builder.set_base_language_code("en")
    localize_creater_builder.set_sdk("xcode")

    localize_creater = localize_creater_builder.build()
    # localize_creater.create_flutter()
    localize_creater.create_android()

if __name__ == "__main__":
    main()
