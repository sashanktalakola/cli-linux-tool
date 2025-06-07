import argparse
import copy
from types import SimpleNamespace


def setup_parser() -> SimpleNamespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("message", nargs="*")
    parser.add_argument("--provider", "-p", default=None,
                       help="LLM provider (default: loaded from config file, overrides config)")
    parser.add_argument("--model", "-m", default=None, 
                       help="Model to use (default: loaded from config file, overrides config)")
    parser.add_argument("--temperature", "-t", type=float, default=None,
                       help="Temperature setting (default: loaded from config file, overrides config)")
    parser.add_argument("--config", "-c", default="config.yaml",
                        help="Path to configuration file (default: config.yaml)")
    parser.add_argument("--system-prompt", "-s", 
                       help="System prompt to use")
    
    args = parser.parse_args()
    return args


def over_ride_config(config:SimpleNamespace, args: SimpleNamespace) -> SimpleNamespace:

    updated_config = copy.deepcopy(config)
    
    if args.provider is not None:
        updated_config.main.provider = args.provider
    
    if args.model is not None:
        updated_config.main.model_name = args.model
    
    if args.system_prompt is not None:
        updated_config.main.system_prompt = args.system_prompt
    
    if args.temperature is not None:
        provider = updated_config.main.provider
        
        if hasattr(updated_config, provider):
            provider_config = getattr(updated_config, provider)
            provider_config.temperature = args.temperature
    
    return updated_config