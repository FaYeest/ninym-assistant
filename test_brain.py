from modules.brain import Brain
from colorama import Fore, init

init(autoreset=True)

def test_ninym():
    print(f"{Fore.YELLOW}[TEST] Initializing Ninym's brain...")
    try:
        ninym = Brain()
        
        test_message = "Ninym, coba baca link ini https://v9.kuramanime.tel/!"
        print(f"{Fore.WHITE}User: {test_message}")
        
        reply = ninym.think(test_message)
        
        print(f"{Fore.CYAN}Ninym: {reply}")
        
        if "Ninym" in reply or "Master" in reply or "asist" in reply.lower():
            print(f"\n{Fore.GREEN}[SUCCESS] Ninym is alive and responding with personality!")
        else:
            print(f"\n{Fore.YELLOW}[WARNING] Ninym responded, but personality might need tuning.")
            
    except Exception as e:
        print(f"{Fore.RED}[FAILED] Error during test: {e}")

if __name__ == "__main__":
    test_ninym()
