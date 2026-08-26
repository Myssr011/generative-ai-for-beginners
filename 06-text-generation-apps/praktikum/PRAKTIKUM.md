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

## Isi TODO (Langkah 05)

| TODO | Fungsi | Kenapa? |
|------|--------|---------|
| 1 | `buat_prompt_resep(jumlah, bahan, pantangan)` | Prompt template = jantung aplikasi; variabel pengguna dirakit jadi instruksi |
| 2 | `generate(prompt)` | Pintu ke model — sama seperti praktikum 04 |
| 3 | `buat_prompt_belanja(resep, bahan_dimiliki)` | Fitur lanjutan: output langkah 1 jadi *input* langkah berikutnya (chaining) |

## Yang Diamati di Langkah 06

- **Demo 1:** dua resep dari bahan ayam-santan-serai-daun jeruk, tanpa rasa pedas.
- **Demo 2:** daftar belanja dari satu resep — perhatikan apakah bahan yang *sudah dimiliki* (ayam, serai) masih ikut tercetak. Sering iya! Itu bahan diskusi checkpoint.

✅ **Validasi:** kedua demo tampil tanpa `[LEWAT]`, `pytest -q` → `3 passed`.

### 🧠 Checkpoint 1
Pada Demo 2, jika bahan yang sudah dimiliki masih muncul di daftar belanja, perbaiki `buat_prompt_belanja` (misal: tambahkan penegasan/format output). Tulis prompt versi lama vs baru dan hasilnya.

### 🧠 Checkpoint 2
Aplikasi nyata menerima input dari pengguna. Apa risikonya jika input pengguna langsung disisipkan ke prompt tanpa disaring? (petunjuk: *prompt injection* — pengguna menulis "abaikan semua instruksi sebelumnya...")

## Langkah 08 — Eksplorasi

1. Tambahkan parameter `porsi` (jumlah orang) ke `buat_prompt_resep`.
2. Minta output resep dalam **format JSON** (kunci: `nama`, `bahan`, `langkah`) lalu parse dengan `json.loads`. Apa tantangannya?
3. (Bonus) Buat versi interaktif dengan `input()` sehingga pengguna mengetik bahannya sendiri.

## Yang Dikumpulkan

1. `src/main.py` dengan 3 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 (prompt lama vs baru) & Checkpoint 2.

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
