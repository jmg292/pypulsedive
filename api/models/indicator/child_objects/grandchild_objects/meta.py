"""
class Meta(object):

    FIELD_MAP = {
        "assets": "",
        "author": "",
        "charset": "",
        "description": "",
        "keywords": "",
        "og:description": "",
        "og:image": "",
        "og:title": "",
        "og:url": "",
        "twitter:card": "",
        "twitter:creator": "",
        "twitter:description": "",
        "twitter:image": "",
        "twitter:site": "",
        "twitter:title": "",
        "version": "",
        "viewport": ""
    }

    def __init__(self):
        self.assets = ""
        self.author = ""
        self.charset = ""
        self.description = ""
        self.keywords = ""
        self.og:description = ""
        self.og:image = ""
        self.og:title = ""
        self.og:url = ""
        self.twitter:card = ""
        self.twitter:creator = ""
        self.twitter:description = ""
        self.twitter:image = ""
        self.twitter:site = ""
        self.twitter:title = ""
        self.version = ""
        self.viewport  = ""

    @staticmethod
    def from_dictionary(meta_dict: dict):
        meta = Meta()
        field_map = getattr(meta.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in meta_dict:
                setattr(meta, field_map[key_name], meta_dict[key_name])
        return meta
        """