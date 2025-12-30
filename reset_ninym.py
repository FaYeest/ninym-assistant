import os
import shutil
import json
import sys
from colorama import init, Fore, Style

init(autoreset=True)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "core", "memory.json")
PROFILE_FILE = os.path.join(BASE_DIR, "core", "user_profile.json")
VECTOR_DB_DIR = os.path.join(BASE_DIR, "core", "chroma_db")

DEFAULT_PROFILE = {
    "user_name": "Farras",
    "facts": [],
    "mood": "neutral",
    "affection": 0
}

def reset_all():
    print(f"{Fore.RED}{Style.BRIGHT}!!! WARNING: NINYM FACTORY RESET !!!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}This will delete:")
    print(f"1. Chat Memory ({MEMORY_FILE})")
    print(f"2. User Profile/Affection ({PROFILE_FILE})")
    print(f"3. Vector DB Knowledge ({VECTOR_DB_DIR})")
    
    confirm = input(f"\n{Fore.WHITE}Are you sure? (Type 'YES' to confirm): ")
    
    if confirm != "YES":
        print(f"{Fore.GREEN}Reset cancelled.")
        return

    # 1. Reset Memory
    if os.path.exists(MEMORY_FILE):
        try:
            os.remove(MEMORY_FILE)
            print(f"{Fore.GREEN}[OK] Memory deleted.")
        except Exception as e:
            print(f"{Fore.RED}[FAIL] Could not delete memory: {e}")
    else:
        print(f"{Fore.YELLOW}[SKIP] No memory file found.")

    # 2. Reset Profile
    try:
        with open(PROFILE_FILE, 'w') as f:
            json.dump(DEFAULT_PROFILE, f, indent=2)
        print(f"{Fore.GREEN}[OK] Profile reset to default (Affection: 0).")
    except Exception as e:
        print(f"{Fore.RED}[FAIL] Could not reset profile: {e}")

    # 3. Reset Vector DB
    if os.path.exists(VECTOR_DB_DIR):
        try:
            shutil.rmtree(VECTOR_DB_DIR)
            print(f"{Fore.GREEN}[OK] Vector DB wiped.")
        except Exception as e:
            print(f"{Fore.RED}[FAIL] Could not delete Vector DB: {e}")
    else:
        print(f"{Fore.YELLOW}[SKIP] No Vector DB found.")

    print(f"\n{Fore.CYAN}{Style.BRIGHT}✨ Ninym has been reset to factory settings. ✨")

if __name__ == "__main__":
    reset_all()
