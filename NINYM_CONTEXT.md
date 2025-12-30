# 📔 Project Ninym: Context & Status

## Hardware
- **Device:** MSI GF63 11sc Laptop
- **CPU:** Intel i5-11400H
- **GPU:** NVIDIA GTX 1650 (4GB VRAM)
- **RAM:** 16GB

## Current Software Architecture
1.  **Orchestrator:** `modules/brain/` (Modular package)
2.  **LLM:** Transitioning to **Ollama** (Local) for uncensored responses.
3.  **Search:** Manual Deep Search via `ddgs` (SafeSearch OFF, Scraper enabled).
4.  **RAG:** ChromaDB based local knowledge (Supports TXT, PDF, DOCX, MD, C++, PY, JS).
5.  **Personality:** "Ninym" - Indonesian Waifu Style (Cheeky, Smart, Emotional).
6.  **Memory:** `core/memory.json` (Chat History) & `core/user_profile.json` (Affection/Mood/Facts).

## Key Features Implemented
- **Emotional Engine:** Track Mood & Affection.
- **Deep Research:** Scrapes content from 3-5 top URLs for accurate data.
- **Inner Monologue:** Hidden `<thought>` tags for reasoning.
- **Security:** Sandwich Defense for prompt injection.

## Next Steps for Future Sessions
- Finish Ollama installation (`ollama run qwen2.5:3b`).
- Update `modules/brain/llm_client.py` to target Ollama localhost.
- Proceed to Phase 3 (The Voice).
