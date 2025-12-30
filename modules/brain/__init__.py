import sys
import os
import re
from colorama import Fore

# Setup Path to Root
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from tools.web_search import WebSearch
from modules.rag.rag_engine import RagEngine
from core.profile_manager import ProfileManager

# Sub-modules
from .llm_client import LLMClient
from .memory import MemoryManager
from .prompt_builder import PromptBuilder
from .output_parser import OutputParser

class Brain:
    def __init__(self, memory_file="core/memory.json"):
        print(f"{Fore.CYAN}[SYSTEM] Initializing Modular Brain...")
        
        # 1. Init Components
        self.profile = ProfileManager()
        self.llm = LLMClient()
        self.memory = MemoryManager(memory_file)
        self.prompt_builder = PromptBuilder(self.profile)
        self.parser = OutputParser(self.profile)
        self.web_search = WebSearch()
        self.rag = RagEngine()

        # 2. Init Session
        system_instr = self.prompt_builder.build_system_instruction()
        self.history = self.memory.load_history(system_instr)

    def _smart_search(self, user_input):
        """Uses LLM to extract a clean search query from user input."""
        # Removed generic words like "siapa", "apa itu", "dimana" to prevent false positives during chat.
        search_triggers = ["cariin", "carikan", "berita", "terbaru", "harga", "cuaca", "info tentang", "alur cerita"]
        
        # Simple Trigger Check
        if not any(t in user_input.lower() for t in search_triggers):
            return ""

        print(f"{Fore.YELLOW}[TOOL] Detecting Search Intent...")
        
        # LLM Call to extract query (Logic Mode, No Personality)
        prompt = [
            {"role": "system", "content": "You are a Search Query Extractor. Extract the main topic. If user asks for news/price, add 'terbaru' or 'hari ini' to the query. Output ONLY the query."},
            {"role": "user", "content": f"Extract search query from: '{user_input}'"}
        ]
        
        try:
            # Consume stream for tool usage (non-interactive)
            query_generator = self.llm.generate_response(prompt, temperature=0.1)
            query = "".join([chunk for chunk in query_generator]).strip()
            
            # Cleanup if model is chatty
            if "Search query:" in query: query = query.replace("Search query:", "").strip()
            if "'" in query: query = query.replace("'", "").strip()
            
            print(f"{Fore.GREEN}[TOOL] Optimized Query: '{query}'")
            return self.web_search.search(query)
        except Exception as e:
            print(f"{Fore.RED}[TOOL ERROR] {e}")
            return ""

    def think(self, user_input):
        # 1. Gather Context (RAG & Smart Web Search)
        local_data = self.rag.search(user_input)
        web_data = ""
        
        # A. URL DETECTION (Direct Link Reader)
        url_match = re.search(r'(https?://\S+)', user_input)
        if url_match:
            target_url = url_match.group(1)
            print(f"{Fore.YELLOW}[TOOL] URL Detected. Reading content...")
            raw_content = self.web_search.read_url(target_url)
            web_data = f"Content of {target_url}:\n{raw_content}"
        
        # B. SMART SEARCH (Fallback if no URL)
        else:
            web_data = self._smart_search(user_input)
        
        # 2. Build Final Prompt
        final_input = self.prompt_builder.construct_context(user_input, local_data, web_data)
        
        # 3. Add to Memory (Transient State)
        self.memory.add_message("user", final_input)
        
        # 4. Generate (LLM Stream)
        print(f"{Fore.CYAN}Ninym: {Fore.RESET}", end="", flush=True)
        
        full_reply = ""
        stream_generator = self.llm.generate_response(self.memory.history)
        
        # STREAMING LOOP
        for chunk in stream_generator:
            print(chunk, end="", flush=True) # Efek ngetik real-time
            full_reply += chunk
            
        print() # Newline at the end

        # 5. Parse Output (Thought, Meta, Speech) -> Post-Processing
        thought, speech = self.parser.parse(full_reply)
        
        # 6. Finalize Memory (Clean up)
        self.memory.update_last_user_message(user_input) 
        self.memory.add_message("assistant", full_reply)
        self.memory.save_history()
        
        return speech

if __name__ == "__main__":
    brain = Brain()
    print(f"{Fore.GREEN}Ninym Modular Brain Online.")
    while True:
        txt = input(f"{Fore.YELLOW}You: ")
        if txt.lower() == "exit": break
        reply = brain.think(txt)
        # Note: 'reply' is the parsed speech.
        # But we already printed the raw stream above.
        # So we don't need to print 'reply' again to avoid double output.