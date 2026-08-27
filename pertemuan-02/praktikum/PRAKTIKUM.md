# Praktikum Pertemuan 02 — Prompt Engineering: Dasar & Teknik Lanjutan

Versi hands-on dari materi [MATERI.md#04-prompt-engineering](../MATERI.md#04-prompt-engineering) dan [MATERI.md#05-advanced-prompts](../MATERI.md#05-advanced-prompts), memakai server Ollama kampus — tanpa API key. Satu praktikum, dua bagian:

- **Bagian A (dasar):** tokenisasi, memanggil model, percakapan multi-role, few-shot.
- **Bagian B (lanjutan):** temperature, chain-of-thought, self-consistency, self-refine.

## Tujuan Pembelajaran

1. Memahami bahwa model membaca **token** (bukan huruf) dan prompt adalah "antarmuka pemrograman" aplikasi AI.
2. Memanggil model lewat dua endpoint: `/api/generate` (prompt tunggal) dan `/api/chat` (multi-role dengan system message).
3. Menyusun prompt **few-shot** (memberi contoh pola) sebagai alternatif instruksi eksplisit.
4. Mengendalikan jawaban dengan **temperature** dan meningkatkan akurasi dengan **chain-of-thought**, **self-consistency**, dan **self-refine**.

## Prasyarat

- Sudah menyelesaikan setup di [pertemuan-01](../../pertemuan-01/README.md) (Python 3.9+, paham venv).

## Urutan Kerja

Semua perintah dari folder ini: `cd pertemuan-02/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → `export OLLAMA_MODEL="..."` |
| 05 | **Isi TODO Bagian A** | Kerjakan TODO 1–4 di `src/main.py` |
| 06 | **Jalankan demo A** | `python src/main.py` (amati DEMO A1–A5) |
| 07 | **Isi TODO Bagian B** | Kerjakan TODO 5–7 di `src/main.py` |
| 08 | **Jalankan demo B** | `python src/main.py` (amati DEMO B1–B4) |
| 09 | **Uji jawaban** | `pytest -q` (target: `10 passed`) |
| 10 | **Eksplorasi** | `notebooks/eksplorasi.ipynb` + tantangan di bawah |

Detail tiap TODO ada di bawah. **Jangan lompat-lompat** — tiap langkah bergantung pada langkah sebelumnya.

## Bagian A — TODO 1–4 (Dasar)

### TODO 1 — `hitung_token(teks)`
**Kenapa?** LLM tidak membaca huruf per huruf, melainkan **token** — potongan kecil teks. Jumlah token menentukan biaya dan batas *context window*. Dengan `tiktoken` kamu melihat sendiri berapa token sebuah kalimat.

### TODO 2 — `generate(prompt, temperature=None)`
**Kenapa?** Ini pintu utama ke model: kirim prompt ke `/api/generate`, terima jawaban. Parameter `temperature` (opsional) mengatur kreativitas: `0.0` = konsisten, `1.0` = kreatif — dipakai lagi di Bagian B.

### TODO 3 — `chat(messages)`
**Kenapa?** Aplikasi chat sungguhan mengirim **daftar pesan dengan peran**: `system` (aturan main AI), `user` (pertanyaanmu), `assistant` (jawaban sebelumnya). Di sinilah kekuatan *system message* terlihat.

### TODO 4 — `buat_prompt_few_shot(contoh, input_baru)`
**Kenapa?** *Few-shot prompting* = memberi model beberapa **contoh** pola input→output, lalu membiarkan model meneruskan polanya — tanpa instruksi eksplisit.

## Bagian B — TODO 5–7 (Lanjutan)

### TODO 5 — `prompt_cot(soal)`
**Kenapa?** *Chain-of-thought*: menyuruh model "berpikir langkah demi langkah" membuat soal cerita/logika jauh lebih sering dijawab benar dibanding minta jawaban langsung.

### TODO 6 — `self_consistency(soal, n)`
**Kenapa?** Jawaban model itu stokastik (bisa berubah-ubah). *Self-consistency*: tanya soal yang sama beberapa kali (temperature tinggi), lalu ambil jawaban yang paling sering muncul — voting mayoritas.

### TODO 7 — `prompt_refine(jawaban, instruksi_awal)`
**Kenapa?** *Self-refine*: minta model mengkritik jawabannya sendiri lalu menulis versi perbaikan. Dua panggilan model, hasil lebih matang.

## Demo yang Dijalankan (`python src/main.py`)

| Demo | Konsep yang dibuktikan | Amati |
|------|------------------------|-------|
| A1 Tokenization | Model melihat token, bukan kata | Kalimat Indonesia vs Inggris — jumlah token beda! |
| A2 Instruksi | Instruksi detail = jawaban terarah | Prompt polos vs detail vs format JSON |
| A3 System message | System message mengubah gaya | Jawaban bergaya "guru SD" + bullet |
| A4 Fabrication | Model bisa mengarang meyakinkan | Rencana pelajaran "Perang Mars 2076" fiktif! |
| A5 Few-shot | Model meneruskan pola contoh | Jawaban "Basketball" tanpa instruksi |
| B1 Chain-of-thought | Menalar bertahap lebih akurat | Bandingkan jawaban langsung vs CoT |
| B2 Temperature | 0.0 konsisten, 1.0 kreatif | Slogan yang sama vs berubah-ubah |
| B3 Self-consistency | Voting mayoritas jawaban | 3 percobaan, cek jawaban akhirnya |
| B4 Self-refine | AI mengkritik dirinya sendiri | Versi 1 vs versi perbaikan |

### 🧠 Checkpoint (jawab singkat di catatanmu, akan didiskusikan)

1. Dari Demo A2: apa beda paling mencolok jawaban prompt polos vs prompt berformat JSON?
2. Dari Demo A4: kenapa fabrication **berbahaya** di aplikasi nyata (misal aplikasi kesehatan)? Sebutkan 1 cara menguranginya (materi lesson 03).
3. Dari Demo B2: kapan kamu ingin temperature rendah, kapan tinggi? Beri masing-masing 1 contoh kasus.

## Uji Jawaban

```bash
pytest -q
```

✅ **Hasil:** `10 passed`. Kalau ada `FAILED`, baca nama tesnya (misal `test_prompt_cot_...` = TODO 5 belum sesuai). `skipped` = server tidak terjangkau saat tes.

## Rangkuman

- **Prompt = antarmuka pemrograman**; kualitas prompt menentukan kualitas jawaban.
- Model membaca **token** — memengaruhi biaya & batas context window.
- **System message** mengatur kepribadian & aturan main model.
- **Few-shot** memberi pola contoh; **CoT** menyuruh menalar bertahap; **self-consistency** voting jawaban; **self-refine** memperbaiki diri.
- Model bisa **fabrication** — selalu validasi output AI.

## Tugas Lanjutan (Opsional)

1. **Cue technique**: kirim prompt berisi teks tentang planet Jupiter diakhiri baris `Top 3 Fakta yang Kita Pelajari:` — amati model "mengambil pancingan".
2. **Prompt template kampus**: rancang prompt pembuat soal kuis dari materi kuliah; uji 2 iterasi perbaikan, catat apa yang membaik.
3. Gabungkan: `self_consistency` yang otomatis memilih jawaban mayoritas (bukan sekadar list).

## Yang Dikumpulkan

Lihat [SUBMISSION.md](../SUBMISSION.md) pertemuan ini.
