# Praktikum Pertemuan 03 — Aplikasi Text Generation & Chat

Versi hands-on dari materi [MATERI.md#06-text-generation-apps](../MATERI.md#06-text-generation-apps) dan [MATERI.md#07-chat-applications](../MATERI.md#07-chat-applications), memakai server Ollama kampus — tanpa API key. Satu praktikum, dua bagian:

- **Bagian A (recipe app):** merakit prompt dari input user → aplikasi generator teks.
- **Bagian B (chat app):** membangun inti chatbot — percakapan multi-giliran yang "mengingat" konteks.

## Tujuan Pembelajaran

1. Membangun aplikasi text generation: template prompt (f-string) + panggilan model + iterasi memperbaiki prompt.
2. Memahami bahwa chatbot **tidak punya memori** — "ingatan" berasal dari *seluruh riwayat percakapan* yang dikirim ulang tiap giliran.
3. Mengelola riwayat pesan (role `system`/`user`/`assistant`) sebagai struktur data.
4. Menangani keterbatasan **context window** dengan memangkas riwayat tanpa membuang system message.

## Prasyarat

- Sudah menyelesaikan [praktikum pertemuan-02](../../pertemuan-02/praktikum/PRAKTIKUM.md) (terutama TODO 2 `generate` dan TODO 3 `chat`).

## Urutan Kerja

Semua perintah dari folder ini: `cd pertemuan-03/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → `export OLLAMA_MODEL="..."` |
| 05 | **Isi TODO Bagian A** | Kerjakan TODO 1–3 di `src/main.py` |
| 06 | **Jalankan demo A** | `python src/main.py` (amati DEMO A1–A2) |
| 07 | **Isi TODO Bagian B** | Kerjakan TODO 4–6 di `src/main.py` |
| 08 | **Jalankan demo B** | `python src/main.py` (amati DEMO B1–B3) |
| 09 | **Uji jawaban** | `pytest -q` (target: `8 passed`) |
| 10 | **Eksplorasi** | Tantangan di bagian bawah |

## Bagian A — TODO 1–3 (Recipe App)

### TODO 1 — `buat_prompt_resep(jumlah, bahan, pantangan)`
**Kenapa?** Inilah bedanya "aplikasi AI" dengan "sekadar bertanya ke AI": prompt dirakit otomatis dari **input user** memakai f-string. User cukup isi bahan & pantangan, aplikasi yang menyusun kalimatnya.

### TODO 2 — `generate(prompt)`
**Kenapa?** Pintu ke model via `/api/generate` — sama seperti pertemuan-02, sekarang jadi mesin aplikasimu.

### TODO 3 — `buat_prompt_belanja(resep_teks, bahan_dimiliki)`
**Kenapa?** Output AI bisa jadi **input untuk panggilan AI berikutnya** (chaining): resep hasil TODO 1–2 diolah lagi menjadi daftar belanja. Amati juga betapa pentingnya instruksi "jangan sertakan yang sudah saya punya".

## Bagian B — TODO 4–6 (Chat App)

### TODO 4 — `chat(messages)`
**Kenapa?** Endpoint `/api/chat` menerima **daftar pesan ber-role** — fondasi semua chatbot.

### TODO 5 — `tambah_pesan(riwayat, role, content)`
**Kenapa?** Riwayat = list of dict yang terus tumbuh. Fungsi ini harus mengembalikan **list baru** (bukan mengubah yang lama) — kebiasaan penting agar data tidak berubah diam-diam.

### TODO 6 — `potong_riwayat(riwayat, maks)`
**Kenapa?** Context window terbatas: kalau riwayat kepanjangan, model "meluap". Pangkas riwayat, tapi **system message (pesan pertama) wajib selamat**.

## Demo yang Dijalankan (`python src/main.py`)

| Demo | Konsep yang dibuktikan | Amati |
|------|------------------------|-------|
| A1 Generator resep | Prompt dirakit dari input user | Resep sesuai bahan & pantangan |
| A2 Daftar belanja | Output AI jadi input AI (chaining) | Apakah bahan yang dimiliki ikut muncul? |
| B1 Chatbot mengingat | Riwayat dikirim ulang tiap giliran | Model "ingat" nama Budi |
| B2 Tanpa riwayat | Tidak ada riwayat = amnesia | Model tidak tahu nama user |
| B3 Memangkas riwayat | Context window terbatas | System message tetap di posisi 1 |

### 🧠 Checkpoint (jawab singkat, akan didiskusikan)

1. Dari Demo B1 vs B2: jelaskan dengan bahasamu kenapa model bisa "ingat" di B1 tapi "amnesia" di B2.
2. Dari Demo A2: kalau daftar belanja masih memuat bahan yang sudah dimiliki, bagian prompt mana yang akan kamu perbaiki?
3. Kenapa system message tidak boleh ikut terpotong saat riwayat dipangkas?

## Uji Jawaban

```bash
pytest -q
```

✅ **Hasil:** `8 passed`. `FAILED` = baca nama tesnya; `skipped` = server tidak terjangkau.

## Rangkuman

- Aplikasi AI = **template prompt + input user + panggilan model + olah jawaban**.
- Output model bisa **dirangkai** (chaining) menjadi input panggilan berikutnya.
- Chatbot **tidak punya memori** — riwayat dikirim ulang tiap giliran.
- **Context window terbatas** → pangkas riwayat, pertahankan system message.

## Tugas Lanjutan (Opsional)

1. Ganti domain resep jadi domain lain (rencana olahraga, itinerary liburan) — test harus tetap hijau.
2. Buat loop chat interaktif di terminal: `input()` → `tambah_pesan` → `chat` → cetak, sampai user mengetik `keluar`.
3. Gabungkan `potong_riwayat` ke loop chat-mu dengan `maks=6`, buktikan percakapan panjang tetap jalan.

## Yang Dikumpulkan

Lihat [SUBMISSION.md](../SUBMISSION.md) pertemuan ini.
