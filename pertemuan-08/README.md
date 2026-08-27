# Pertemuan 08 — MINI PROJECT

Inilah puncaknya! Kalian membuat **satu aplikasi AI kecil yang jalan beneran** di server Ollama kampus (tanpa API key), dengan menggabungkan **minimal 2 konsep** dari pertemuan 1–7. Tujuannya bukan aplikasi yang wah, tapi membuktikan kalian paham cara merakit blok-blok yang sudah dilatih: prompt → aplikasi → memori → embeddings → tools → RAG.

## Pilihan Tema (pilih satu, boleh dimodifikasi)

| Tema | Konsep yang digabung | Gambaran |
|---|---|---|
| **1. "Tanya Dokumen" — Chatbot + RAG** | P3 (chat + memori) + P6 (RAG) + P4 (embeddings) | Chatbot yang menjawab HANYA dari dokumen pilihanmu (panduan akademik, aturan lab, materi kuliah). Mulai dari praktikum 15, ganti dokumennya, tambah loop percakapan. |
| **2. Asisten Ber-Tool — Chat + Function Calling** | P3 (chat + memori) + P5 (tools) | Asisten dengan minimal 2 tool nyata: cek jadwal, hitung IPK, info ruangan, konversi nilai — data dari dict/CSV buatanmu. |
| **3. Generator Belajar Pintar — Prompt Engineering + Text App** | P2 (few-shot/CoT/self-refine) + P3 (app) + opsional P4 | Aplikasi pembuat soal kuis/flashcard dari topik input user; pakai few-shot biar format konsisten, self-refine biar hasil makin bagus. |

## Requirement Minimum (fitur wajib)

1. Jalan end-to-end di server Ollama kampus, dari cek koneksi sampai output.
2. Minimal **2 konsep** dari pertemuan 1–7, disebut eksplisit di README project.
3. Punya **system prompt / template prompt yang dirancang sendiri** (bukan asal tanya).
4. Ada **interaksi berulang** (loop input user) ATAU **output terstruktur** (JSON/format tetap).
5. **README project**: cara setup (venv → install → `export OLLAMA_MODEL`), cara menjalankan, 1 contoh output.
6. Kode dipecah jadi **fungsi-fungsi** (tiru pola praktikum), bukan satu blob panjang.

## Cara Mulai

1. Salin folder [starter-code/](./starter-code/) sebagai kerangka project kelompokmu.
2. Fungsi dasar (`generate`, `chat`, `embedding`) sudah disediakan — fokus ke logika aplikasimu.
3. Ambil bebas potongan kode dari praktikum pertemuan 2–7 yang sudah kalian kerjakan.

## Timeline

- **Opsi A — dikerjakan di kelas (2–3 jam):** kelompok 2–3 orang. Menit 0–15 briefing & pilih tema → 15–30 desain fungsi di kertas → 30–120 koding (asisten keliling) → 120–150 demo kilat 5 menit/kelompok.
- **Opsi B — take-home (1–2 minggu):** briefing di akhir pertemuan-07, kerja individu/berpasangan, pertemuan-08 full untuk demo + tanya jawab 5–7 menit/kelompok. Item bonus di checklist jadi ekspektasi.

> Opsi yang dipakai akan diumumkan asisten/dosen di kelas.

## Penilaian

Lihat checklist lengkap di [SUBMISSION.md](./SUBMISSION.md).
