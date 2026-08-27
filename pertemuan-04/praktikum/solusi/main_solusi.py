"""KUNCI JAWABAN — Praktikum Pertemuan 04 Search Applications.
Coba kerjakan sendiri dulu di src/main.py; lihat ke sini bila mentok.
"""
import math
import os

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
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


# TODO 1 — JAWABAN
def embedding(teks: str) -> list:
    r = requests.post(
        f"{BASE_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": teks},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["embedding"]


# TODO 2 — JAWABAN
def cosine_similarity(a: list, b: list) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b)


# TODO 3 — JAWABAN
def cari(query: str, dokumen: list, k: int = 3) -> list:
    v_query = embedding(query)
    skor = [(cosine_similarity(v_query, embedding(d)), d) for d in dokumen]
    return sorted(skor, key=lambda s: s[0], reverse=True)[:k]


# ── Demo (sama dengan src/main.py) ───────────────────────────
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
