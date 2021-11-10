from .api import Indicator, InfoApi
from .config_object import Configuration


configuration = Configuration()


def find_indicator(indicator: str) -> Indicator:
    """
        Search the Pulsedive API for a given indicator.

        Parameters:

            indicator: The indicator to search for

        Returns:

            An `InfoApi` object
    """
    if not configuration.api_key:
        raise ValueError("No API key was provided.")
    info_api_client = InfoApi(configuration)
    return info_api_client.get_indicator_by_value(indicator)

__all__ = [
    "configuration",
    "find_indicator"
]