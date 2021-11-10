class RiskFactors(object):

    FIELD_MAP = {
        "description": "description",
        "rfid": "rfid",
        "risk": "risk"
    }

    def __init__(self):
        self.description = ""
        self.rfid = ""
        self.risk = ""

    @staticmethod
    def from_dictionary(riskfactors_dict: dict):
        riskfactors = RiskFactors()
        field_map = getattr(riskfactors.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in riskfactors_dict:
                setattr(riskfactors, field_map[key_name], riskfactors_dict[key_name])
        return riskfactors