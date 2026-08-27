# Pertemuan 02 — Ngobrol yang Benar dengan AI: Responsible AI & Prompt Engineering

> Gabungan dari lesson asli: **03-using-generative-ai-responsibly**, **04-prompt-engineering-fundamentals**, dan **05-advanced-prompts**.

Minggu lalu kalian sudah kenalan dengan LLM. Sekarang kita belajar "bahasa"-nya: bagaimana menulis perintah (prompt) yang menghasilkan jawaban bagus dan konsisten, trik-trik lanjutan biar AI lebih akurat, plus kesadaran bahwa AI bisa ngarang — jadi jawabannya jangan ditelan mentah-mentah.

## Tujuan Belajar

1. Menulis prompt yang jelas: instruksi + konteks + format output yang diminta.
2. Memakai peran `system` / `user` / `assistant` dan teknik few-shot (kasih contoh).
3. Mencoba teknik lanjutan: temperature, chain-of-thought, self-consistency, self-refine.
4. Menyadari risiko halusinasi & konten berbahaya, dan membiasakan verifikasi jawaban AI.

## Konsep Inti

1. **Prompt yang baik = instruksi jelas + konteks + format output** (misal: "jawab HANYA dalam JSON").
2. **Tiga peran pesan**: `system` (kepribadian AI), `user` (kita), `assistant` (jawaban AI).
3. **Few-shot**: beri 2–3 contoh, model meniru polanya.
4. **Teknik lanjutan**: `temperature` (kreatif vs konsisten), chain-of-thought ("pikir langkah demi langkah"), self-consistency (tanya 3× lalu bandingkan), self-refine (AI mengkritik jawabannya sendiri).
5. **Responsible AI**: halusinasi itu nyata — model menebak, bukan tahu. Selalu cek fakta.

## Isi Folder Ini

| Folder/File | Isi |
|---|---|
| [MATERI.md#03-responsible-ai](./MATERI.md#03-responsible-ai) | Materi asli: memakai Generative AI secara bertanggung jawab |
| [MATERI.md#04-prompt-engineering](./MATERI.md#04-prompt-engineering) | Materi asli: dasar-dasar prompt engineering |
| [MATERI.md#05-advanced-prompts](./MATERI.md#05-advanced-prompts) | Materi asli: teknik prompt lanjutan |
| [praktikum/](./praktikum/) | **Praktikum terpadu** — Bagian A: tokenisasi, generate, chat, few-shot (TODO 1–4); Bagian B: temperature, CoT, self-consistency, self-refine (TODO 5–7) |
| src/ | Kode contoh asli lesson 04–05 (python & javascript) sebagai referensi |
| images/ | Gambar pendukung materi |

## Alur Praktik

1. Baca [praktikum/PRAKTIKUM.md](./praktikum/PRAKTIKUM.md) — setup venv, `python src/cek_env.py`, lalu kerjakan Bagian A (TODO 1–4) di `src/main.py`.
2. Lanjut Bagian B (TODO 5–7) di file yang sama → uji `pytest -q` (target `10 passed`). Kalau waktu habis, TODO 6–7 boleh dilanjutkan di rumah.
3. Diskusi: temukan satu contoh halusinasi dari model, lalu tulis prompt yang menguranginya.

## Hubungan dengan Mini Project

Prompt engineering dipakai di SEMUA pilihan mini project — system message dan few-shot adalah fondasi aplikasimu nanti.

## Tugas

Lihat aturan pengumpulan di [SUBMISSION.md](./SUBMISSION.md).
