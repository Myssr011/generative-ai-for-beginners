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

### TODO 1 — `chat(messages)`

**Kenapa?** Endpoint percakapan multi-role — fondasi seluruh aplikasi chat.

### TODO 2 — `tambah_pesan(riwayat, role, content)`

**Kenapa?** Riwayat = data; harus dikelola *immutable* (kembalikan list baru) agar tidak ada efek samping.

### TODO 3 — `potong_riwayat(riwayat, maks)`

**Kenapa?** Context window terbatas; aplikasi nyata wajib memangkas riwayat tapi system message harus selamat.

💡 Kerjakan satu TODO → langsung lompat ke langkah 06 untuk melihat hasilnya → kembali kerjakan TODO berikutnya. Demo yang TODO-nya belum selesai otomatis dilewati.

## Langkah 06: Jalankan

```bash
python src/main.py
```

**Kenapa?** Script ini menjalankan demo yang membuktikan konsep dari materi. Amati:

- **Demo 1:** 3 giliran percakapan — di giliran terakhir model tahu "Budi, semester 3" karena riwayat dikirim ulang.
- **Demo 2:** pertanyaan sama tanpa riwayat → model "amnesia", tidak tahu nama pengguna.
- **Demo 3:** 8 pesan dipangkas jadi 4: system + 3 pesan terakhir.

✅ **Hasil:** ketiga demo tampil tanpa `[LEWAT]`. Kalau masih ada `[LEWAT] TODO x belum dikerjakan`, kembali ke langkah 05.

### 🧠 Checkpoint 1
Dari Demo 1 vs Demo 2: jelaskan dengan kata-katamu sendiri dari mana "ingatan" chatbot berasal. Apa konsekuensinya terhadap biaya (token) saat percakapan makin panjang?

## Langkah 07: Uji Jawaban

```bash
pytest -q
```

**Kenapa?** Tes otomatis memeriksa apakah fungsimu benar — bukan cuma "jalan tanpa error", tapi hasilnya sesuai spesifikasi.

✅ **Hasil:** semua tes hijau — `5 passed`.

> Kalau ada `FAILED`, baca nama tesnya untuk tahu TODO mana yang belum sesuai. Kalau ada `skipped`, artinya server tidak terjangkau saat tes jalan.

## Langkah 08: Eksplorasi

1. Buat loop chat interaktif dengan `input()` (ketik `keluar` untuk berhenti) memakai ketiga fungsimu.
2. Ganti `SYSTEM` menjadi persona lain (misal: dosen killer vs kakak tingkat santai) — bandingkan gaya jawabannya.
3. (Bonus) Panggil `potong_riwayat(riwayat, maks=6)` setiap giliran di loop chatmu, lalu buktikan kapan chatbot mulai "lupa" nama pengguna.

### 🧠 Checkpoint 2

`potong_riwayat` membuang pesan lama. Informasi apa yang bisa hilang, dan bagaimana aplikasi seperti ChatGPT mengatasinya? (petunjuk: ringkasan percakapan, RAG — praktikum 15)

---

## Rangkuman

- Chatbot **tidak punya memori** — "ingatan" berasal dari seluruh riwayat percakapan yang dikirim ulang tiap giliran.
- Riwayat = list pesan ber-role `system`/`user`/`assistant` yang dikelola sebagai struktur data.
- Percakapan makin panjang = token makin banyak = biaya naik dan mendekati batas **context window**.
- Memangkas riwayat wajib menyelamatkan **system message**; informasi lama yang terbuang bisa diatasi dengan ringkasan percakapan atau RAG.

## Yang Dikumpulkan

1. `src/main.py` dengan 3 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Kode loop chat interaktif dari Eksplorasi no. 1.

> Kunci jawaban di `solusi/main_solusi.py` — gunakan hanya jika mentok.
