# Praktikum 11 — Function Calling (Tool Use)

Versi hands-on dari materi [README.md](../README.md), memakai server Ollama kampus — tanpa API key. Kamu memberi model "tangan" untuk mengakses data yang tidak ia ketahui: jadwal praktikum kampus.

## Tujuan Pembelajaran

1. Memahami **function calling**: model tidak menjalankan kode — ia *meminta* fungsi dipanggil, kode kitalah yang mengeksekusi.
2. Menulis **definisi tool** (skema JSON berisi nama, deskripsi, dan parameter fungsi) yang bisa dipahami model.
3. Merangkai alur lengkap: pertanyaan → model minta tool → eksekusi lokal → hasil dikirim balik → jawaban akhir.

## Prasyarat

- Sudah menyelesaikan [Praktikum 07](../../07-building-chat-applications/praktikum/PRAKTIKUM.md) (paham `/api/chat` dan struktur messages).
- Gunakan model yang mendukung tools: `llama3.2:latest` atau `qwen2.5:7b-instruct`.

## Urutan Kerja

Semua perintah dari folder ini: `cd 11-integrating-with-function-calling/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → `export OLLAMA_MODEL="llama3.2:latest"` |
| 05 | **Isi TODO** | Kerjakan 3 fungsi di `src/main.py` |
| 06 | **Jalankan** | `python src/main.py` |
| 07 | **Uji jawaban** | `pytest -q` (target: `5 passed`) |
| 08 | **Eksplorasi** | Tantangan di bagian bawah |

## Isi TODO (Langkah 05)

| TODO | Fungsi | Kenapa? |
|------|--------|---------|
| 1 | `definisi_tools()` | Skema inilah "iklan" kemampuan tool ke model — deskripsi yang jelas menentukan kapan model memakainya |
| 2 | `jalankan_tool(nama, argumen)` | Dispatcher: menerjemahkan permintaan model menjadi eksekusi kode nyata (akses dict `JADWAL`) |
| 3 | `chat_dengan_tools(messages)` | Sama seperti `/api/chat` biasa + parameter `tools`; kembalikan message utuh karena bisa berisi `tool_calls` |

## Yang Diamati di Langkah 06

- **Demo 1:** tiga tahap tercetak: (1) model meminta `get_jadwal_praktikum({'hari': 'rabu'})`, (2) kode kita mengeksekusi dan mendapat "Praktikum Kecerdasan Buatan...", (3) model merangkai jawaban akhir dari hasil itu.
- **Demo 2:** pertanyaan sama tanpa tools → model mengarang atau mengaku tidak tahu.

> Catatan: kadang model kecil memilih menjawab langsung tanpa memanggil tool — jalankan ulang atau perjelas deskripsi tool.

✅ **Validasi:** `pytest -q` → `5 passed`.

### 🧠 Checkpoint 1
Siapa yang sebenarnya mengeksekusi fungsi — model atau kode kita? Mengapa desain ini lebih **aman** daripada model mengeksekusi kode sendiri?

### 🧠 Checkpoint 2
Deskripsi di `definisi_tools` memengaruhi perilaku model. Ubah deskripsinya jadi menyesatkan (misal "dapatkan resep masakan") — apakah model masih memanggil tool untuk pertanyaan jadwal? Catat hasilnya.

## Langkah 08 — Eksplorasi

1. Tambahkan tool kedua `get_dosen_pengampu(matakuliah)` dengan dict data sendiri; uji pertanyaan yang butuh **kedua** tool sekaligus.
2. Uji pertanyaan yang TIDAK butuh tool ("apa itu rekursi?") — apakah model tetap memaksakan memanggil tool?
3. (Bonus) Ganti model ke `qwen2.5:7b-instruct` dan bandingkan keandalan pemanggilan tool-nya.

## Yang Dikumpulkan

1. `src/main.py` dengan 3 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Kode + hasil Eksplorasi no. 1 (tool kedua).

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
