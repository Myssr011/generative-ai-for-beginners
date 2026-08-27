# Pertemuan 04 — AI yang Paham Makna (Embeddings) + AI Pembuat Gambar

> Gabungan dari lesson asli: **08-building-search-applications** dan **09-building-image-applications**.

Komputer ternyata bisa "mengukur kemiripan makna" dua kalimat — caranya dengan mengubah teks jadi deretan angka (vektor). Hari ini kalian membangun mesin pencari yang paham maksud, bukan sekadar mencocokkan kata. Sebagai bonus wawasan: cara kerja AI pembuat gambar.

## Tujuan Belajar

1. Menjelaskan apa itu embedding dan kenapa "makna mirip = angka berdekatan".
2. Menghitung kemiripan dua teks dengan cosine similarity.
3. Membangun mesin pencari semantik sederhana (top-k dokumen paling relevan).
4. Memahami konsep AI pembuat gambar (prompt → gambar) beserta isu keamanannya.

## Konsep Inti

1. **Embedding = teks → vektor** (ratusan angka float); makna mirip → vektor berdekatan.
2. **Model embedding ≠ model chat** — kita pakai `bge-m3` (bagus untuk bahasa Indonesia).
3. **Cosine similarity**: dot(a,b) / (|a|·|b|) — hasil 1.0 = identik, 0.0 = tak berhubungan.
4. **Semantic search vs keyword search**: "mobil impian" ≠ mimpi tentang mobil.
5. **Image generation**: prompt → gambar lewat proses diffusion; perhatikan keamanan konten & hak cipta.

## Isi Folder Ini

| Folder/File | Isi |
|---|---|
| [MATERI.md#08-search-embeddings](./MATERI.md#08-search-embeddings) | Materi asli: membangun aplikasi pencarian dengan embeddings |
| [MATERI.md#09-image-generation](./MATERI.md#09-image-generation) | Materi asli: membangun aplikasi penghasil gambar |
| [praktikum/](./praktikum/) | **Praktikum inti**: embedding, cosine similarity, mesin pencari semantik (TODO 1–3) |
| src/08-search/ | Kode contoh asli lesson 08 + `embedding_index_3m.json` (indeks transkrip video) |
| src/09-image-gen/ | Kode contoh asli lesson 09 (butuh API model gambar berbayar — demo saja) |
| images/ | Gambar pendukung materi |

## Alur Praktik

1. [praktikum/PRAKTIKUM.md](./praktikum/PRAKTIKUM.md): kerjakan `embedding`, `cosine_similarity`, `cari` → `pytest -q`.
2. Uji pencarian dengan pertanyaanmu sendiri — perhatikan skor kemiripannya.
3. Image generation (lesson 09) **tidak ada praktikum** karena butuh API berbayar — cukup ikuti demo dan bedah kode di `src/09-image-gen/`.

## Hubungan dengan Mini Project

`embedding` + `cosine_similarity` + `cari` adalah separuh mesin RAG di pertemuan-06 — dan bahan utama tema mini project "Tanya Dokumen".

## Tugas

Lihat aturan pengumpulan di [SUBMISSION.md](./SUBMISSION.md).
