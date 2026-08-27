"""Praktikum Pertemuan 04 — Aplikasi Pencarian Semantik (Embeddings).

Lengkapi ketiga fungsi bertanda TODO, lalu jalankan:
    python src/main.py
"""
import math
import os

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
# Model khusus embedding (bukan model chat!) — bge-m3 bagus untuk bahasa Indonesia
EMBED_MODEL = os.environ.get("OLLAMA_EMBED_MODEL", "bge-m3:latest")
TIMEOUT = 300

DOKUMEN = [
    "Pertemuan 04 membahas dasar prompt engineering dan tokenisasi.",
    "Pertemuan 06 mengajarkan cara membangun aplikasi generator teks seperti aplikasi resep.",
    "Pertemuan 07 membahas cara membangun chatbot yang mengingat percakapan.",
    "Pertemuan 09 membahas pembuatan aplikasi penghasil gambar dengan AI.",
    "Pertemuan 13 membahas keamanan aplikasi AI dan ancaman prompt injection.",
    "Pertemuan 15 membahas RAG dan basis data vektor untuk menjawab dari dokumen sendiri.",
]


# ─────────────────────────────────────────────────────────────
# TODO 1: Ubah teks menjadi vektor angka (embedding)
# ─────────────────────────────────────────────────────────────
def embedding(teks: str) -> list:
    """Kembalikan vektor embedding untuk `teks`.

    Petunjuk:
    1. POST ke f"{BASE_URL}/api/embeddings" dengan
       json={"model": EMBED_MODEL, "prompt": teks}, timeout=TIMEOUT.
    2. raise_for_status(), lalu kembalikan r.json()["embedding"]
       (sebuah list berisi ratusan angka float).
    """
    raise NotImplementedError("TODO 1 (embedding) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 2: Cosine similarity — fungsi murni matematika
# ─────────────────────────────────────────────────────────────
def cosine_similarity(a: list, b: list) -> float:
    """Hitung kemiripan dua vektor: dot(a,b) / (|a| * |b|).

    Petunjuk:
    - dot   = jumlah dari x*y untuk tiap pasangan (pakai zip)
    - |a|   = math.sqrt(jumlah dari x*x)
    - hasil 1.0 = identik, 0.0 = tidak berhubungan.
    """
    raise NotImplementedError("TODO 2 (cosine_similarity) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 3: Mesin pencari semantik
# ─────────────────────────────────────────────────────────────
def cari(query: str, dokumen: list, k: int = 3) -> list:
    """Kembalikan `k` dokumen paling relevan sebagai list (skor, teks),
    terurut dari skor tertinggi.

    Petunjuk:
    1. v_query = embedding(query)
    2. Untuk tiap dok: hitung cosine_similarity(v_query, embedding(dok))
    3. Urutkan menurun berdasarkan skor (sorted + reverse=True),
       ambil k teratas.
    """
    raise NotImplementedError("TODO 3 (cari) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# Demo — tidak perlu diubah
# ─────────────────────────────────────────────────────────────
def demo_embedding():
    v = embedding("praktikum kecerdasan buatan")
    print(f"Teks diubah menjadi vektor {len(v)} dimensi.")
    print(f"5 angka pertama: {[round(x, 4) for x in v[:5]]}")


def demo_kemiripan():
    pasangan = [
        ("kucing duduk di sofa", "seekor kucing bersantai di kursi"),
        ("kucing duduk di sofa", "harga saham naik tajam hari ini"),
    ]
    for a, b in pasangan:
        skor = cosine_similarity(embedding(a), embedding(b))
        print(f'  "{a}" vs "{b}"\n   -> kemiripan: {skor:.4f}\n')
    print("  💡 Kalimat semakna berskor tinggi MESKI kata-katanya berbeda —")
    print("     inilah bedanya pencarian semantik vs pencarian kata kunci.")


def demo_cari():
    query = "bagaimana cara membuat chatbot?"
    print(f'Query: "{query}"\n')
    for skor, dok in cari(query, DOKUMEN, k=3):
        print(f"  [{skor:.4f}] {dok}")


def main():
    demo_list = [
        ("DEMO 1 — Teks menjadi vektor (TODO 1)", demo_embedding),
        ("DEMO 2 — Mengukur kemiripan makna (TODO 2)", demo_kemiripan),
        ("DEMO 3 — Mesin pencari semantik (TODO 3)", demo_cari),
    ]
    print(f"Model embedding: {EMBED_MODEL}  (server: {BASE_URL})")
    for judul, fungsi in demo_list:
        print(f"\n{'=' * 60}\n{judul}\n{'=' * 60}")
        try:
            fungsi()
        except NotImplementedError as e:
            print(f"[LEWAT] {e}")
        except requests.RequestException as e:
            print(f"[GAGAL JARINGAN] {type(e).__name__}: server lambat/tidak terjangkau.")
            print("  Coba jalankan ulang. Kalau berulang terus, lapor ke aslab.")


if __name__ == "__main__":
    main()
