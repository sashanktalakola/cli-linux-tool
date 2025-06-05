from types import SimpleNamespace
import json


def dictToNameSpace(d: dict) -> SimpleNamespace:

    ns = json.loads(json.dumps(d), object_hook=lambda x: SimpleNamespace(**x))
    return ns