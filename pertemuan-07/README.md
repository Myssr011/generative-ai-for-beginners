# Pertemuan 07 — Model Terbuka, AI Agent & Wawasan Lanjutan

> Gabungan dari lesson asli: **16-open-source-models**, **17-ai-agents**, plus ringkasan wawasan **18-fine-tuning**, **19-slm**, **20-mistral**, dan **21-meta**.

Pertemuan materi terakhir! Kalian akan sadar satu hal keren: model yang kita pakai sejak pertemuan pertama (Llama via Ollama kampus) adalah **model terbuka** — bisa diunduh dan dijalankan sendiri. Hari ini kita bahas peta dunia model terbuka, apa itu AI agent, lalu buktikan sendiri beda model kecil vs besar pakai stopwatch. Ditutup briefing mini project.

## Tujuan Belajar

1. Membedakan model terbuka (Llama, Mistral, Phi, Gemma) vs tertutup (GPT) dan trade-off-nya.
2. Menjelaskan AI agent: LLM + state + tools yang berjalan dalam loop.
3. Mengukur sendiri kecepatan vs kualitas model kecil (SLM) vs besar.
4. Mengenal fine-tuning dan kapan memilihnya dibanding prompt engineering / RAG.

## Konsep Inti

1. **Open model** = bobot modelnya bisa diunduh & dijalankan sendiri — itulah yang dilakukan server Ollama kampus.
2. **AI Agent = LLM + state + tools dalam loop** — function calling pertemuan-05 adalah bahan dasarnya.
3. **SLM**: model kecil (ratusan juta parameter) = cepat & murah, tapi kualitas terbatas — pilih sesuai kebutuhan.
4. **Tiga jurus meningkatkan kualitas**: prompt engineering (termurah) → RAG (sedang) → fine-tuning (termahal, melatih ulang model).
5. **Keluarga model populer**: Mistral (Large/Small/Nemo) & Meta Llama (3.1, 3.2 vision) — kenali nama & kegunaannya.

## Isi Folder Ini

| Folder/File | Isi |
|---|---|
| [MATERI.md#16-open-source-models](./MATERI.md#16-open-source-models) | Materi asli: model open source |
| [MATERI.md#17-ai-agents](./MATERI.md#17-ai-agents) | Materi asli: AI agents & framework-nya |
| [MATERI.md#18-fine-tuning](./MATERI.md#18-fine-tuning) | Materi asli (wawasan): fine-tuning LLM |
| [MATERI.md#18-resources](./MATERI.md#18-resources) | Sumber belajar tambahan fine-tuning |
| [MATERI.md#19-slm](./MATERI.md#19-slm) | Materi asli (wawasan): Small Language Models & Phi-3 |
| [MATERI.md#20-mistral](./MATERI.md#20-mistral) | Materi asli (wawasan): keluarga model Mistral |
| [MATERI.md#21-meta](./MATERI.md#21-meta) | Materi asli (wawasan): keluarga model Meta Llama |
| [praktikum/](./praktikum/) | **Praktikum inti**: benchmark model kecil vs besar (TODO 1–2) |
| src/ | Kode contoh asli lesson 18–21 (python) sebagai referensi |
| images/ | Gambar pendukung materi |

## Alur Praktik

1. [praktikum/PRAKTIKUM.md](./praktikum/PRAKTIKUM.md): kerjakan `generate_model` (ukur durasi) dan `bandingkan` → `pytest -q`.
2. Benchmark `smollm2:135m` vs `llama3.2` vs `gemma3:27b`: mana tercepat? Mana jawabannya paling bagus? Layakkah selisihnya?
3. **Briefing mini project** + pembentukan kelompok — baca [../pertemuan-08/README.md](../pertemuan-08/README.md) sebelum pulang!

## Hubungan dengan Mini Project

Hasil benchmark hari ini = dasar memilih model untuk project kalian (mau cepat atau mau pintar?). Konsep agent juga bisa jadi nilai plus di tema "Asisten Ber-Tool".

## Tugas

Lihat aturan pengumpulan di [SUBMISSION.md](./SUBMISSION.md).
