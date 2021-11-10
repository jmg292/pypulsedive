class Redirects(object):

    FIELD_MAP = {
        "to": "to"
    }

    def __init__(self):
        self.to = ""

    @staticmethod
    def from_dictionary(location_information_dict: dict):
        location_information = Redirects()
        field_map = getattr(location_information.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in location_information_dict:
                setattr(location_information, field_map[key_name], location_information_dict[key_name])
        return location_information