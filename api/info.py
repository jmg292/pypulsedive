#https://pulsedive.com/api/indicators

import requests
import urllib.parse
from .models import Indicator

class InfoApi(object): 

    def __init__(self, config):
        self.url = config["url"]
        self.api_key = config["api_key"]

    def get_indicator_by_value(self, indicator):
        api_response = requests.get(
            url = urllib.parse.urljoin(self.url, f"/api/info.php?indicator={indicator}&key={self.api_key}"),
        )

        api_response.raise_for_status()
        response_json = api_response.json()
        indicator = Indicator.from_dictionary(response_json)
        return indicator
