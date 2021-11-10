class Dns(object):

    FIELD_MAP = {
        "a": "a",
        "mname": "mname",
        "mx": "mx",
        "ns": "ns",
        "rname": "rname",
        "soa": "soa",
        "txt": "txt"
    }

    def __init__(self):
        self.a = ""
        self.mname = ""
        self.mx = ""
        self.ns = ""
        self.rname = ""
        self.soa = ""
        self.txt = ""

    @staticmethod
    def from_dictionary(dns_dict: dict):
        dns = Dns()
        field_map = getattr(dns.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in dns_dict:
                setattr(dns, field_map[key_name], dns_dict[key_name])
        return dns