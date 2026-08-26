# Praktikum 05 — Teknik Prompt Lanjutan (Advanced Prompts)

Versi hands-on dari materi [README.md](../README.md). Dikerjakan di **GitHub Codespaces** dengan server Ollama kampus (`https://ollama.if.unismuh.ac.id`) — tanpa API key.

## Tujuan Pembelajaran

1. Menerapkan **chain-of-thought (CoT)**: menyuruh model berpikir langkah demi langkah agar jawaban soal bernalar lebih akurat.
2. Memahami efek **temperature** (pengatur "kreativitas"/keacakan output: rendah = konsisten, tinggi = variatif).
3. Menerapkan **self-consistency**: menanyakan soal yang sama berulang kali lalu mengambil jawaban mayoritas.
4. Menerapkan **self-refine**: meminta model mengkritik dan memperbaiki jawabannya sendiri.

## Prasyarat

- Sudah menyelesaikan [Praktikum 04](../../04-prompt-engineering-fundamentals/praktikum/PRAKTIKUM.md) (konsep prompt, token, `/api/generate`).
- Paham dasar Python.

## Urutan Kerja

Semua perintah dijalankan dari folder ini: `cd 05-advanced-prompts/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → catat model, `export OLLAMA_MODEL="..."` |
| 05 | **Isi TODO** | Kerjakan 4 fungsi di `src/main.py` |
| 06 | **Jalankan** | `python src/main.py` |
| 07 | **Uji jawaban** | `pytest -q` (target: `5 passed`) |
| 08 | **Eksplorasi** | Tantangan di bagian bawah |

## Isi TODO (Langkah 05)

| TODO | Fungsi | Kenapa? |
|------|--------|---------|
| 1 | `generate(prompt, temperature)` | Seperti praktikum 04, tapi kini bisa mengatur `options.temperature` — kunci demo keacakan |
| 2 | `prompt_cot(soal)` | CoT hanyalah *teknik menyusun prompt* — instruksi "berpikir langkah demi langkah" memicu penalaran |
| 3 | `self_consistency(soal, n)` | Karena jawaban model stokastik, bertanya n× lalu voting mengurangi jawaban ngawur |
| 4 | `prompt_refine(jawaban, instruksi)` | Model bisa jadi "reviewer" untuk outputnya sendiri — dua panggilan lebih baik dari satu |

## Yang Diamati di Langkah 06

- **Demo 1:** bandingkan jawaban langsung vs jawaban ber-CoT untuk soal cerita komputer lab (jawaban benar: **12**). Mana yang benar?
- **Demo 2:** temperature 0.0 dijalankan 2× (jawaban mirip/identik) vs 1.0 dijalankan 2× (jawaban berbeda-beda).
- **Demo 3:** 3 jawaban self-consistency — apakah mayoritas menjawab 12?
- **Demo 4:** paragraf versi 1 vs versi hasil self-refine — apa yang membaik?

✅ **Validasi:** kelima demo tampil tanpa `[LEWAT]`, lalu `pytest -q` → `5 passed`.

### 🧠 Checkpoint 1
1. Pada Demo 1, mengapa instruksi "berpikir langkah demi langkah" bisa mengubah akurasi jawaban, padahal modelnya sama?
2. Kapan kamu justru *tidak* ingin temperature tinggi? Beri 1 contoh aplikasi nyata.

### 🧠 Checkpoint 2
Self-consistency memanggil model n kali → n kali lebih lambat dan mahal. Dalam kondisi apa trade-off ini layak? Dalam kondisi apa tidak?

## Langkah 08 — Eksplorasi

1. Ubah `SOAL` di `main.py` menjadi soal cerita buatanmu yang lebih menjebak. Apakah CoT masih menang?
2. Coba `self_consistency` dengan `n=5` dan `temperature=0.5` — apakah hasil voting lebih stabil?
3. (Bonus) Terapkan **least-to-most**: pecah soal menjadi sub-pertanyaan, tanyakan berurutan, bandingkan dengan CoT biasa.

## Yang Dikumpulkan

1. `src/main.py` dengan 4 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Catatan hasil eksplorasi no. 1 (soal buatanmu + hasil perbandingannya).

> Kunci jawaban tersedia di `solusi/main_solusi.py` — gunakan hanya jika mentok, dan tulis ulang dengan pemahamanmu sendiri.
