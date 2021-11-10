class Attributes(object):

    FIELD_MAP = {
        "port": "port",
        "protocol": "protocol",
        "technology": "technology"
    }

    def __init__(self):
        self.port = ""
        self.protocol = ""
        self.technology = ""

    @staticmethod
    def from_dictionary(attributes_dict: dict):
        attributes = Attributes()
        field_map = getattr(attributes.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in attributes_dict:
                setattr(attributes, field_map[key_name], attributes_dict[key_name])
        return attributes