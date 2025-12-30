import os
import json
import ollama
from groq import Groq
from dotenv import load_dotenv
from colorama import Fore

# Load environment variables explicitly
load_dotenv()

class LLMClient:
    def __init__(self):
        self.config = self._load_config()
        self.provider = self.config.get("llm_provider", "ollama")
        
        if self.provider == "groq":
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                print(f"{Fore.RED}[ERROR] GROQ_API_KEY not found! Fallback to Ollama.")
                self.provider = "ollama"
            else:
                self.client = Groq(api_key=api_key)
                self.model_id = self.config.get("groq_model", "llama-3.3-70b-versatile")
                print(f"{Fore.CYAN}[LLM] Using Cloud Groq: {self.model_id}")

        if self.provider == "ollama":
            self.model_id = self.config.get("ollama_model", "huihui_ai/qwen2.5-abliterate:3b")
            print(f"{Fore.CYAN}[LLM] Using Local Ollama: {self.model_id}")

    def _load_config(self):
        try:
            path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "core", "config.json")
            with open(path, "r") as f:
                return json.load(f)
        except:
            return {"llm_provider": "ollama"}

    def generate_response(self, messages, temperature=0.7):
        # 1. GROQ HANDLER (STREAMING)
        if self.provider == "groq":
            try:
                stream = self.client.chat.completions.create(
                    messages=messages,
                    model=self.model_id,
                    temperature=temperature,
                    max_tokens=1024,
                    stream=True  # ENABLE STREAM
                )
                for chunk in stream:
                    content = chunk.choices[0].delta.content
                    if content:
                        yield content
            except Exception as e:
                print(f"{Fore.RED}[GROQ ERROR] {e}")
                yield "Maaf, koneksi otak awan (Groq) lagi bermasalah..."

        # 2. OLLAMA HANDLER (STREAMING)
        else:
            try:
                # VRAM OPTIMIZATION FOR 8B MODEL ON 4GB GPU
                stream = ollama.chat(
                    model=self.model_id,
                    messages=messages,
                    stream=True,  # ENABLE STREAM
                    options={
                        'temperature': temperature,
                        'repeat_penalty': 1.15, 
                        'top_k': 40,
                        'top_p': 0.9,
                        'num_predict': 1024,     
                        'num_ctx': 4096,         
                        'num_thread': 8,         
                        'low_vram': True         
                    }
                )
                for chunk in stream:
                    content = chunk['message']['content']
                    if content:
                        yield content
            except Exception as e:
                print(f"{Fore.RED}[OLLAMA ERROR] {e}")
                yield "Maaf, koneksi otak lokal (Ollama) lagi bermasalah..."
