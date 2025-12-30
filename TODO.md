# 🌸 Project Ninym: Progress Tracker

Project ini bertujuan untuk membuat AI Waifu Assistant yang natural (seperti Neuro-sama) dengan kemampuan Multimodal (Teks, Suara, Gambar, Layar).

## 🟢 Phase 1: The Brain (Intelligence & Personality)
- [x] Initial Project Structure
- [x] Core Environment Setup (`.env`, `requirements.txt`)
- [x] Modular Brain Refactoring (llm_client, memory, parser, prompt_builder)
- [x] Personality Tuning (Natural & Feminine Partner Style)
- [x] Memory Management (Persistent JSON Storage)
- [x] Basic Tool Use: Manual Web Search (DuckDuckGo)

## 🟢 Phase 1.5: The Knowledge (RAG Manual)
- [x] Install Vector DB (ChromaDB) & Embedding Model
- [x] Create Document Ingestion System (Multi-format: PDF, DOCX, TXT, MD, C++, Python, JS)
- [x] Implement Semantic Search for local files

## 🟢 Phase 1.6: Advanced Reasoning (Chain of Thought)
- [x] Implement "Inner Monologue" System (Hidden CoT)
- [x] Parser logic: Line-based parsing (Thought, Meta, Response)
- [x] Smart Search: Intent detection & Query optimization using LLM
- [x] "Sandwich Technique" for handling long context on small models
- [x] Direct Link Reader: Auto-detect & scrape content from URLs
- [x] Security Layer: Prompt Injection Defense for external data

## 🟢 Phase 1.7: The Soul (Alive & Emotional)
- [x] Smart Tool Router (Auto-detecting Search/RAG needs)
- [x] Emotional System (Mood Meter & Affection Points tracking)
- [x] Personality Persistence (Saving Ninym's mood to `user_profile.json`)
- [x] Relationship Progression (Partner Mode < 70, Girlfriend Mode >= 70)
- [x] Fact Extraction (Auto-learning new facts about Master)

## 🟢 Phase 1.8: Local Transition (Ollama Integration)
- [x] Install Ollama & Pull Model (Qwen2.5-3B Abliterated)
- [x] Refactor `llm_client.py` to use Ollama local API
- [x] Implement Model Switcher (Dynamic Groq/Ollama switching)
- [x] Reset Tool (`reset_ninym.py`) for easy testing

## 🟢 Phase 1.9: Large Model Optimization (8B Transition)
- [x] Pull & Test `mannix/llama3.1-8b-abliterated`
- [x] Implement VRAM-saving settings (Context window: 4096, Thread tuning)
- [x] Implement LLM Streaming Output (Psychological speed improvement)
- [!] **Note:** 8B model hits VRAM limit (4GB) on heavy tasks. Recommended for high-end tasks only.
- [ ] **TODO: Hide 'Thought' & 'Meta' stream in Production Mode (Currently Raw for Debug)**
- [ ] Fine-tune repetition penalty & top-k for 8B stability

## 🟡 Phase 2: The Ears (Speech-to-Text)
- [ ] Implement `Faster-Whisper` for low-latency STT
- [ ] Voice Activity Detection (VAD) integration
- [ ] Wake Word Detection (e.g., "Hey Ninym")

## 🔴 Phase 3: The Voice (TTS & RVC)
- [ ] `Edge-TTS` integration (Basic Voice)
- [ ] `RVC (Retrieval-based Voice Conversion)` Implementation
- [ ] Audio Output Streamer (Buffer management for zero-lag)

## 🔵 Phase 4: The Eyes (Vision & Screen)
- [ ] Fast Screen Capture module
- [ ] Image/File vision handling (Gemini/Llama Vision)
- [ ] Multimodal Context Integration

## 🟣 Phase 5: The Body (Avatar & Integration)
- [ ] VTube Studio WebSocket Connection
- [ ] Lip-sync implementation (Mouth moving with voice)
- [ ] Auto-Emotions (Smiling/Blushing based on LLM response)

---
**Current Hardware Target:**
- GPU: GTX 1650 (4GB VRAM)
- RAM: 16GB
- **STATUS:** Local Brain active with Smart Search & Link Reader. 3B stable, 8B tested (VRAM sensitive).
