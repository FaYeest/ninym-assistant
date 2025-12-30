import re
from colorama import Fore

class OutputParser:
    def __init__(self, profile_manager):
        self.profile = profile_manager

    def parse(self, full_reply):
        """
        Extracts Thought, Meta, and Speech from the new Line-Based format.
        Format:
        Thought: ...
        Meta: mood='...' affection='...'
        Response: ...
        """
        thought = "..."
        speech = full_reply # Default fallback
        
        # 1. Extract Thought
        # Regex looks for "Thought: (content) \n"
        thought_match = re.search(r'Thought:\s*(.*?)(?=Meta:|Response:|$)', full_reply, re.DOTALL | re.IGNORECASE)
        if thought_match:
            thought = thought_match.group(1).strip()
            
        # 2. Extract Meta (Mood & Affection)
        # Regex looks for "Meta: ... mood='x' ... affection='y' ..."
        meta_match = re.search(r'Meta:\s*(.*?)(?=Response:|$)', full_reply, re.DOTALL | re.IGNORECASE)
        if meta_match:
            meta_content = meta_match.group(1)
            
            # Parse Mood
            mood_match = re.search(r"mood=['\"](.*?)['\"]", meta_content)
            if mood_match:
                new_mood = mood_match.group(1)
                self.profile.update_mood(new_mood)
                
            # Parse Affection
            aff_match = re.search(r"affection=['\"](.*?)['\"]", meta_content)
            if aff_match:
                try:
                    aff_str = aff_match.group(1)
                    # Handle '+1' or '-1' or '1'
                    aff_val = int(aff_str.replace('+', '')) 
                    curr = self.profile.update_affection(aff_val)
                    print(f"{Fore.MAGENTA}[EMOTION] Affection: {curr} ({aff_str})")
                except: pass

        # 3. Extract Response (Speech)
        # Regex looks for "Response: (content)"
        response_match = re.search(r'Response:\s*(.*)', full_reply, re.DOTALL | re.IGNORECASE)
        if response_match:
            speech = response_match.group(1).strip()
        else:
            # Fallback cleanup if "Response:" tag is missing but Thought/Meta exists
            speech = re.sub(r'Thought:.*?(?=Meta:|Response:|$)', '', speech, flags=re.DOTALL | re.IGNORECASE)
            speech = re.sub(r'Meta:.*?(?=Response:|$)', '', speech, flags=re.DOTALL | re.IGNORECASE)
            speech = speech.replace("Response:", "").strip()
        
        return thought, speech
