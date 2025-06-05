# /ai Linux Commands CLI Tool

A command-line interface application that provides intelligent Linux command suggestions using Large Language Models (LLMs). Simply describe what you want to do, and get the appropriate Linux command with confirmation before execution.

## Features
* 🤖 AI-powered Linux command generation
* 🔒 Secure execution with user confirmation prompt (y/N) to prevent unintended actions
* 🔧 Support for multiple LLM providers (OpenAI, Anthropic, Ollama, etc.)
* ⚙️ Configurable via YAML file
* 🚀 Simple and intuitive command-line interface

## Usage
Use the `/ai` command followed by a description of what you want to accomplish:
```bash
/ai find all .txt files in current directory
/ai compress folder backup into tar.gz
/ai show disk usage for each directory
/ai kill process running on port 8080
/ai create a new user named 'developer'
```

## Example
```bash
$ /ai list all running docker containers
Command: docker ps

Execute this command? (y/N): y
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
abc123def456   nginx     ...       ...       ...       ...       webserver
```


## Installation
```bash

git clone https://github.com/sashanktalakola/cli-linux-tool.git
cd cli-linux-tool

pip install -r requirements.txt
chmod +x main.py
```

## Configuration
1. Setup the configuration file

    Copy the example configuration file:
    ```bash
    cp config.yaml.example config.yaml
    ```
    Edit `config.yaml` to configure your preferred LLM provider and model

2. Configure shell alias

    Add the following function and alias to your `~/.zshrc` file to enable the `/ai` command:

    ```bash
    ai() {
        if [ $# -eq 0 ]; then
            echo "Usage: /ai <message>"
            return 1
        fi
        # If you're not using a virtual environment (venv), comment out the `source` and `deactivate` lines below,
        # and ensure the required Python packages are installed system-wide (e.g., via pip).
        source /path/to/venv/bin/activate
        python3 /path/to/python/script.py "$@"
        deactivate
    }
    alias /ai='ai'
    ```

**Important**: Update the paths in the function:
* Replace `/path/to/venv/bin/activate` with the actual path to your virtual environment
* Replace `/path/to/python/script.py` with the actual path to your Python script

After adding this to your `~/.zshrc`, reload your shell configuration:
```bash
source ~/.zshrc
```

Note for Bash users: If you're using Bash instead of Zsh, add the same configuration to your `~/.bashrc` file.