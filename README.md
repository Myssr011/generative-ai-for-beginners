# Praktikum Generative AI — 8 Pertemuan

Kurikulum praktikum Generative AI untuk mahasiswa, hasil restrukturisasi dari [Generative AI for Beginners (Microsoft)](https://github.com/microsoft/generative-ai-for-beginners) — 22 lesson asli dipadatkan menjadi **8 pertemuan tatap muka**, dengan pertemuan terakhir berupa **mini project**.

Semua praktikum berjalan di **server Ollama kampus** (`https://ollama.if.unismuh.ac.id`) — **tanpa API key, tanpa biaya**.

## Daftar Pertemuan

| # | Pertemuan | Lesson Asal | Praktikum |
|---|---|---|---|
| 1 | [Kenalan GenAI & Siapkan Lingkungan](./pertemuan-01/README.md) | 00, 01, 02 | Setup venv + koneksi server |
| 2 | [Responsible AI & Prompt Engineering](./pertemuan-02/README.md) | 03, 04, 05 | Tokenisasi, generate, chat, few-shot, CoT |
| 3 | [Text Generation & Chat App](./pertemuan-03/README.md) | 06, 07 | Recipe app + chatbot ber-memori |
| 4 | [Embeddings & Image Generation](./pertemuan-04/README.md) | 08, 09 | Mesin pencari semantik |
| 5 | [Function Calling, Low-Code & UX](./pertemuan-05/README.md) | 10, 11, 12 | AI ber-tool (jadwal praktikum) |
| 6 | [RAG, Keamanan & Lifecycle](./pertemuan-06/README.md) | 13, 14, 15 | RAG atas dokumen sendiri |
| 7 | [Model Terbuka, Agent & Wawasan Lanjutan](./pertemuan-07/README.md) | 16, 17, 18–21 | Benchmark SLM vs LLM |
| 8 | [**MINI PROJECT**](./pertemuan-08/README.md) | — | Aplikasi gabungan ≥2 konsep |

## Struktur Tiap Folder Pertemuan

```
pertemuan-XX/
├── README.md        ← ringkasan materi berbahasa Indonesia (mulai dari sini!)
├── SUBMISSION.md    ← aturan pengumpulan tugas
├── MATERI.md        ← materi bacaan asli gabungan (referensi lengkap, bahasa Inggris)
├── images/          ← gambar pendukung materi
├── praktikum/       ← latihan berkode dengan TODO + pytest (inti pertemuan)
└── src/             ← kode contoh asli lesson terkait (python/ts/dotnet)
```

## Cara Mulai (Mahasiswa)

1. Clone repo ini, lalu buka folder pertemuan yang sedang berjalan.
2. Baca `README.md` pertemuan itu, lanjut ke `praktikum/*/PRAKTIKUM.md`.
3. Ikuti urutan kerja di PRAKTIKUM.md:

   ```bash
   cd pertemuan-02/praktikum
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   python src/cek_env.py                 # cek koneksi server AI kampus
   export OLLAMA_MODEL="llama3.2:latest" # pilih model dari daftar
   # kerjakan TODO di src/main.py, lalu:
   python src/main.py
   pytest -q                             # uji jawabanmu
   ```

4. Kumpulkan tugas sesuai `SUBMISSION.md` pertemuan tersebut.

## Folder Lain

| Folder | Isi |
|---|---|
| [arsip-lesson-asli/](./arsip-lesson-asli/) | 22 folder lesson asli (00–21), README upstream, dan DAFTAR-VIDEO |
| [pendukung/](./pendukung/) | Dokumen komunitas upstream, presentasi, skrip utilitas, tes |

## Kredit & Lisensi

Diadaptasi dari [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) (lisensi MIT — lihat [LICENSE](./LICENSE)). Materi asli tiap lesson tersimpan utuh di `MATERI.md` tiap pertemuan dan di `arsip-lesson-asli/`.
