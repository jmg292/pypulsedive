class Dom(object):

    FIELD_MAP = {
        "screenshot": "screenshot"
    }

    def __init__(self):
        self.screenshot = ""

    @staticmethod
    def from_dictionary(dom_dict: dict):
        dom = Dom()
        field_map = getattr(dom.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in dom_dict:
                setattr(dom, field_map[key_name], dom_dict[key_name])
        return dom