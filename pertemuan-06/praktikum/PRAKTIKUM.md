# Praktikum Pertemuan 06 — RAG (Retrieval Augmented Generation) & Basis Data Vektor

Versi hands-on dari materi [README.md](../MATERI.md#15-rag-vector-db), memakai server Ollama kampus — tanpa API key. Kamu membuat AI yang bisa menjawab pertanyaan tentang **aturan lab kampus sendiri** — data yang mustahil diketahui model.

## Tujuan Pembelajaran

1. Memahami keterbatasan LLM: hanya tahu data latihnya — tidak tahu dokumen privat/terbaru.
2. Membangun pipeline **RAG** lengkap: *chunking* (memecah dokumen) → *embedding* → *retrieval* (mengambil potongan relevan) → *augmented prompt* (menyuntikkan konteks ke prompt).
3. Membuktikan RAG mengurangi *fabrication*: jawaban terikat pada dokumen sumber.

## Prasyarat

- Sudah menyelesaikan [Praktikum Pertemuan 04](../../pertemuan-04/praktikum/PRAKTIKUM.md) (embedding & cosine similarity — dipakai lagi di sini).

## Urutan Kerja

Semua perintah dari folder ini: `cd pertemuan-06/praktikum`

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

📌 **Penting:** daftarkan model chat yang akan dipakai (praktikum ini juga memakai model embedding `bge-m3` secara otomatis):

```bash
export OLLAMA_MODEL="llama3.2:latest"
```

> Kalau ada baris `[GAGAL]`: biasanya library belum terpasang (ulangi langkah 03) atau koneksi ke server bermasalah (lapor ke aslab).

## Langkah 05: Isi TODO di `src/main.py`

Ada **4 fungsi** yang harus kamu lengkapi. Tiap fungsi sudah berisi petunjuk langkah demi langkah di dalam docstring-nya. Kerjakan berurutan:

### TODO 1 — `potong_dokumen(teks)`

**Kenapa?** Dokumen utuh terlalu panjang untuk context window — dipecah per paragraf agar bisa dipilih yang relevan saja.

### TODO 2 — `embedding(teks)`

**Kenapa?** Tiap potongan diubah jadi vektor agar kemiripannya dengan pertanyaan bisa dihitung.

### TODO 3 — `ambil_konteks(query, potongan, k)`

**Kenapa?** Inti *retrieval*: pilih k potongan paling relevan — inilah tugas *vector database* di dunia nyata.

### TODO 4 — `buat_prompt_rag(query, konteks)`

**Kenapa?** Inti *augmentation*: konteks + aturan "jawab hanya dari konteks" mencegah model mengarang.

Fungsi `generate` dan `cosine_similarity` **sudah disediakan** (sudah kamu kuasai di praktikum pertemuan 02 & 04).

💡 Kerjakan satu TODO → langsung lompat ke langkah 06 untuk melihat hasilnya → kembali kerjakan TODO berikutnya. Demo yang TODO-nya belum selesai otomatis dilewati.

## Langkah 06: Jalankan

```bash
python src/main.py
```

**Kenapa?** Script ini menjalankan demo yang membuktikan konsep dari materi.

Dokumen sumber: [data/materi.txt](./data/materi.txt) — panduan lab fiktif berisi fakta spesifik (jam buka, nama kepala lab, sanksi, bobot nilai). Amati:

- **Demo 1:** dokumen terpecah menjadi ±9 potongan paragraf.
- **Demo 2 (tanpa RAG):** ditanya jam buka lab Sabtu + nama kepala lab → model menebak/mengaku tidak tahu.
- **Demo 3 (dengan RAG):** retrieval mengambil paragraf jam operasional & kepala lab → jawaban model: **Sabtu 08.00–12.00, Ibu Nurhayati** — cocok dengan dokumen!

✅ **Hasil:** ketiga demo tampil tanpa `[LEWAT]`. Kalau masih ada `[LEWAT] TODO x belum dikerjakan`, kembali ke langkah 05.

### 🧠 Checkpoint 1
Bandingkan jawaban Demo 2 vs Demo 3 untuk pertanyaan yang sama persis. Komponen mana dari pipeline (chunking/retrieval/augmented prompt) yang menurutmu paling berperan? Jelaskan.

## Langkah 07: Uji Jawaban

```bash
pytest -q
```

**Kenapa?** Tes otomatis memeriksa apakah fungsimu benar — bukan cuma "jalan tanpa error", tapi hasilnya sesuai spesifikasi.

✅ **Hasil:** semua tes hijau — `5 passed`.

> Kalau ada `FAILED`, baca nama tesnya untuk tahu TODO mana yang belum sesuai. Kalau ada `skipped`, artinya server tidak terjangkau saat tes jalan.

## Langkah 08: Eksplorasi

1. Ganti `data/materi.txt` dengan dokumen milikmu (misal silabus mata kuliah) dan uji 3 pertanyaan.
2. Demo 3 meng-embed semua potongan setiap kali bertanya. Ubah agar embedding potongan dihitung **sekali** di awal lalu disimpan (list of (vektor, teks)) — inilah esensi *vector database*.
3. (Bonus) Naikkan `k` dari 2 ke 5 — apakah jawaban membaik atau justru "tenggelam" oleh konteks tidak relevan?

### 🧠 Checkpoint 2

Instruksi "jika tidak ada di konteks, katakan tidak tahu" di `buat_prompt_rag` itu penting. Uji: tanyakan sesuatu yang TIDAK ada di dokumen (misal "berapa biaya praktikum?"). Apa jawabannya? Apa yang terjadi kalau instruksi itu dihapus?

---

## Rangkuman

- LLM hanya tahu data latihnya — dokumen privat/terbaru mustahil ia ketahui tanpa bantuan.
- Pipeline **RAG**: *chunking* (pecah dokumen) → *embedding* → *retrieval* (ambil potongan relevan) → *augmented prompt* (suntikkan konteks).
- Aturan "jawab hanya dari konteks; kalau tidak ada, katakan tidak tahu" mengikat jawaban ke dokumen sumber dan mengurangi *fabrication*.
- Menghitung embedding potongan sekali di awal lalu menyimpannya = esensi *vector database*.

## Yang Dikumpulkan

1. `src/main.py` dengan 4 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Hasil Eksplorasi no. 1 (dokumen sendiri + 3 tanya-jawab).

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
