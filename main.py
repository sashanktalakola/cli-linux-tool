#!/usr/bin/env python3

import os
import yaml
import sys
import subprocess
from utils import dictToNameSpace

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.yaml')

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        config = dictToNameSpace(config)

    api_key = None
    if hasattr(config, "api_keys"):
        api_key = getattr(config.api_keys, config.main.provider)

    provider = config.main.provider
    model_name = config.main.model_name

    llm = init_chat_model(
        model_provider=provider,
        model=model_name,
        api_key=api_key,
        temperature=1.0
    )

    user_query = " ".join(sys.argv[1:])
    messages = [
        SystemMessage(content="You are an AI assistant that translates natural language descriptions into appropriate Linux/Unix commands. Respond ONLY with the command itself - no explanations, no markdown formatting. For example, if asked 'list all files', respond only with 'ls'."),
        HumanMessage(content=user_query)
    ]

    response = llm.invoke(messages)
    command = response.content

    print(f"\033[1;32mCommand: {command}\033[0m")
    confirm = input("Execute this command? [y/N]: ").lower().strip()

    if confirm.lower() == "y":
        print()
        try:
            result = subprocess.run(command, shell=True, text=True, check=True)
            return result
        except Exception as e:
            print(f"\033[1;31mError executing command: {str(e)}\033[0m")
            return 1

    else:
        print(f"\033[1;33mCommand execution cancelled.\033[0m")
        return 1


if __name__ == "__main__":
    main()