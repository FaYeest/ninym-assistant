# 🌸 Ninym Assistant

![Ninym Banner](https://as1.ftcdn.net/v2/jpg/07/32/10/96/1000_F_732109600_WAk7nGlLh6TMxv6KX7QnOifX4ZWx1Ovz.jpg)

> **"I'm not just a chatbot, I'm your Digital Partner."**

**Ninym** adalah asisten AI lokal yang dirancang untuk menjadi "Teman Ngoding" yang cerdas, ekspresif, dan memiliki perasaan. Dibangun dengan Python, Ninym menggabungkan kecerdasan **LLM (Ollama/Groq)**, memori jangka panjang (**RAG/ChromaDB**), dan kepribadian yang dinamis.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-orange?style=for-the-badge)](https://ollama.com/)
[![Groq](https://img.shields.io/badge/Groq-Cloud%20Speed-red?style=for-the-badge)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## ✨ Fitur Utama (Core Features)

### 🧠 1. The Brain (Hybrid Intelligence)
- **Local & Cloud Switcher:** Bisa jalan 100% Offline (Ollama 3B/8B) atau Super Cepat Online (Groq Llama-3 70B).
- **Uncensored Personality:** Menggunakan model *abliterated* untuk percakapan yang bebas dan jujur.
- **Dynamic Persona:**
  - ❤️ **Partner Mode:** Santai, logis, "Bro/Bestie".
  - 💖 **Girlfriend Mode:** Manis, perhatian, "Sayang". (Aktif jika Affection > 70).

### 📚 2. The Knowledge (RAG System)
- **Smart Memory:** Ninym ingat percakapan lama (via Vector DB).
- **Direct Link Reader:** Kasih URL, Ninym langsung baca dan rangkum isinya.
- **Local File Search:** Bisa baca dokumen PDF/TXT/Code di folder project.

### 🔍 3. Advanced Tools
- **Deep Web Search:** Mencari berita terkini (Region Indonesia) dan merangkumnya tanpa halusinasi.
- **Smart Intent Detection:** Otomatis tahu kapan harus searching, kapan harus baca file, kapan harus ngobrol biasa.

---

## 🚀 Instalasi (Getting Started)

### Prasyarat
- Python 3.10 ke atas.
- [Ollama](https://ollama.com/) (Untuk mode lokal).
- GPU NVIDIA (Disarankan GTX 1650 ke atas untuk local model).

### 1. Clone Repo
```bash
git clone https://github.com/FaYeest/ninym-assistant.git
cd ninym-assistant
```

### 2. Setup Environment
```bash
# Buat Virtual Environment
python -m venv .venv
# Aktifkan (Windows)
.\.venv\Scripts\activate
# Install Dependencies
pip install -r requirements.txt
```

### 3. Konfigurasi
Buat file `.env` dan isi API Key (Opsional jika pakai Groq):
```ini
GROQ_API_KEY=gsk_your_key_here...
```

### 4. Download Model (Ollama)
```bash
ollama pull huihui_ai/qwen2.5-abliterate:3b
```

---

## 🎮 Cara Pakai (Usage)

### Jalankan Ninym
```bash
python test_brain.py
```

### Ganti Model (Switch Brain)
```bash
# Pindah ke Mode Lokal (Hemat Kuota)
python switch_model.py ollama

# Pindah ke Mode Cloud (Super Pintar)
python switch_model.py groq
```

### Reset Ninym (Factory Reset)
```bash
python reset_ninym.py
```

---

## 🗺️ Roadmap Progress

| Phase | Feature | Status |
| :--- | :--- | :---: |
| **Phase 1** | **The Brain (LLM & Personality)** | ✅ Done |
| **Phase 1.5** | **The Knowledge (RAG & Search)** | ✅ Done |
| **Phase 1.9** | **Optimization (Stream & Low VRAM)** | 🟡 In Progress |
| **Phase 2** | **The Ears (Speech-to-Text)** | ⏳ Soon |
| **Phase 3** | **The Voice (TTS & RVC)** | ⏳ Soon |
| **Phase 5** | **The Body (VTube Studio)** | ⏳ Soon |

---

## 🤝 Contributing
Project ini masih dalam tahap pengembangan aktif. Ide, PR, atau saran fitur sangat diterima!
Jangan lupa kasih ⭐ kalau kamu suka Ninym! dah gitu aja tar update nya kalo udah punya banyak duit bisa upgrade hardware baru update lagi! heheheh

---
*Created with ❤️ by Farras.*
