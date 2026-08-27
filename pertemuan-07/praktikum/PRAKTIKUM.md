# Praktikum Pertemuan 07 — Small Language Models (SLM): Kecil vs Besar

Versi hands-on dari materi [README.md](../MATERI.md#19-slm), memakai server Ollama kampus — tanpa API key. Kamu mengadu **SLM 135 juta parameter** (`smollm2:135m`) melawan model 3 miliar (`llama3.2`) dan 27 miliar (`gemma3:27b`) untuk merasakan sendiri trade-off ukuran model.

## Tujuan Pembelajaran

1. Memahami apa itu **SLM** (Small Language Model): model berparameter jauh lebih sedikit — lebih cepat, murah, bisa jalan di perangkat kecil, tapi kemampuan nalarnya terbatas.
2. Mengukur **latency** (waktu respons) beberapa model secara empiris.
3. Menilai kapan SLM cukup, dan kapan butuh model besar (trade-off kecepatan vs kualitas).

## Prasyarat

- Sudah menyelesaikan [Praktikum Pertemuan 02](../../pertemuan-02/praktikum/PRAKTIKUM.md).

## Urutan Kerja

Semua perintah dari folder ini: `cd pertemuan-07/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → pastikan `smollm2:135m`, `llama3.2`, `gemma3:27b` ada |
| 05 | **Isi TODO** | Kerjakan 2 fungsi di `src/main.py` |
| 06 | **Jalankan** | `python src/main.py` (Demo 2 bisa lama — model 27B lambat!) |
| 07 | **Uji jawaban** | `pytest -q` (target: `3 passed`) |
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

📌 **Penting:** pastikan ketiga model yang diadu — `smollm2:135m`, `llama3.2`, dan `gemma3:27b` — ada di daftar model. Tidak perlu `export OLLAMA_MODEL`; daftar model diatur lewat `MODEL_UJI` di `src/main.py`.

> Kalau ada baris `[GAGAL]`: biasanya library belum terpasang (ulangi langkah 03) atau koneksi ke server bermasalah (lapor ke aslab).

## Langkah 05: Isi TODO di `src/main.py`

Ada **2 fungsi** yang harus kamu lengkapi. Tiap fungsi sudah berisi petunjuk langkah demi langkah di dalam docstring-nya. Kerjakan berurutan:

### TODO 1 — `generate_model(model, prompt)`

**Kenapa?** Seperti `generate` biasa tapi model bisa dipilih + waktu diukur `time.perf_counter()`.

### TODO 2 — `bandingkan(daftar_model, prompt, fn)`

**Kenapa?** Benchmark mini: kumpulkan hasil semua model, urutkan dari tercepat. Parameter `fn` memungkinkan diuji tanpa server.

💡 Kerjakan satu TODO → langsung lompat ke langkah 06 untuk melihat hasilnya → kembali kerjakan TODO berikutnya. Demo yang TODO-nya belum selesai otomatis dilewati.

## Langkah 06: Jalankan

```bash
python src/main.py
```

**Kenapa?** Script ini menjalankan demo yang membuktikan konsep dari materi (Demo 2 bisa lama — model 27B lambat!). Amati:

- **Demo 1 (soal mudah):** semua model menjawab "Jakarta" — tapi `smollm2:135m` (200× lebih kecil!) tercepat. Untuk tugas sederhana, SLM = pilihan hemat.
- **Demo 2 (soal jebakan "semua kecuali 9 mati"):** jawaban benar **9**. Amati model mana yang terjebak menjawab 8 (17−9) dan mana yang bernalar benar — biasanya makin besar makin andal.

✅ **Hasil:** kedua demo tampil tanpa `[LEWAT]`. Kalau masih ada `[LEWAT] TODO x belum dikerjakan`, kembali ke langkah 05.

### 🧠 Checkpoint 1
Dari Demo 1: berapa kali lipat `smollm2` lebih cepat dari `gemma3:27b`? Sebutkan 2 kasus penggunaan nyata di mana kecepatan itu lebih penting daripada kecerdasan maksimal.

## Langkah 07: Uji Jawaban

```bash
pytest -q
```

**Kenapa?** Tes otomatis memeriksa apakah fungsimu benar — bukan cuma "jalan tanpa error", tapi hasilnya sesuai spesifikasi.

✅ **Hasil:** semua tes hijau — `3 passed`.

> Kalau ada `FAILED`, baca nama tesnya untuk tahu TODO mana yang belum sesuai. Kalau ada `skipped`, artinya server tidak terjangkau saat tes jalan.

## Langkah 08: Eksplorasi

1. Tambahkan `qwen2.5:7b-instruct` ke `MODEL_UJI` (4 model) dan jalankan ulang — di mana posisinya di spektrum kecepatan/kualitas?
2. Buat 3 soal ujianmu sendiri (mudah/sedang/jebakan) dan catat model terkecil yang masih menjawab benar untuk tiap soal.
3. (Bonus) Ukur juga **panjang jawaban** (jumlah karakter) tiap model — apakah model besar cenderung lebih "cerewet"?

### 🧠 Checkpoint 2

Dari Demo 2: model mana saja yang menjawab benar (9)? Jika aplikasimu adalah (a) autocomplete keyboard HP dan (b) asisten diagnosa awal puskesmas — model ukuran apa yang kamu pilih untuk masing-masing, dan mengapa?

---

## Rangkuman

- **SLM** = model berparameter jauh lebih sedikit: lebih cepat, murah, bisa jalan di perangkat kecil — tapi nalarnya terbatas.
- Untuk tugas sederhana, SLM sering cukup dan jauh lebih hemat; soal bernalar/jebakan lebih andal di model besar.
- **Latency** bisa (dan sebaiknya) diukur secara empiris, bukan diasumsikan.
- Pilih ukuran model berdasarkan kebutuhan aplikasi: trade-off kecepatan/biaya vs kualitas jawaban.

## Yang Dikumpulkan

1. `src/main.py` dengan 2 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Tabel hasil Eksplorasi no. 2 (soal × model × benar/salah).

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
