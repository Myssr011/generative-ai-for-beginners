# Pertemuan 06 — RAG: AI yang Menjawab dari Dokumenmu (+ Keamanan & Lifecycle)

> Gabungan dari lesson asli: **13-securing-ai-applications**, **14-the-generative-ai-application-lifecycle**, dan **15-rag-and-vector-databases**.

Model AI tidak tahu isi aturan lab kampus kita. Dengan **RAG (Retrieval Augmented Generation)**, kalian membuat AI yang menjawab berdasarkan dokumen kalian sendiri: dokumen dipecah, dicari potongan yang relevan, lalu ditempel ke prompt. Kita juga belajar cara orang jahat "membajak" chatbot (prompt injection) dan kenapa aplikasi AI perlu terus dipantau setelah jadi.

## Tujuan Belajar

1. Membangun pipeline RAG lengkap: chunking → embedding → retrieval → augmented prompt.
2. Membuktikan bedanya jawaban model tanpa RAG vs dengan RAG.
3. Mengenali serangan prompt injection dan cara dasarnya memitigasi.
4. Memahami lifecycle aplikasi AI: kualitas, biaya, latensi — tidak pernah benar-benar "selesai".

## Konsep Inti

1. **RAG = Retrieval + Augmented + Generation**: cari potongan relevan, tempel ke prompt, baru minta jawaban.
2. **Chunking**: dokumen dipecah per paragraf sebelum di-embed.
3. **Retrieval memakai ilmu pertemuan-04**: embedding + cosine similarity.
4. **Prompt injection**: "abaikan semua instruksi sebelumnya…" — lawan dengan instruksi tegas & validasi.
5. **LLMOps**: ukur kualitas, harm, kejujuran (groundedness), biaya, dan latensi aplikasimu.

## Isi Folder Ini

| Folder/File | Isi |
|---|---|
| [MATERI.md#13-securing-ai](./MATERI.md#13-securing-ai) | Materi asli: mengamankan aplikasi AI |
| [MATERI.md#14-app-lifecycle](./MATERI.md#14-app-lifecycle) | Materi asli: lifecycle aplikasi Generative AI |
| [MATERI.md#15-rag-vector-db](./MATERI.md#15-rag-vector-db) | Materi asli: RAG dan vector database |
| [praktikum/](./praktikum/) | **Praktikum inti**: chunking, embedding, retrieval, augmented prompt (TODO 1–4) |
| src/15-rag/ | Notebook asli lesson 15 + data pendukung |
| images/ | Gambar pendukung materi |

## Alur Praktik

1. [praktikum/PRAKTIKUM.md](./praktikum/PRAKTIKUM.md): kerjakan `potong_dokumen`, `embedding`, `ambil_konteks`, `buat_prompt_rag` atas `data/materi.txt` → `pytest -q`.
2. Bandingkan demo "tanpa RAG" vs "dengan RAG" — cocokkan jawabannya dengan isi dokumen.
3. Eksperimen keamanan: coba serang chatbot RAG-mu dengan prompt injection, lalu perkuat prompt-nya (materi 13).

## Hubungan dengan Mini Project

RAG adalah tema mini project "Tanya Dokumen" — tinggal ganti `materi.txt` dengan dokumen pilihanmu. Kebiasaan "menyerang aplikasi sendiri" dipakai saat menguji project.

## Tugas

Lihat aturan pengumpulan di [SUBMISSION.md](./SUBMISSION.md).
