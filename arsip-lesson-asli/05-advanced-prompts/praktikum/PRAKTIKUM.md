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

Ada **4 fungsi** yang harus kamu lengkapi. Tiap fungsi sudah berisi petunjuk langkah demi langkah di dalam docstring-nya. Kerjakan berurutan:

### TODO 1 — `generate(prompt, temperature)`

**Kenapa?** Seperti praktikum 04, tapi kini bisa mengatur `options.temperature` — kunci demo keacakan.

### TODO 2 — `prompt_cot(soal)`

**Kenapa?** CoT hanyalah *teknik menyusun prompt* — instruksi "berpikir langkah demi langkah" memicu penalaran.

### TODO 3 — `self_consistency(soal, n)`

**Kenapa?** Karena jawaban model stokastik, bertanya n× lalu voting mengurangi jawaban ngawur.

### TODO 4 — `prompt_refine(jawaban, instruksi)`

**Kenapa?** Model bisa jadi "reviewer" untuk outputnya sendiri — dua panggilan lebih baik dari satu.

💡 Kerjakan satu TODO → langsung lompat ke langkah 06 untuk melihat hasilnya → kembali kerjakan TODO berikutnya. Demo yang TODO-nya belum selesai otomatis dilewati.

## Langkah 06: Jalankan

```bash
python src/main.py
```

**Kenapa?** Script ini menjalankan demo yang membuktikan konsep dari materi. Amati:

- **Demo 1:** bandingkan jawaban langsung vs jawaban ber-CoT untuk soal cerita komputer lab (jawaban benar: **12**). Mana yang benar?
- **Demo 2:** temperature 0.0 dijalankan 2× (jawaban mirip/identik) vs 1.0 dijalankan 2× (jawaban berbeda-beda).
- **Demo 3:** 3 jawaban self-consistency — apakah mayoritas menjawab 12?
- **Demo 4:** paragraf versi 1 vs versi hasil self-refine — apa yang membaik?

✅ **Hasil:** kelima demo tampil tanpa `[LEWAT]`. Kalau masih ada `[LEWAT] TODO x belum dikerjakan`, kembali ke langkah 05.

### 🧠 Checkpoint 1
1. Pada Demo 1, mengapa instruksi "berpikir langkah demi langkah" bisa mengubah akurasi jawaban, padahal modelnya sama?
2. Kapan kamu justru *tidak* ingin temperature tinggi? Beri 1 contoh aplikasi nyata.

## Langkah 07: Uji Jawaban

```bash
pytest -q
```

**Kenapa?** Tes otomatis memeriksa apakah fungsimu benar — bukan cuma "jalan tanpa error", tapi hasilnya sesuai spesifikasi.

✅ **Hasil:** semua tes hijau — `5 passed`.

> Kalau ada `FAILED`, baca nama tesnya untuk tahu TODO mana yang belum sesuai. Kalau ada `skipped`, artinya server tidak terjangkau saat tes jalan.

## Langkah 08: Eksplorasi

1. Ubah `SOAL` di `main.py` menjadi soal cerita buatanmu yang lebih menjebak. Apakah CoT masih menang?
2. Coba `self_consistency` dengan `n=5` dan `temperature=0.5` — apakah hasil voting lebih stabil?
3. (Bonus) Terapkan **least-to-most**: pecah soal menjadi sub-pertanyaan, tanyakan berurutan, bandingkan dengan CoT biasa.

### 🧠 Checkpoint 2

Self-consistency memanggil model n kali → n kali lebih lambat dan mahal. Dalam kondisi apa trade-off ini layak? Dalam kondisi apa tidak?

---

## Rangkuman

- **Chain-of-thought**: instruksi "berpikir langkah demi langkah" memicu penalaran — akurasi soal bernalar naik tanpa mengganti model.
- **Temperature** mengatur keacakan output: rendah = konsisten/deterministik, tinggi = variatif/kreatif.
- **Self-consistency**: tanya n× lalu ambil jawaban mayoritas — menukar biaya/waktu dengan keandalan.
- **Self-refine**: model mengkritik dan memperbaiki outputnya sendiri — dua panggilan lebih baik dari satu.
- Semua teknik ini hanyalah *cara menyusun prompt & memanggil model* — pilih sesuai kebutuhan akurasi vs biaya.

## Yang Dikumpulkan

1. `src/main.py` dengan 4 TODO selesai + screenshot `pytest -q` hijau.
2. Jawaban Checkpoint 1 & 2.
3. Catatan hasil eksplorasi no. 1 (soal buatanmu + hasil perbandingannya).

> Kunci jawaban tersedia di `solusi/main_solusi.py` — gunakan hanya jika mentok, dan tulis ulang dengan pemahamanmu sendiri.
