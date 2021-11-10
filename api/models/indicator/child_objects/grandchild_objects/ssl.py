class Ssl(object):

    FIELD_MAP = {
        "domain": "domain",
        "expires": "expires",
        "issuer": "issuer",
        "org": "org",
        "subject": "subject",
        "valid": "valid",
        "version": "version"
    }

    def __init__(self):
        self.domain = ""
        self.expires = ""
        self.issuer = ""
        self.org = ""
        self.subject = ""
        self.valid = ""
        self.version = ""

    @staticmethod
    def from_dictionary(ssl_dict: dict):
        ssl = Ssl()
        field_map = getattr(ssl.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in ssl_dict:
                setattr(ssl, field_map[key_name], ssl_dict[key_name])
        return ssl