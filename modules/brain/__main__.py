from . import Brain
from colorama import Fore

if __name__ == "__main__":
    try:
        brain = Brain()
        print(f"{Fore.GREEN}Ninym Modular Brain Online (Groq Powered).")
        print(f"{Fore.WHITE}Type 'exit' to stop.")
        
        while True:
            txt = input(f"{Fore.YELLOW}You: ")
            if txt.lower() == "exit": 
                break
            if not txt.strip():
                continue
                
            reply = brain.think(txt)
            print(f"{Fore.CYAN}Ninym: {reply}")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[SYSTEM] Shutdown by user.")
