# Starter Code Mini Project

Kerangka minimal untuk memulai — fungsi `generate`, `chat`, dan `embedding` sudah siap pakai.

## Cara Pakai

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OLLAMA_MODEL="llama3.2:latest"   # ganti sesuai hasil benchmark-mu di pertemuan-07
python main.py
```

Lalu kembangkan `main()` sesuai tema kelompokmu. Potongan kode praktikum pertemuan 2–7 boleh dipakai ulang — misalnya `cosine_similarity` & `potong_dokumen` (pertemuan-06) untuk tema RAG, atau `definisi_tools` & `jalankan_tool` (pertemuan-05) untuk tema asisten ber-tool.

Jangan lupa tulis README project kalian sendiri (lihat requirement di [../README.md](../README.md)).
