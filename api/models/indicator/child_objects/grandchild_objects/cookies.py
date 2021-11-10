class Cookies(object):

    FIELD_MAP = {
        "phpsessid": "phpsessid"
    }

    def __init__(self):
        self.phpsessid = ""

    @staticmethod
    def from_dictionary(cookies_dict: dict):
        cookies = Cookies()
        field_map = getattr(cookies.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in cookies_dict:
                setattr(cookies, field_map[key_name], cookies_dict[key_name])
        return cookies