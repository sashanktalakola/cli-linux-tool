from types import SimpleNamespace
import json
from typing import Optional


def dictToNameSpace(d: dict) -> SimpleNamespace:

    ns = json.loads(json.dumps(d), object_hook=lambda x: SimpleNamespace(**x))
    return ns

def getAPIKey(config: SimpleNamespace) -> Optional[str]:

    api_key = None
    provider_config = getattr(config, config.main.provider)
    if hasattr(provider_config, "api_key"):
        api_key = getattr(provider_config, "api_key")

    return api_key