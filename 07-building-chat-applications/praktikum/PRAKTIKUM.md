# Praktikum 07 — Membangun Aplikasi Chat

Versi hands-on dari materi [README.md](../README.md), memakai server Ollama kampus — tanpa API key. Kamu membangun inti chatbot: percakapan multi-giliran yang "mengingat" konteks.

## Tujuan Pembelajaran

1. Memahami bahwa chatbot **tidak punya memori** — "ingatan" berasal dari *seluruh riwayat percakapan* yang dikirim ulang tiap giliran.
2. Mengelola riwayat pesan (role `system`/`user`/`assistant`) sebagai struktur data.
3. Menangani keterbatasan **context window** (batas token yang bisa "diingat" model) dengan memangkas riwayat tanpa membuang system message.

## Prasyarat

- Sudah menyelesaikan [Praktikum 04](../../04-prompt-engineering-fundamentals/praktikum/PRAKTIKUM.md) (terutama TODO 3 `/api/chat`).

## Urutan Kerja

Semua perintah dari folder ini: `cd 07-building-chat-applications/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` → `export OLLAMA_MODEL="..."` |
| 05 | **Isi TODO** | Kerjakan 3 fungsi di `src/main.py` |
| 06 | **Jalankan** | `python src/main.py` |
| 07 | **Uji jawaban** | `pytest -q` (target: `5 passed`) |
| 08 | **Eksplorasi** | Tantangan di bagian bawah |

## Isi TODO (Langkah 05)

| TODO | Fungsi | Kenapa? |
|------|--------|---------|
| 1 | `chat(messages)` | Endpoint percakapan multi-role — fondasi seluruh aplikasi chat |
| 2 | `tambah_pesan(riwayat, role, content)` | Riwayat = data; harus dikelola *immutable* (kembalikan list baru) agar tidak ada efek samping |
| 3 | `potong_riwayat(riwayat, maks)` | Context window terbatas; aplikasi nyata wajib memangkas riwayat tapi system message harus selamat |

## Yang Diamati di Langkah 06

- **Demo 1:** 3 giliran percakapan — di giliran terakhir model tahu "Budi, semester 3" karena riwayat dikirim ulang.
- **Demo 2:** pertanyaan sama tanpa riwayat → model "amnesia", tidak tahu nama pengguna.
- **Demo 3:** 8 pesan dipangkas jadi 4: system + 3 pesan terakhir.

✅ **Validasi:** ketiga demo tampil tanpa `[LEWAT]`, `pytest -q` → `5 passed`.

### 🧠 Checkpoint 1
Dari Demo 1 vs Demo 2: jelaskan dengan kata-katamu sendiri dari mana "ingatan" chatbot berasal. Apa konsekuensinya terhadap biaya (token) saat percakapan makin panjang?

### 🧠 Checkpoint 2
`potong_riwayat` membuang pesan lama. Informasi apa yang bisa hilang, dan bagaimana aplikasi seperti ChatGPT mengatasinya? (petunjuk: ringkasan percakapan, RAG — praktikum 15)

## Langkah 08 — Eksplorasi

1. Buat loop chat interaktif dengan `input()` (ketik `keluar` untuk berhenti) memakai ketiga fungsimu.
2. Ganti `SYSTEM` menjadi persona lain (misal: dosen killer vs kakak tingkat santai) — bandingkan gaya jawabannya.
3. (Bonus) Panggil `potong_riwayat(riwayat, maks=6)` setiap giliran di loop chatmu, lalu buktikan kapan chatbot mulai "lupa" nama pengguna.

## Yang Dikumpulkan

1. `src/main.py` dengan 3 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Kode loop chat interaktif dari Eksplorasi no. 1.

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
