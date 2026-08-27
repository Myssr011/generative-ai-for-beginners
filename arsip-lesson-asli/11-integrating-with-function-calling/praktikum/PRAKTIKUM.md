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

📌 **Penting:** praktikum ini butuh model yang **mendukung tools** — pakai `llama3.2:latest` atau `qwen2.5:7b-instruct`:

```bash
export OLLAMA_MODEL="llama3.2:latest"
```

> Kalau ada baris `[GAGAL]`: biasanya library belum terpasang (ulangi langkah 03) atau koneksi ke server bermasalah (lapor ke aslab).

## Langkah 05: Isi TODO di `src/main.py`

Ada **3 fungsi** yang harus kamu lengkapi. Tiap fungsi sudah berisi petunjuk langkah demi langkah di dalam docstring-nya. Kerjakan berurutan:

### TODO 1 — `definisi_tools()`

**Kenapa?** Skema inilah "iklan" kemampuan tool ke model — deskripsi yang jelas menentukan kapan model memakainya.

### TODO 2 — `jalankan_tool(nama, argumen)`

**Kenapa?** Dispatcher: menerjemahkan permintaan model menjadi eksekusi kode nyata (akses dict `JADWAL`).

### TODO 3 — `chat_dengan_tools(messages)`

**Kenapa?** Sama seperti `/api/chat` biasa + parameter `tools`; kembalikan message utuh karena bisa berisi `tool_calls`.

💡 Kerjakan satu TODO → langsung lompat ke langkah 06 untuk melihat hasilnya → kembali kerjakan TODO berikutnya. Demo yang TODO-nya belum selesai otomatis dilewati.

## Langkah 06: Jalankan

```bash
python src/main.py
```

**Kenapa?** Script ini menjalankan demo yang membuktikan konsep dari materi. Amati:

- **Demo 1:** tiga tahap tercetak: (1) model meminta `get_jadwal_praktikum({'hari': 'rabu'})`, (2) kode kita mengeksekusi dan mendapat "Praktikum Kecerdasan Buatan...", (3) model merangkai jawaban akhir dari hasil itu.
- **Demo 2:** pertanyaan sama tanpa tools → model mengarang atau mengaku tidak tahu.

> Catatan: kadang model kecil memilih menjawab langsung tanpa memanggil tool — jalankan ulang atau perjelas deskripsi tool.

✅ **Hasil:** kedua demo tampil tanpa `[LEWAT]`. Kalau masih ada `[LEWAT] TODO x belum dikerjakan`, kembali ke langkah 05.

### 🧠 Checkpoint 1
Siapa yang sebenarnya mengeksekusi fungsi — model atau kode kita? Mengapa desain ini lebih **aman** daripada model mengeksekusi kode sendiri?

## Langkah 07: Uji Jawaban

```bash
pytest -q
```

**Kenapa?** Tes otomatis memeriksa apakah fungsimu benar — bukan cuma "jalan tanpa error", tapi hasilnya sesuai spesifikasi.

✅ **Hasil:** semua tes hijau — `5 passed`.

> Kalau ada `FAILED`, baca nama tesnya untuk tahu TODO mana yang belum sesuai. Kalau ada `skipped`, artinya server tidak terjangkau saat tes jalan.

## Langkah 08: Eksplorasi

1. Tambahkan tool kedua `get_dosen_pengampu(matakuliah)` dengan dict data sendiri; uji pertanyaan yang butuh **kedua** tool sekaligus.
2. Uji pertanyaan yang TIDAK butuh tool ("apa itu rekursi?") — apakah model tetap memaksakan memanggil tool?
3. (Bonus) Ganti model ke `qwen2.5:7b-instruct` dan bandingkan keandalan pemanggilan tool-nya.

### 🧠 Checkpoint 2

Deskripsi di `definisi_tools` memengaruhi perilaku model. Ubah deskripsinya jadi menyesatkan (misal "dapatkan resep masakan") — apakah model masih memanggil tool untuk pertanyaan jadwal? Catat hasilnya.

---

## Rangkuman

- **Function calling**: model tidak mengeksekusi kode — ia *meminta* fungsi dipanggil; kode kitalah yang mengeksekusi. Desain ini lebih aman.
- **Definisi tool** (skema JSON: nama, deskripsi, parameter) adalah "iklan" kemampuan ke model — kualitas deskripsi menentukan kapan tool dipakai.
- Alur lengkap: pertanyaan → model minta tool → eksekusi lokal → hasil dikirim balik → jawaban akhir.
- Tanpa tools, model mengarang atau mengaku tidak tahu untuk data yang tidak ia ketahui.
- Model kecil kadang tidak konsisten memanggil tool — deskripsi yang jelas dan pemilihan model berpengaruh.

## Yang Dikumpulkan

1. `src/main.py` dengan 3 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Kode + hasil Eksplorasi no. 1 (tool kedua).

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
