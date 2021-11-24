#https://pulsedive.com/api/indicators

import requests
import urllib.parse
from .models import Indicator
from ..config_object import Configuration

class InfoApi(object): 

    def __init__(self, config: Configuration):
        self._config = config

    def get_indicator_by_value(self, indicator):
        api_response = requests.get(
            url = urllib.parse.urljoin(
                self._config.url, 
                f"/api/info.php?indicator={urllib.parse.quote(indicator)}&key={self._config.api_key}"),
        )

        #api_response.raise_for_status()
        response_json = api_response.json()
        return response_json
        #indicator = Indicator.from_dictionary(response_json)
        #return indicator
