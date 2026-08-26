# Praktikum 04 — Dasar-Dasar Prompt Engineering

Modul praktikum ini adalah versi hands-on dari materi [README.md](../README.md), disesuaikan untuk dikerjakan di **GitHub Codespaces** dengan server **Ollama kampus** (`https://ollama.if.unismuh.ac.id`) — **tanpa perlu API key apa pun**.

## Tujuan Pembelajaran

Setelah menyelesaikan praktikum ini, kamu mampu:

1. Menjelaskan apa itu *prompt engineering* dan mengapa cara menulis prompt memengaruhi kualitas jawaban AI.
2. Memahami cara model "membaca" teks lewat *tokenization*, serta beda *base LLM* dan *instruction-tuned LLM*.
3. Menyusun prompt yang efektif: instruksi detail, *system message*, *few-shot examples*, dan *cues*.
4. Mengenali *fabrication* (model mengarang fakta) dan tahu cara menguranginya.

## Prasyarat

- Bisa membuka repo ini di GitHub Codespaces (menu **Code → Codespaces → Create codespace**).
- Paham dasar Python: menjalankan script, mengedit fungsi, membaca error.
- Tidak perlu API key — semua latihan memakai server Ollama kampus.

## Urutan Kerja

Semua perintah dijalankan dari folder ini: `cd 04-prompt-engineering-fundamentals/praktikum`

| No | Langkah | Perintah |
|----|---------|----------|
| 01 | **Buat environment** | `python3 -m venv .venv` |
| 02 | **Aktifkan** | `source .venv/bin/activate` |
| 03 | **Pasang library** | `pip install -r requirements.txt` |
| 04 | **Cek kesiapan** | `python src/cek_env.py` |
| 05 | **Isi TODO** | Kerjakan 4 fungsi di `src/main.py` |
| 06 | **Jalankan** | `python src/main.py` |
| 07 | **Uji jawaban** | `pytest -q` |
| 08 | **Eksplorasi** | Bandingkan waktu antar model di `notebooks/eksplorasi.ipynb` |

Detail tiap langkah ada di bawah. **Jangan lompat-lompat** — tiap langkah bergantung pada langkah sebelumnya.

---

## Langkah 01–02: Buat & Aktifkan Environment

**Kenapa?** *Virtual environment* (venv) adalah "kotak terisolasi" untuk library Python, supaya library praktikum ini tidak bercampur dengan proyek lain.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

✅ **Hasil yang seharusnya kamu lihat:** prompt terminal berubah, ada awalan `(.venv)` di kiri, contoh:

```
(.venv) @kamu ➜ .../04-prompt-engineering-fundamentals/praktikum $
```

## Langkah 03: Pasang Library

**Kenapa?** Kita butuh `requests` (mengirim HTTP request ke server AI), `tiktoken` (melihat cara teks dipecah jadi token), dan `pytest` (menguji jawabanmu otomatis).

```bash
pip install -r requirements.txt
```

✅ **Hasil:** baris terakhir kurang lebih `Successfully installed requests-... tiktoken-... pytest-...` tanpa error merah.

## Langkah 04: Cek Kesiapan

**Kenapa?** Sebelum menulis kode, pastikan environment benar dan server AI kampus bisa dijangkau — supaya kalau nanti ada error, kamu tahu itu bukan masalah koneksi.

```bash
python src/cek_env.py
```

✅ **Hasil:** semua baris `[OK]`, daftar model yang tersedia di server, dan tulisan `SIAP!`. Contoh:

```
[OK]   Python >= 3.9 — terdeteksi 3.12.1
[OK]   Library 'requests' terpasang
...
Model yang tersedia di server:
  - llama3.2:latest
  - ...
SIAP! Lanjut kerjakan TODO di src/main.py
```

📌 **Penting:** catat salah satu nama model dari daftar itu, lalu daftarkan ke terminal (ganti dengan nama model pilihanmu):

```bash
export OLLAMA_MODEL="llama3.2:latest"
```

> Kalau ada baris `[GAGAL]`, baca keterangannya: biasanya library belum terpasang (ulangi langkah 03) atau koneksi ke server bermasalah (lapor ke aslab).

## Langkah 05: Isi TODO di `src/main.py`

Ada **4 fungsi** yang harus kamu lengkapi. Tiap fungsi sudah berisi petunjuk langkah demi langkah di dalam docstring-nya. Kerjakan berurutan:

### TODO 1 — `hitung_token(teks)`

**Kenapa?** LLM tidak membaca huruf per huruf, melainkan **token** — potongan kecil teks (± sepotong kata). Jumlah token menentukan biaya dan batas panjang prompt (*context window* = jumlah token maksimal yang bisa "diingat" model dalam sekali percakapan). Dengan `tiktoken` kamu bisa melihat sendiri berapa token sebuah kalimat.

### TODO 2 — `generate(prompt)`

**Kenapa?** Ini pintu utama ke model: mengirim satu prompt teks ke endpoint `/api/generate` dan menerima jawaban. Semua eksperimen selanjutnya memakai fungsi ini.

### TODO 3 — `chat(messages)`

**Kenapa?** Aplikasi chat sungguhan tidak mengirim satu kalimat, tapi **daftar pesan dengan peran** (*role*): `system` (aturan main untuk AI), `user` (pertanyaanmu), `assistant` (jawaban AI sebelumnya). Endpoint `/api/chat` menerima format ini — di sinilah kamu melihat kekuatan *system message*.

### TODO 4 — `buat_prompt_few_shot(contoh, input_baru)`

**Kenapa?** *Few-shot prompting* = memberi model beberapa **contoh** pola input→output alih-alih instruksi eksplisit, lalu membiarkan model meneruskan polanya. Fungsi ini menyusun teks prompt-nya.

💡 Kerjakan satu TODO → langsung lompat ke langkah 06 untuk melihat hasilnya → kembali kerjakan TODO berikutnya. Demo yang TODO-nya belum selesai otomatis dilewati.

## Langkah 06: Jalankan

```bash
python src/main.py
```

**Kenapa?** Script ini menjalankan 5 demo yang membuktikan konsep dari materi:

| Demo | Konsep yang dibuktikan | Amati |
|------|------------------------|-------|
| 1. Tokenization | Model melihat token, bukan kata | Kalimat Indonesia vs Inggris — jumlah tokennya beda! |
| 2. Instruksi | Instruksi detail = jawaban lebih terarah | Prompt polos vs detail vs minta format JSON |
| 3. System message | *System message* mengubah gaya jawaban | Jawaban jadi gaya "guru SD" + bullet point |
| 4. Fabrication | Model bisa mengarang dengan meyakinkan | Model membuat rencana pelajaran "Perang Mars 2076" yang fiktif! |
| 5. Few-shot | Model meneruskan pola dari contoh | Jawaban "Basketball" tanpa pernah diberi instruksi |

✅ **Hasil:** kelima demo tampil tanpa baris `[LEWAT]`. Kalau masih ada `[LEWAT] TODO x belum dikerjakan`, kembali ke langkah 05.

### 🧠 Checkpoint 1 (jawab singkat di catatanmu, akan didiskusikan)

1. Dari Demo 2: apa perbedaan paling mencolok antara jawaban prompt polos dan prompt berformat JSON?
2. Dari Demo 4: model menjawab pertanyaan fiktif dengan sangat percaya diri. Mengapa ini **berbahaya** jika terjadi di aplikasi nyata (misal aplikasi kesehatan)? Sebutkan 1 cara menguranginya dari materi README.

## Langkah 07: Uji Jawaban

```bash
pytest -q
```

**Kenapa?** Tes otomatis memeriksa apakah keempat fungsimu benar — bukan cuma "jalan tanpa error", tapi hasilnya sesuai spesifikasi.

✅ **Hasil:** semua tes hijau, contoh:

```
......                                                    [100%]
6 passed in 4.21s
```

> Kalau ada `FAILED`, baca nama tesnya — misal `test_buat_prompt_few_shot_format` berarti TODO 4 belum sesuai format. Kalau ada `skipped`, artinya server tidak terjangkau saat tes jalan.

## Langkah 08: Eksplorasi

Buka [notebooks/eksplorasi.ipynb](./notebooks/eksplorasi.ipynb) di Codespaces (pilih kernel Python dari `.venv`), jalankan sel dari atas ke bawah.

**Kenapa?** Materi bilang *"model capabilities will vary"* dan *"model responses are stochastic"* (jawaban bisa berbeda meski prompt sama). Di notebook ini kamu membuktikannya sendiri: prompt yang sama dikirim ke beberapa model berbeda, lalu bandingkan **waktu respons** dan **isi jawaban** — plus mengirim prompt yang sama dua kali ke model yang sama.

### 🧠 Checkpoint 2

Jawab 3 pertanyaan refleksi di sel terakhir notebook, langsung di dalam notebook-nya.

---

## Rangkuman

- **Prompt = antarmuka pemrograman** untuk aplikasi AI generatif; kualitas prompt menentukan kualitas jawaban.
- Model membaca **token**, bukan teks — jumlah token memengaruhi biaya & batas *context window*.
- **Instruksi yang spesifik** (audience, panjang, format) menghasilkan jawaban yang jauh lebih berguna.
- **System message** mengatur "kepribadian" dan aturan main model dalam percakapan.
- **Few-shot** memberi contoh pola sehingga model paham tugas tanpa instruksi eksplisit.
- Model bisa **fabrication** — selalu validasi output AI, jangan telan mentah-mentah.
- Jawaban model **stokastik** dan tiap model **berbeda kemampuan** — prompt yang baik untuk satu model belum tentu optimal untuk model lain.

## Tugas Lanjutan (Opsional)

1. **Cue technique**: tambah demo sendiri di `main.py` — kirim prompt berisi teks tentang planet Jupiter (ada di README bagian *Prompt Cues*) diakhiri baris `Top 3 Fakta yang Kita Pelajari:` dan amati bagaimana model "mengambil pancingan" itu.
2. **Prompt template pendidikan**: rancang 1 prompt template untuk kasus nyata di kampusmu (misal: pembuat soal kuis dari materi kuliah). Uji minimal 2 iterasi perbaikan, catat prompt versi 1 vs versi 2 dan apa yang membaik.
3. Lanjut ke materi [Lesson 05 — Advanced Prompts](../../05-advanced-prompts/README.md) untuk teknik chain-of-thought dan lainnya.

## Yang Dikumpulkan

1. `src/main.py` dengan 4 TODO selesai (bukti: screenshot `pytest -q` semua hijau).
2. Jawaban Checkpoint 1 (file teks/markdown atau tulis tangan sesuai instruksi aslab).
3. `notebooks/eksplorasi.ipynb` yang sudah dijalankan + jawaban refleksi Checkpoint 2 terisi.
