from .grandchild_objects import Cookies
from .grandchild_objects import Dns
from .grandchild_objects import Dom
from .grandchild_objects import Geo
#from .grandchild_objects import Http
#from .grandchild_objects import Meta
from .grandchild_objects import Ssl
#from .grandchild_objects import WhoIs

class Properties(object):

    FIELD_MAP = {
        "cookies": "cookies",
        "dns": "dns",
        "dom": "dom",
        "geo": "geo",
        "http": "http",
        "meta": "meta",
        "ssl": "ssl",
        "whois": "whois"
    }

    def __init__(self):
        self.cookies = ""
        self.dns = ""
        self.dom = ""
        self.geo = ""
        self.http = ""
        self.meta = ""
        self.ssl = ""
        self.whois = ""

    @staticmethod
    def from_dictionary(properties_dict: dict):
        properties = Properties()
        field_map = getattr(properties.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in properties_dict:
                setattr(properties, field_map[key_name], properties_dict[key_name])
        properties.cookies = Cookies.from_dictionary(properties.cookies)
        properties.dns = Dns.from_dictionary(properties.dns)
        properties.dom = Dom.from_dictionary(properties.dom)
        properties.geo = Geo.from_dictionary(properties.geo)
        #properties.http = Http.from_dictionary(properties.http)
        #properties.meta = Meta.from_dictionary(properties.meta)
        properties.ssl = Ssl.from_dictionary(properties.ssl)
        #properties.whois = WhoIs.from_dictionary(properties.whois)
        return properties