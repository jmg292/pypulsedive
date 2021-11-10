import json


class Configuration(object):

    def __init__(self, **kwargs):
        self.url = "https://www.pulsedive.com"
        self.api_key = ""
        for keyword_argument in kwargs:
            if hasattr(self, keyword_argument):
                setattr(self, keyword_argument, kwargs[keyword_argument])

    @staticmethod
    def from_dictionary(config_dictionary: dict):
        return Configuration(**config_dictionary)

    @staticmethod
    def from_json(config_json: str):
        return Configuration.from_dictionary(json.loads(config_json))
