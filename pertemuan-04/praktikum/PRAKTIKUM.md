# Praktikum Pertemuan 04 — Aplikasi Pencarian Semantik (Embeddings)

Versi hands-on dari materi [README.md](../MATERI.md#08-search-embeddings), memakai server Ollama kampus — tanpa API key. Kamu membangun mesin pencari yang memahami **makna**, bukan sekadar mencocokkan kata.

## Tujuan Pembelajaran

1. Memahami **embedding**: representasi teks sebagai vektor angka, sehingga "makna" bisa dihitung secara matematis.
2. Menghitung **cosine similarity** (ukuran kemiripan dua vektor: 1 = identik, 0 = tak berhubungan) dari nol, tanpa library ML.
3. Membangun **pencarian semantik**: menemukan dokumen relevan meski kata kuncinya tidak sama persis.

## Prasyarat

- Sudah menyelesaikan [Praktikum Pertemuan 02](../../pertemuan-02/praktikum/PRAKTIKUM.md).
- Ingat matematika vektor dasar (dot product, panjang vektor) — dipandu di docstring.

> **Penting:** praktikum ini memakai model **embedding** (`bge-m3`), bukan model chat. Model embedding tidak "menjawab" — ia hanya mengubah teks menjadi vektor.

## Urutan Kerja

Semua perintah dari folder ini: `cd pertemuan-04/praktikum`

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

Detail tiap langkah ada di bawah. **Jangan lompat-lompat** — tiap langkah bergantung pada langkah sebelumnya.

---

## Langkah 01–02: Buat & Aktifkan Environment

**Kenapa?** *Virtual environment* (venv) mengisolasi library praktikum ini agar tidak bercampur dengan proyek lain.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

✅ **Hasil:** muncul awalan `(.venv)` di kiri prompt terminal.

## Langkah 03: Pasang Library

**Kenapa?** Kita butuh `requests` (mengirim HTTP request ke server AI) dan `pytest` (menguji jawabanmu otomatis).

```bash
pip install -r requirements.txt
```

✅ **Hasil:** baris terakhir kurang lebih `Successfully installed requests-... pytest-...` tanpa error merah.

## Langkah 04: Cek Kesiapan

**Kenapa?** Sebelum menulis kode, pastikan environment benar dan server AI kampus bisa dijangkau — supaya kalau nanti ada error, kamu tahu itu bukan masalah koneksi.

```bash
python src/cek_env.py
```

✅ **Hasil:** semua baris `[OK]`, daftar model yang tersedia, dan tulisan `SIAP!`.

📌 **Penting:** pastikan `bge-m3` muncul di daftar model — itulah model **embedding** yang dipakai praktikum ini (bukan model chat). Kalau ingin memakai model embedding lain, daftarkan lewat:

```bash
export OLLAMA_EMBED_MODEL="bge-m3:latest"
```

> Kalau ada baris `[GAGAL]`: biasanya library belum terpasang (ulangi langkah 03) atau koneksi ke server bermasalah (lapor ke aslab).

## Langkah 05: Isi TODO di `src/main.py`

Ada **3 fungsi** yang harus kamu lengkapi. Tiap fungsi sudah berisi petunjuk langkah demi langkah di dalam docstring-nya. Kerjakan berurutan:

### TODO 1 — `embedding(teks)`

**Kenapa?** Pintu ke model embedding via `/api/embeddings` — teks masuk, vektor keluar.

### TODO 2 — `cosine_similarity(a, b)`

**Kenapa?** Inti matematika pencarian semantik; kamu tulis sendiri agar paham, bukan pakai numpy.

### TODO 3 — `cari(query, dokumen, k)`

**Kenapa?** Merangkai 1+2 jadi mesin pencari: embed semua → skor → urutkan.

💡 Kerjakan satu TODO → langsung lompat ke langkah 06 untuk melihat hasilnya → kembali kerjakan TODO berikutnya. Demo yang TODO-nya belum selesai otomatis dilewati.

## Langkah 06: Jalankan

```bash
python src/main.py
```

**Kenapa?** Script ini menjalankan demo yang membuktikan konsep dari materi. Amati:

- **Demo 1:** satu kalimat menjadi vektor ratusan/ribuan dimensi.
- **Demo 2:** "kucing duduk di sofa" vs "seekor kucing bersantai di kursi" berskor **tinggi** (semakna, kata beda); vs "harga saham naik" berskor **rendah**.
- **Demo 3:** query "bagaimana cara membuat chatbot?" → dokumen Pertemuan 07 harus peringkat 1, padahal tidak ada kata "membuat" atau "bagaimana" di dokumennya.

✅ **Hasil:** ketiga demo tampil tanpa `[LEWAT]`. Kalau masih ada `[LEWAT] TODO x belum dikerjakan`, kembali ke langkah 05.

### 🧠 Checkpoint 1
Mengapa pencarian kata kunci biasa (mis. `if "chatbot" in dokumen`) gagal untuk query "cara bikin bot ngobrol", sedangkan pencarian semantik tetap berhasil?

## Langkah 07: Uji Jawaban

```bash
pytest -q
```

**Kenapa?** Tes otomatis memeriksa apakah fungsimu benar — bukan cuma "jalan tanpa error", tapi hasilnya sesuai spesifikasi.

✅ **Hasil:** semua tes hijau — `5 passed`.

> Kalau ada `FAILED`, baca nama tesnya untuk tahu TODO mana yang belum sesuai. Kalau ada `skipped`, artinya server tidak terjangkau saat tes jalan.

## Langkah 08: Eksplorasi

1. Tambahkan 4 dokumen baru bertema bebas ke `DOKUMEN`, lalu uji 3 query berbeda.
2. Ubah `cari` agar meng-embed dokumen **sekali saja** (simpan di list/dict), bukan setiap query. Ukur bedanya dengan `time.perf_counter()`.
3. (Bonus) Bandingkan hasil `bge-m3` dengan `nomic-embed-text` (ganti `OLLAMA_EMBED_MODEL`) — mana lebih baik untuk bahasa Indonesia?

### 🧠 Checkpoint 2

Demo 3 meng-embed SEMUA dokumen setiap kali mencari. Apa masalahnya jika dokumennya 1 juta? Apa solusinya? (petunjuk: simpan vektor sekali di awal → itulah *vector database*, dibahas di praktikum 15)

---

## Rangkuman

- **Embedding** mengubah teks menjadi vektor angka sehingga "makna" bisa dihitung secara matematis.
- **Cosine similarity** mengukur kemiripan dua vektor: 1 = identik, 0 = tak berhubungan.
- **Pencarian semantik** menemukan dokumen relevan meski kata kuncinya tidak sama persis — kelemahan utama pencarian kata kunci biasa.
- Meng-embed semua dokumen di setiap query tidak skalabel — simpan vektor sekali di awal; itulah esensi *vector database*.

## Yang Dikumpulkan

1. `src/main.py` dengan 3 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Hasil eksplorasi no. 2 (kode + perbandingan waktu).

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
