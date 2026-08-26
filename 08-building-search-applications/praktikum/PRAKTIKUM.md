# Praktikum 08 — Aplikasi Pencarian Semantik (Embeddings)

Versi hands-on dari materi [README.md](../README.md), memakai server Ollama kampus — tanpa API key. Kamu membangun mesin pencari yang memahami **makna**, bukan sekadar mencocokkan kata.

## Tujuan Pembelajaran

1. Memahami **embedding**: representasi teks sebagai vektor angka, sehingga "makna" bisa dihitung secara matematis.
2. Menghitung **cosine similarity** (ukuran kemiripan dua vektor: 1 = identik, 0 = tak berhubungan) dari nol, tanpa library ML.
3. Membangun **pencarian semantik**: menemukan dokumen relevan meski kata kuncinya tidak sama persis.

## Prasyarat

- Sudah menyelesaikan [Praktikum 04](../../04-prompt-engineering-fundamentals/praktikum/PRAKTIKUM.md).
- Ingat matematika vektor dasar (dot product, panjang vektor) — dipandu di docstring.

> **Penting:** praktikum ini memakai model **embedding** (`bge-m3`), bukan model chat. Model embedding tidak "menjawab" — ia hanya mengubah teks menjadi vektor.

## Urutan Kerja

Semua perintah dari folder ini: `cd 08-building-search-applications/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → pastikan `bge-m3` ada di daftar model |
| 05 | **Isi TODO** | Kerjakan 3 fungsi di `src/main.py` |
| 06 | **Jalankan** | `python src/main.py` |
| 07 | **Uji jawaban** | `pytest -q` (target: `5 passed`) |
| 08 | **Eksplorasi** | Tantangan di bagian bawah |

## Isi TODO (Langkah 05)

| TODO | Fungsi | Kenapa? |
|------|--------|---------|
| 1 | `embedding(teks)` | Pintu ke model embedding via `/api/embeddings` — teks masuk, vektor keluar |
| 2 | `cosine_similarity(a, b)` | Inti matematika pencarian semantik; kamu tulis sendiri agar paham, bukan pakai numpy |
| 3 | `cari(query, dokumen, k)` | Merangkai 1+2 jadi mesin pencari: embed semua → skor → urutkan |

## Yang Diamati di Langkah 06

- **Demo 1:** satu kalimat menjadi vektor ratusan/ribuan dimensi.
- **Demo 2:** "kucing duduk di sofa" vs "seekor kucing bersantai di kursi" berskor **tinggi** (semakna, kata beda); vs "harga saham naik" berskor **rendah**.
- **Demo 3:** query "bagaimana cara membuat chatbot?" → dokumen Pertemuan 07 harus peringkat 1, padahal tidak ada kata "membuat" atau "bagaimana" di dokumennya.

✅ **Validasi:** ketiga demo tampil tanpa `[LEWAT]`, `pytest -q` → `5 passed`.

### 🧠 Checkpoint 1
Mengapa pencarian kata kunci biasa (mis. `if "chatbot" in dokumen`) gagal untuk query "cara bikin bot ngobrol", sedangkan pencarian semantik tetap berhasil?

### 🧠 Checkpoint 2
Demo 3 meng-embed SEMUA dokumen setiap kali mencari. Apa masalahnya jika dokumennya 1 juta? Apa solusinya? (petunjuk: simpan vektor sekali di awal → itulah *vector database*, dibahas di praktikum 15)

## Langkah 08 — Eksplorasi

1. Tambahkan 4 dokumen baru bertema bebas ke `DOKUMEN`, lalu uji 3 query berbeda.
2. Ubah `cari` agar meng-embed dokumen **sekali saja** (simpan di list/dict), bukan setiap query. Ukur bedanya dengan `time.perf_counter()`.
3. (Bonus) Bandingkan hasil `bge-m3` dengan `nomic-embed-text` (ganti `OLLAMA_EMBED_MODEL`) — mana lebih baik untuk bahasa Indonesia?

## Yang Dikumpulkan

1. `src/main.py` dengan 3 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Hasil eksplorasi no. 2 (kode + perbandingan waktu).

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
