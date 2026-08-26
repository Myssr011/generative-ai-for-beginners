# Praktikum 19 — Small Language Models (SLM): Kecil vs Besar

Versi hands-on dari materi [README.md](../README.md), memakai server Ollama kampus — tanpa API key. Kamu mengadu **SLM 135 juta parameter** (`smollm2:135m`) melawan model 3 miliar (`llama3.2`) dan 27 miliar (`gemma3:27b`) untuk merasakan sendiri trade-off ukuran model.

## Tujuan Pembelajaran

1. Memahami apa itu **SLM** (Small Language Model): model berparameter jauh lebih sedikit — lebih cepat, murah, bisa jalan di perangkat kecil, tapi kemampuan nalarnya terbatas.
2. Mengukur **latency** (waktu respons) beberapa model secara empiris.
3. Menilai kapan SLM cukup, dan kapan butuh model besar (trade-off kecepatan vs kualitas).

## Prasyarat

- Sudah menyelesaikan [Praktikum 04](../../04-prompt-engineering-fundamentals/praktikum/PRAKTIKUM.md).

## Urutan Kerja

Semua perintah dari folder ini: `cd 19-slm/praktikum`

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

## Isi TODO (Langkah 05)

| TODO | Fungsi | Kenapa? |
|------|--------|---------|
| 1 | `generate_model(model, prompt)` | Seperti `generate` biasa tapi model bisa dipilih + waktu diukur `time.perf_counter()` |
| 2 | `bandingkan(daftar_model, prompt, fn)` | Benchmark mini: kumpulkan hasil semua model, urutkan dari tercepat. Parameter `fn` memungkinkan diuji tanpa server |

## Yang Diamati di Langkah 06

- **Demo 1 (soal mudah):** semua model menjawab "Jakarta" — tapi `smollm2:135m` (200× lebih kecil!) tercepat. Untuk tugas sederhana, SLM = pilihan hemat.
- **Demo 2 (soal jebakan "semua kecuali 9 mati"):** jawaban benar **9**. Amati model mana yang terjebak menjawab 8 (17−9) dan mana yang bernalar benar — biasanya makin besar makin andal.

✅ **Validasi:** kedua demo tampil tanpa `[LEWAT]`, `pytest -q` → `3 passed`.

### 🧠 Checkpoint 1
Dari Demo 1: berapa kali lipat `smollm2` lebih cepat dari `gemma3:27b`? Sebutkan 2 kasus penggunaan nyata di mana kecepatan itu lebih penting daripada kecerdasan maksimal.

### 🧠 Checkpoint 2
Dari Demo 2: model mana saja yang menjawab benar (9)? Jika aplikasimu adalah (a) autocomplete keyboard HP dan (b) asisten diagnosa awal puskesmas — model ukuran apa yang kamu pilih untuk masing-masing, dan mengapa?

## Langkah 08 — Eksplorasi

1. Tambahkan `qwen2.5:7b-instruct` ke `MODEL_UJI` (4 model) dan jalankan ulang — di mana posisinya di spektrum kecepatan/kualitas?
2. Buat 3 soal ujianmu sendiri (mudah/sedang/jebakan) dan catat model terkecil yang masih menjawab benar untuk tiap soal.
3. (Bonus) Ukur juga **panjang jawaban** (jumlah karakter) tiap model — apakah model besar cenderung lebih "cerewet"?

## Yang Dikumpulkan

1. `src/main.py` dengan 2 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Tabel hasil Eksplorasi no. 2 (soal × model × benar/salah).

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
