import json
CONFIG_FILE = r"C:\PY\ПРИМЕРЫ КОДА\PYTHON622\lesson_29_config.json"

class Config:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.__polza_api_key = ""
        self.__model = ""
        self.__polza_base_url = ""
        self.__system_prompt = ""


    def __read_json_config(self):
        try:
            with open(self.config_file, encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("JSON файл конфига не обнаружен")

        except json.JSONDecodeError:
            raise Exception("Файл конфига битый")

    def __read_prompt_txt(self, system_prompt_file: str):
        try:
            with open(system_prompt_file, encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]

        except FileNotFoundError:
            raise FileNotFoundError("Промпт файл не обнаружен")


    def load(self):
        config_data = self.__read_json_config()
        # ПО ХОРОШЕМУ ТУТ НАДО ПРОВЕРИТЬ ЧТО КОНФИГ ПРАВИЛЬНЫЙ, как минимум что данные есть внутри
        system_prompt_file = config_data["system_prompt"]
        self.__system_prompt = self.__read_prompt_txt(system_prompt_file)

        # Если все файлы прочитаны мы можем продолжить определять другие части конфига
        self.__polza_api_key = config_data["polza_api_key"]
        self.__model = config_data["model"]
        self.__polza_base_url = config_data["polza_base_url"]


    @property
    def polza_api_key(self):
        return self.__polza_api_key

    @property
    def model(self):
        return self.__model

    @property
    def polza_base_url(self):
        return self.__polza_base_url

    @property
    def system_prompt(self):
        return self.__system_prompt


config = Config(CONFIG_FILE)
config.load()

print(config.system_prompt)
# config.system_prompt = "Чербурек"
# AttributeError: property 'system_prompt' of 'Config' object has no setter