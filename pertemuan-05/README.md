# Pertemuan 05 — Kasih AI "Tangan": Function Calling (+ Low-Code & UX)

> Gabungan dari lesson asli: **10-building-low-code-ai-applications**, **11-integrating-with-function-calling**, dan **12-designing-ux-for-ai-applications**.

Model AI tidak tahu jadwal praktikum kampus kita — data itu tidak ada di data latihnya. Solusinya: beri dia *tool*. Hari ini kalian membuat AI yang bisa "minta tolong" ke kode kalian untuk mengambil data asli, sehingga jawabannya tidak ngarang. Plus dua wawasan penting: jalur low-code untuk non-programmer, dan prinsip desain aplikasi AI yang nyaman & jujur.

## Tujuan Belajar

1. Menjelaskan kenapa dan kapan AI butuh tool (data privat/terkini).
2. Menulis definisi tool (skema JSON) dan eksekutornya.
3. Merangkai alur lengkap function calling: tanya → model minta tool → kode kita eksekusi → model merangkum.
4. Mengenal Power Platform/Copilot Studio (low-code) dan prinsip UX aplikasi AI.

## Konsep Inti

1. **Model tidak tahu data privatmu** → beri dia tool untuk mengambilnya.
2. **Alur function calling**: user tanya → model *meminta* tool → **kode kita mengeksekusi** → hasil dikirim balik → model merangkai jawaban.
3. **Definisi tool = skema JSON**: nama, deskripsi, parameter wajib.
4. **Model hanya MEMINTA, tidak pernah menjalankan sendiri** — kontrol tetap di kita (penting untuk keamanan).
5. **UX AI yang baik**: transparan, mudah dikoreksi, tidak overclaim; low-code = membangun app AI tanpa banyak koding.

## Isi Folder Ini

| Folder/File | Isi |
|---|---|
| [MATERI.md#10-low-code](./MATERI.md#10-low-code) | Materi asli: aplikasi AI low-code (Power Platform) |
| [MATERI.md#10-assignment](./MATERI.md#10-assignment) | Tugas asli lesson 10 (opsional, butuh akun Power Apps) |
| [MATERI.md#11-function-calling](./MATERI.md#11-function-calling) | Materi asli: integrasi function calling |
| [MATERI.md#12-ux-ai](./MATERI.md#12-ux-ai) | Materi asli: desain UX untuk aplikasi AI |
| [praktikum/](./praktikum/) | **Praktikum inti**: definisi tool, eksekutor, chat ber-tools (TODO 1–3) |
| src/11-function-calling/ | Kode contoh asli lesson 11 (python, typescript, js-githubmodels) |
| images/ | Gambar pendukung materi |

## Alur Praktik

1. [praktikum/PRAKTIKUM.md](./praktikum/PRAKTIKUM.md): kerjakan `definisi_tools`, `jalankan_tool`, `chat_dengan_tools` → `pytest -q`.
2. Perhatikan demo pembanding: pertanyaan yang sama TANPA tool — model terpaksa menebak.
3. Brainstorm: kalau boleh memberi AI satu tool untuk kampus kita, tool apa yang paling berguna?

## Hubungan dengan Mini Project

Function calling adalah bahan utama tema mini project "Asisten Ber-Tool"; prinsip UX jadi checklist saat demo project kalian.

## Tugas

Lihat aturan pengumpulan di [SUBMISSION.md](./SUBMISSION.md).
