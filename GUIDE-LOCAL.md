# 🏠 Panduan Migrasi ke Otak Lokal (Ollama)

Panduan ini akan membantumu menjalankan "Brain" Ninym secara lokal di laptopmu (GTX 1650) agar **Bebas Sensor** dan **Privasi Terjamin**.

## 1. Download & Install Ollama
Ollama adalah software ringan untuk menjalankan model AI (LLM) di komputer pribadi.

1.  Download dari situs resmi: [**ollama.com/download**](https://ollama.com/download)
2.  Install seperti biasa (Next > Next > Finish).
3.  Setelah selesai, buka Terminal (PowerShell/CMD) dan ketik:
    ```bash
    ollama --version
    ```
    (Jika muncul versi, berarti sukses).

## 2. Pilih & Download Model "Unfiltered"
Karena VRAM kamu 4GB, kita cari model yang ukurannya di bawah 3GB agar sisa VRAM bisa dipakai untuk rendering layar/game.

### Pilihan A: Llama 3.2 3B (Sangat Cepat & Pintar, tapi Semi-Censored)
Ini model resmi Meta terbaru yang dibuat khusus untuk laptop. Sangat ngebut!
```bash
ollama run llama3.2
```

### Pilihan B: Dolphin Llama 3 (8B tapi dikompres, Uncensored) - AGAK BERAT
Dolphin terkenal "nurut" dan tidak mau disensor. Tapi ukurannya 4.7GB (mungkin agak berat di 4GB VRAM).
```bash
ollama run dolphin-llama3
```

### Pilihan C: Qwen 2.5 3B (Keseimbangan Terbaik) - **REKOMENDASI**
Qwen 2.5 versi 3B performanya sering mengalahkan Llama 3 8B di benchmark. Versi ini cukup "longgar" sensornya dibanding Llama.
```bash
ollama run qwen2.5:3b
```

**Saran:** Jalankan perintah **Pilihan C** di terminalmu sekarang. Biarkan dia download (~2GB).

## 3. Integrasi ke Ninym
Setelah model terdownload dan bisa dijalankan di terminal, kita perlu mengubah kode `modules/brain/llm_client.py`.

### Install Library Python
Kita butuh library `ollama` untuk python (atau pakai `langchain`, tapi library `ollama` resmi lebih ringan).

```bash
.\.venv\Scripts\pip install ollama
```

### Update Kode (Nanti saya lakukan otomatis)
Kita akan ubah `LLMClient` agar tidak lagi memanggil Groq, melainkan memanggil `ollama.chat()`.

```python
import ollama

response = ollama.chat(model='qwen2.5:3b', messages=[...])
```

## 4. Jalankan Ninym
Setelah kode diupdate, kamu tinggal jalankan seperti biasa:
```bash
python -m modules.brain
```
Bedanya, sekarang internet mati pun Ninym tetap bisa mikir! (Kecuali pas searching).
