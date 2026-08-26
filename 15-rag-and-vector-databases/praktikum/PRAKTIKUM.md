# Praktikum 15 — RAG (Retrieval Augmented Generation) & Basis Data Vektor

Versi hands-on dari materi [README.md](../README.md), memakai server Ollama kampus — tanpa API key. Kamu membuat AI yang bisa menjawab pertanyaan tentang **aturan lab kampus sendiri** — data yang mustahil diketahui model.

## Tujuan Pembelajaran

1. Memahami keterbatasan LLM: hanya tahu data latihnya — tidak tahu dokumen privat/terbaru.
2. Membangun pipeline **RAG** lengkap: *chunking* (memecah dokumen) → *embedding* → *retrieval* (mengambil potongan relevan) → *augmented prompt* (menyuntikkan konteks ke prompt).
3. Membuktikan RAG mengurangi *fabrication*: jawaban terikat pada dokumen sumber.

## Prasyarat

- Sudah menyelesaikan [Praktikum 08](../../08-building-search-applications/praktikum/PRAKTIKUM.md) (embedding & cosine similarity — dipakai lagi di sini).

## Urutan Kerja

Semua perintah dari folder ini: `cd 15-rag-and-vector-databases/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → `export OLLAMA_MODEL="llama3.2:latest"` |
| 05 | **Isi TODO** | Kerjakan 4 fungsi di `src/main.py` |
| 06 | **Jalankan** | `python src/main.py` |
| 07 | **Uji jawaban** | `pytest -q` (target: `5 passed`) |
| 08 | **Eksplorasi** | Tantangan di bagian bawah |

## Isi TODO (Langkah 05)

| TODO | Fungsi | Kenapa? |
|------|--------|---------|
| 1 | `potong_dokumen(teks)` | Dokumen utuh terlalu panjang untuk context window — dipecah per paragraf agar bisa dipilih yang relevan saja |
| 2 | `embedding(teks)` | Tiap potongan diubah jadi vektor agar kemiripannya dengan pertanyaan bisa dihitung |
| 3 | `ambil_konteks(query, potongan, k)` | Inti *retrieval*: pilih k potongan paling relevan — inilah tugas *vector database* di dunia nyata |
| 4 | `buat_prompt_rag(query, konteks)` | Inti *augmentation*: konteks + aturan "jawab hanya dari konteks" mencegah model mengarang |

Fungsi `generate` dan `cosine_similarity` **sudah disediakan** (sudah kamu kuasai di praktikum 04 & 08).

## Yang Diamati di Langkah 06

Dokumen sumber: [data/materi.txt](./data/materi.txt) — panduan lab fiktif berisi fakta spesifik (jam buka, nama kepala lab, sanksi, bobot nilai).

- **Demo 1:** dokumen terpecah menjadi ±9 potongan paragraf.
- **Demo 2 (tanpa RAG):** ditanya jam buka lab Sabtu + nama kepala lab → model menebak/mengaku tidak tahu.
- **Demo 3 (dengan RAG):** retrieval mengambil paragraf jam operasional & kepala lab → jawaban model: **Sabtu 08.00–12.00, Ibu Nurhayati** — cocok dengan dokumen!

✅ **Validasi:** ketiga demo tampil tanpa `[LEWAT]`, `pytest -q` → `5 passed`.

### 🧠 Checkpoint 1
Bandingkan jawaban Demo 2 vs Demo 3 untuk pertanyaan yang sama persis. Komponen mana dari pipeline (chunking/retrieval/augmented prompt) yang menurutmu paling berperan? Jelaskan.

### 🧠 Checkpoint 2
Instruksi "jika tidak ada di konteks, katakan tidak tahu" di `buat_prompt_rag` itu penting. Uji: tanyakan sesuatu yang TIDAK ada di dokumen (misal "berapa biaya praktikum?"). Apa jawabannya? Apa yang terjadi kalau instruksi itu dihapus?

## Langkah 08 — Eksplorasi

1. Ganti `data/materi.txt` dengan dokumen milikmu (misal silabus mata kuliah) dan uji 3 pertanyaan.
2. Demo 3 meng-embed semua potongan setiap kali bertanya. Ubah agar embedding potongan dihitung **sekali** di awal lalu disimpan (list of (vektor, teks)) — inilah esensi *vector database*.
3. (Bonus) Naikkan `k` dari 2 ke 5 — apakah jawaban membaik atau justru "tenggelam" oleh konteks tidak relevan?

## Yang Dikumpulkan

1. `src/main.py` dengan 4 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Hasil Eksplorasi no. 1 (dokumen sendiri + 3 tanya-jawab).

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
