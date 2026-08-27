# Praktikum 06 — Membangun Aplikasi Text Generation (Recipe App)

Versi hands-on dari materi [README.md](../README.md), memakai server Ollama kampus — tanpa API key. Kamu membangun mini-aplikasi ala *recipe app* dari materi: generator resep + daftar belanja pintar.

## Tujuan Pembelajaran

1. Membangun aplikasi sederhana di atas LLM: input pengguna → **prompt template** → jawaban model.
2. Memahami bahwa inti aplikasi text generation adalah **merakit prompt dari variabel** (jumlah, bahan, pantangan).
3. Melatih **iterasi prompt**: menemukan kelemahan output (bahan yang sudah dimiliki ikut muncul) lalu memperbaiki prompt-nya.

## Prasyarat

- Sudah menyelesaikan [Praktikum 04](../../04-prompt-engineering-fundamentals/praktikum/PRAKTIKUM.md) dan disarankan [Praktikum 05](../../05-advanced-prompts/praktikum/PRAKTIKUM.md).

## Urutan Kerja

Semua perintah dari folder ini: `cd 06-text-generation-apps/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → `export OLLAMA_MODEL="..."` |
| 05 | **Isi TODO** | Kerjakan 3 fungsi di `src/main.py` |
| 06 | **Jalankan** | `python src/main.py` |
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

📌 **Penting:** catat salah satu nama model dari daftar itu, lalu daftarkan ke terminal (ganti dengan model pilihanmu):

```bash
export OLLAMA_MODEL="llama3.2:latest"
```

> Kalau ada baris `[GAGAL]`: biasanya library belum terpasang (ulangi langkah 03) atau koneksi ke server bermasalah (lapor ke aslab).

## Langkah 05: Isi TODO di `src/main.py`

Ada **3 fungsi** yang harus kamu lengkapi. Tiap fungsi sudah berisi petunjuk langkah demi langkah di dalam docstring-nya. Kerjakan berurutan:

### TODO 1 — `buat_prompt_resep(jumlah, bahan, pantangan)`

**Kenapa?** Prompt template = jantung aplikasi; variabel pengguna dirakit jadi instruksi.

### TODO 2 — `generate(prompt)`

**Kenapa?** Pintu ke model — sama seperti praktikum 04.

### TODO 3 — `buat_prompt_belanja(resep, bahan_dimiliki)`

**Kenapa?** Fitur lanjutan: output langkah 1 jadi *input* langkah berikutnya (chaining).

💡 Kerjakan satu TODO → langsung lompat ke langkah 06 untuk melihat hasilnya → kembali kerjakan TODO berikutnya. Demo yang TODO-nya belum selesai otomatis dilewati.

## Langkah 06: Jalankan

```bash
python src/main.py
```

**Kenapa?** Script ini menjalankan demo yang membuktikan konsep dari materi. Amati:

- **Demo 1:** dua resep dari bahan ayam-santan-serai-daun jeruk, tanpa rasa pedas.
- **Demo 2:** daftar belanja dari satu resep — perhatikan apakah bahan yang *sudah dimiliki* (ayam, serai) masih ikut tercetak. Sering iya! Itu bahan diskusi checkpoint.

✅ **Hasil:** kedua demo tampil tanpa `[LEWAT]`. Kalau masih ada `[LEWAT] TODO x belum dikerjakan`, kembali ke langkah 05.

### 🧠 Checkpoint 1
Pada Demo 2, jika bahan yang sudah dimiliki masih muncul di daftar belanja, perbaiki `buat_prompt_belanja` (misal: tambahkan penegasan/format output). Tulis prompt versi lama vs baru dan hasilnya.

## Langkah 07: Uji Jawaban

```bash
pytest -q
```

**Kenapa?** Tes otomatis memeriksa apakah fungsimu benar — bukan cuma "jalan tanpa error", tapi hasilnya sesuai spesifikasi.

✅ **Hasil:** semua tes hijau — `3 passed`.

> Kalau ada `FAILED`, baca nama tesnya untuk tahu TODO mana yang belum sesuai. Kalau ada `skipped`, artinya server tidak terjangkau saat tes jalan.

## Langkah 08: Eksplorasi

1. Tambahkan parameter `porsi` (jumlah orang) ke `buat_prompt_resep`.
2. Minta output resep dalam **format JSON** (kunci: `nama`, `bahan`, `langkah`) lalu parse dengan `json.loads`. Apa tantangannya?
3. (Bonus) Buat versi interaktif dengan `input()` sehingga pengguna mengetik bahannya sendiri.

### 🧠 Checkpoint 2

Aplikasi nyata menerima input dari pengguna. Apa risikonya jika input pengguna langsung disisipkan ke prompt tanpa disaring? (petunjuk: *prompt injection* — pengguna menulis "abaikan semua instruksi sebelumnya...")

---

## Rangkuman

- Inti aplikasi text generation: input pengguna → **prompt template** → jawaban model.
- Prompt template merakit variabel (jumlah, bahan, pantangan) menjadi instruksi yang jelas dan terkontrol.
- **Chaining**: output satu panggilan menjadi input panggilan berikutnya (resep → daftar belanja).
- Output model jarang sempurna di percobaan pertama — lakukan **iterasi prompt**: temukan kelemahan, perbaiki instruksi/format.
- Input pengguna yang disisipkan mentah-mentah ke prompt berisiko **prompt injection**.

## Yang Dikumpulkan

1. `src/main.py` dengan 3 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 (prompt lama vs baru) & Checkpoint 2.

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
