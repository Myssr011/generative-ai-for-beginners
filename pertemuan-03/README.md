# Pertemuan 03 — Bikin Aplikasi AI Pertamamu: Text Generation & Chat App

> Gabungan dari lesson asli: **06-text-generation-apps** dan **07-building-chat-applications**.

Hari ini kalian naik level: dari "sekadar memanggil AI" menjadi membangun aplikasi utuh. Pertama, generator resep yang prompt-nya dirakit dari input user. Kedua — yang paling penting — chatbot yang nyambung diajak ngobrol karena "mengingat" percakapan sebelumnya.

## Tujuan Belajar

1. Membangun aplikasi text generation: template prompt + input user + panggil model + olah jawaban.
2. Memahami rahasia chatbot: model **tidak punya memori** — seluruh riwayat dikirim ulang tiap giliran.
3. Mengelola riwayat percakapan sebagai struktur data (list of dict role/content).
4. Menangani keterbatasan context window dengan memangkas riwayat tanpa membuang system message.

## Konsep Inti

1. **Aplikasi AI = template prompt + panggilan API + pengolahan jawaban** — bukan sihir.
2. **Prompt dirakit dari input user** memakai f-string (jumlah resep, bahan, pantangan…).
3. **Chatbot tidak mengingat apa pun** — "ingatan" = riwayat yang kita kirim ulang.
4. **Struktur riwayat**: `[{"role": "system", ...}, {"role": "user", ...}, {"role": "assistant", ...}]`.
5. **Context window terbatas** → pangkas riwayat, tapi pertahankan pesan system.

## Isi Folder Ini

| Folder/File | Isi |
|---|---|
| [MATERI.md#06-text-generation-apps](./MATERI.md#06-text-generation-apps) | Materi asli: membangun aplikasi text generation |
| [MATERI.md#07-chat-applications](./MATERI.md#07-chat-applications) | Materi asli: membangun aplikasi chat ber-AI |
| [praktikum/](./praktikum/) | **Praktikum terpadu** — Bagian A: recipe app (TODO 1–3); Bagian B: chatbot ber-memori (TODO 4–6) |
| src/ | Kode contoh asli lesson 06–07 (python, typescript, dotnet, js-githubmodels) |
| images/ | Gambar pendukung materi |

## Alur Praktik

1. Baca [praktikum/PRAKTIKUM.md](./praktikum/PRAKTIKUM.md) — Bagian A: kerjakan `buat_prompt_resep`, `generate`, `buat_prompt_belanja` (TODO 1–3).
2. Bagian B: kerjakan `chat`, `tambah_pesan`, `potong_riwayat` (TODO 4–6) → uji `pytest -q`, target **8 passed**.
3. Eksperimen bebas: ganti domain resep jadi domain lain (rencana olahraga, itinerary liburan, dsb.).

## Hubungan dengan Mini Project

Kerangka chatbot ber-memori dari pertemuan ini adalah tulang punggung hampir semua pilihan mini project di pertemuan-08.

## Tugas

Lihat aturan pengumpulan di [SUBMISSION.md](./SUBMISSION.md).
