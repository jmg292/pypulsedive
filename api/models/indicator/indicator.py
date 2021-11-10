from .child_objects.attributes import Attributes
from .child_objects.comments import Comments
from .child_objects.properties import Properties
from .child_objects.redirects import Redirects
from .child_objects.riskfactors import RiskFactors


class Indicator(object):

    FIELD_MAP = {
        "attributes" : "attributes",
        "comments" : "comments",
        "iid" : "iid",
        "indicator" : "indicator",
        "mapretired" : "mapretired",
        "properties" : "properties",
        "recent" : "recent",
        "redirects" : "redirects",
        "risk" : "risk",
        "risk_recommended" : "risk_recommended",
        "riskfactors" : "riskfactors",
        "stamp_added" : "stamp_added",
        "stamp_probed" : "stamp_probed",
        "stamp_retired" : "stamp_retired",
        "stamp_seen" : "stamp_seen",
        "stamp_updated" : "stamp_updated",
        "submissions" : "submissions",
        "type" : "type"
    }

    def __init__(self):
        self.attributes = ""
        self.comments = ""
        self.iid = ""
        self.indicator = ""
        self.mapretired = ""
        self.properties = ""
        self.recent = ""
        self.redirects = ""
        self.risk = ""
        self.risk_recommended = ""
        self.riskfactors = ""
        self.stamp_added = ""
        self.stamp_probed = ""
        self.stamp_retired = ""
        self.stamp_seen = ""
        self.stamp_updated = ""
        self.submissions = ""
        self.type = ""

    @staticmethod
    def from_dictionary(indicator_dict: dict):
        indicator = Indicator()
        field_map = getattr(indicator.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in indicator_dict:
                setattr(indicator, field_map[key_name], indicator_dict[key_name])
        indicator.attributes = Attributes.from_dictionary(indicator.attributes)
        indicator.comments = [Comments.from_dictionary(comment) for comment in indicator.comments]
        indicator.properties = Properties.from_dictionary(indicator.properties)
        indicator.redirects = Redirects.from_dictionary(indicator.redirects)
        indicator.riskfactors = [RiskFactors.from_dictionary(riskfactor) for riskfactor in indicator.riskfactors]
        return indicator