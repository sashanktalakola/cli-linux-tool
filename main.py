#!/usr/bin/env python3

import os
import yaml
import sys
from openai import OpenAI
import subprocess
from utils import dictToNameSpace

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.yaml')

with open(config_path, "r") as file:
    config = yaml.safe_load(file)
    config = dictToNameSpace(config)

api_key = getattr(config.api_keys, config.main.provider)
client = OpenAI(
    api_key=api_key
)

user_query = " ".join(sys.argv[1:])
messages = [

    {
        "role": "system",
        "content": "You are an AI assistant that translates natural language descriptions into appropriate Linux/Unix commands. Respond ONLY with the command itself - no explanations, no markdown formatting. For example, if asked 'list all files', respond only with 'ls'."
    },

    {
        "role": "user",
        "content": user_query
    }

]

response = client.responses.create(
    model=config.main.model_name,
    input=messages
)

command = response.output_text

print(f"\033[1;32mCommand: {command}\033[0m")
confirm = input("Execute this command? [y/N]: ").lower().strip()
print()

if confirm.lower() == "y":
    try:
        result = subprocess.run(command, shell=True, text=True, check=True)
    except Exception as e:
        print(f"\033[1;31mError executing command: {str(e)}\033[0m")

else:
    print(f"\033[1;33mCommand execution cancelled.\033[0m")