class Geo(object):

    FIELD_MAP = {
        "address": "address",
        "city": "city",
        "country": "country",
        "countrycode": "countrycode",
        "org": "org",
        "region": "region",
        "zip": "zip"
    }

    def __init__(self):
        self.address = ""
        self.city = ""
        self.country = ""
        self.countrycode = ""
        self.org = ""
        self.region = ""
        self.zip = ""

    @staticmethod
    def from_dictionary(geo_dict: dict):
        geo = Geo()
        field_map = getattr(geo.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in geo_dict:
                setattr(geo, field_map[key_name], geo_dict[key_name])
        return geo