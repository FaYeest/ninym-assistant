import json
import sys
import os
from colorama import init, Fore

init(autoreset=True)

CONFIG_PATH = os.path.join("core", "config.json")

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=4)

def switch_provider(provider):
    config = load_config()
    
    if provider.lower() not in ["ollama", "groq"]:
        print(f"{Fore.RED}Invalid provider! Use 'ollama' or 'groq'.")
        return

    config["llm_provider"] = provider.lower()
    save_config(config)
    print(f"{Fore.GREEN}Successfully switched to: {Fore.YELLOW}{provider.upper()}")
    
    if provider == "ollama":
        print(f"Model: {config.get('ollama_model')}")
    else:
        print(f"Model: {config.get('groq_model')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python switch_model.py [ollama|groq]")
        current = load_config().get("llm_provider", "unknown")
        print(f"Current Provider: {Fore.CYAN}{current}")
    else:
        switch_provider(sys.argv[1])
