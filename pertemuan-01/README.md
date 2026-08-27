# Pertemuan 01 — Kenalan dengan Generative AI & Siapkan Lingkungan Kerja

> Gabungan dari lesson asli: **00-course-setup**, **01-introduction-to-genai**, dan **02-exploring-and-comparing-different-llms**.

Selamat datang di pertemuan pertama! Hari ini kita kenalan dulu: apa sih Generative AI itu, kenapa dia bisa "ngobrol" dengan kita, dan model AI itu macamnya apa saja. Setelah itu kita siapkan komputer kalian supaya siap dipakai praktik sampai akhir semester.

## Tujuan Belajar

Setelah pertemuan ini, kalian bisa:

1. Menjelaskan dengan bahasa sendiri apa itu Generative AI dan LLM (Large Language Model).
2. Memahami cara kerja dasar LLM: mesin penebak "kata berikutnya" yang dilatih dari teks raksasa.
3. Menyebutkan jenis-jenis model AI dan kapan memakainya (teks, gambar, embedding; besar vs kecil; tertutup vs terbuka).
4. Menyiapkan lingkungan kerja Python (virtual environment) dan tersambung ke server AI kampus.

## Konsep Inti

1. **Generative AI = AI yang membuat konten baru** (teks, gambar, kode) — bukan sekadar mengenali/mengklasifikasi.
2. **LLM bekerja dengan menebak token berikutnya.** Itulah kenapa jawabannya kadang meyakinkan tapi salah — dia menebak, bukan "tahu".
3. **Token & tokenisasi**: model membaca teks sebagai potongan-potongan kata. Jumlah token menentukan biaya dan batas "ingatan" model.
4. **Tidak ada satu model untuk semua**: ada model teks, gambar, audio, embedding; ada model raksasa dan mungil; ada yang tertutup (GPT) dan terbuka (Llama, Mistral, Phi — yang kita pakai di kampus lewat Ollama).
5. **Dua cara mengakses model**: sewa layanan cloud (perlu API key, berbayar) atau jalankan sendiri lewat Ollama — di praktikum kita pakai **server Ollama kampus, tanpa API key**.

## Isi Folder Ini

| Folder/File | Isi |
|---|---|
| [MATERI.md#01-intro-genai](./MATERI.md#01-intro-genai) | Materi (bahasa Indonesia): pengenalan Generative AI & LLM |
| [MATERI.md#02-exploring-llms](./MATERI.md#02-exploring-llms) | Materi (bahasa Indonesia): menjelajah & membandingkan berbagai LLM |
| [images/](./images/) | Semua gambar pendukung materi |

> Catatan: panduan setup (venv, koneksi server) tidak lagi berupa materi terpisah — langsung ikuti bagian **Alur Praktik** di bawah. Versi Inggris lengkap materi asli tetap tersedia di [arsip-lesson-asli](../arsip-lesson-asli/).

## Alur Praktik Hari Ini

1. **Pasang Python 3.9+** dan editor (VS Code disarankan).
2. **Buat virtual environment**: `python3 -m venv .venv` lalu `source .venv/bin/activate`.
3. **Tes koneksi ke server AI kampus** (`https://ollama.if.unismuh.ac.id`) — daftar model bisa dicek lewat endpoint `/api/tags`.
4. **Eksperimen kecil tokenisasi**: hitung token kalimat Indonesia vs Inggris — mana yang lebih "boros"? (Latihan berkode penuh dimulai di **pertemuan-02**.)

## Hubungan dengan Mini Project

Lingkungan yang kalian siapkan hari ini dipakai terus sampai mini project di pertemuan-08. Paham token juga membantu kalian mengerti kenapa chatbot bisa "lupa" percakapan panjang nanti.

## Tugas

Lihat aturan pengumpulan di [SUBMISSION.md](./SUBMISSION.md).
