import json
import os

class MemoryManager:
    def __init__(self, memory_file="core/memory.json"):
        # Ensure path is absolute relative to project root
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.filepath = os.path.join(base_dir, memory_file)
        self.history = []

    def load_history(self, initial_system_prompt):
        """Loads history from JSON and injects fresh system prompt."""
        # Fresh start template
        self.history = [
            {"role": "system", "content": initial_system_prompt},
            {"role": "assistant", "content": "<thought>Init modular brain.</thought><meta mood='neutral' affection='0' />Siap Master! Sistem Modular Ninym online! 🧠"}
        ]

        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Append old conversation (skipping old system prompt at index 0/1)
                    # We start from index 2 usually to skip init messages
                    if len(data) > 2:
                        for item in data[2:]:
                            # Convert format if needed
                            role = item.get('role')
                            if role == 'model': role = 'assistant' # Gemini comp
                            
                            content = item.get('content') or item.get('text', '')
                            self.history.append({"role": role, "content": content})
            except Exception as e:
                print(f"[MEMORY LOAD ERROR] {e}")
        
        return self.history

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def update_last_user_message(self, clean_content):
        """Updates the last user message (usually to remove heavy context injections)."""
        if self.history and self.history[-1]["role"] == "user":
            self.history[-1]["content"] = clean_content

    def save_history(self):
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            print(f"[MEMORY SAVE ERROR] {e}")
