"""
class Http(object):

    FIELD_MAP = {
        "code": "++code",
        "content_type": "++content-type",
        "status": "++status",
        "cache_control": "cache-control",
        "connection": "connection",
        "content_encoding": "content-encoding",
        "content_length": "content-length",
        "content_type": "content-type",
        "date": "date",
        "expires": "expires",
        "keep_alive": "keep-alive",
        "pragma": "pragma",
        "server": "server",
        "set_cookie": "set-cookie",
        "strict_transport-security": "strict-transport-security",
        "vary": "vary",
        "x_content-type-options": "x-content-type-options",
        "x_frame_options": "x-frame-options",
        "x_xss_protection": "x-xss-protection"
    }

    def __init__(self):
        self.code = ""
        self.content-type = ""
        self.status = ""
        self.cache-control = ""
        self.connection = ""
        self.content-encoding = ""
        self.content-length = ""
        self.content-type = ""
        self.date = ""
        self.expires = ""
        self.keep-alive = ""
        self.pragma = ""
        self.server = ""
        self.set-cookie = ""
        self.strict-transport-security = ""
        self.vary = ""
        self.x-content-type-options = ""
        self.x-frame-options = ""
        self.x-xss-protection = ""

    @staticmethod
    def from_dictionary(attributes_dict: dict):
        attributes = Http()
        field_map = getattr(attributes.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in attributes_dict:
                setattr(attributes, field_map[key_name], attributes_dict[key_name])
            elif key_name in attributes_dict:
                
        return attributes
        """