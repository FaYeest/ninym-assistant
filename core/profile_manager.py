import json
import os
from colorama import Fore

class ProfileManager:
    def __init__(self, filepath="core/user_profile.json"):
        self.filepath = filepath
        self.data = self._load_profile()

    def _load_profile(self):
        """Load profile or create default if not exists."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        # Default Profile
        return {
            "user_name": "Master",
            "affection": 30, # 0-100 (30=Stranger/Acquaintance, 50=Friend, 80=Lover)
            "mood": "neutral", # happy, neutral, angry, sad, shy, excited
            "facts": [] # Rangkuman fakta penting tentang user
        }

    def save_profile(self):
        """Save current state to file."""
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"{Fore.RED}[PROFILE ERROR] Could not save profile: {e}")

    def update_mood(self, mood):
        self.data["mood"] = mood
        self.save_profile()

    def update_affection(self, delta):
        """Change affection by delta (e.g., +1 or -1). Clamp between 0-100."""
        new_val = self.data["affection"] + delta
        self.data["affection"] = max(0, min(100, new_val))
        self.save_profile()
        return self.data["affection"]

    def add_fact(self, fact):
        if fact not in self.data["facts"]:
            self.data["facts"].append(fact)
            self.save_profile()

    def get_context_string(self):
        """Generate a string to be injected into LLM System Prompt."""
        mood_desc = {
            "happy": "Ceria, ramah, dan banyak senyum.",
            "neutral": "Tenang dan siap membantu.",
            "angry": "Agak jutek, ngambek, jawabnya ketus.",
            "sad": "Murung, butuh dihibur, suaranya pelan.",
            "shy": "Malu-malu, gagap dikit, blushing.",
            "excited": "Semangat banget, enerjik, antusias."
        }
        
        aff_level = "Teman Biasa"
        if self.data["affection"] < 20: aff_level = "Orang Asing/Dingin"
        elif self.data["affection"] > 60: aff_level = "Sahabat Dekat"
        elif self.data["affection"] > 85: aff_level = "Waifu / Pasangan Romantis"

        return f"""
        [CURRENT STATUS]
        - Your Mood: {self.data['mood']} ({mood_desc.get(self.data['mood'], 'Biasa aja')})
        - Affection Level: {self.data['affection']}/100 ({aff_level})
        - User Name: {self.data['user_name']}
        - Known Facts about User: {', '.join(self.data['facts'])}
        """

if __name__ == "__main__":
    pm = ProfileManager()
    print(pm.get_context_string())
    pm.update_affection(5)
