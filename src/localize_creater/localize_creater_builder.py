from src.locale_code.code_list import code_list
from src.sdk import sdk_list
from src.localize_creater.localize_creater import LocalizeCreater


class LocalizeCreaterBuilder:
    def __init__(self):
        self._localize_creater = LocalizeCreater()

    def set_base_language_code(self, language_code):
        self._localize_creater.base_language_code = language_code
        if language_code not in code_list:
            raise ValueError(f"Invalid language code: {language_code}")
        return self

    def set_language_code_list(self, language_code_list):
        new_language_code_list = []
        self._localize_creater.target_language_code_list = language_code_list
        for language_code in language_code_list:
            if language_code not in code_list:
                print(f"Invalid language code: {language_code}")
            else:
                new_language_code_list.append(language_code)
        return self

    def set_sdk(self, sdk_code):
        self._localize_creater.sdk = sdk_code
        if sdk_code not in sdk_list:
            raise ValueError(f"Invalid sdk code: {sdk_code}")
        return self

    def build(self):
        return self._localize_creater

