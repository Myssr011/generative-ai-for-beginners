"""KUNCI JAWABAN — Praktikum 15 RAG.
Coba kerjakan sendiri dulu di src/main.py; lihat ke sini bila mentok.
"""
import math
import os
from pathlib import Path

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
EMBED_MODEL = os.environ.get("OLLAMA_EMBED_MODEL", "bge-m3:latest")
TIMEOUT = 300

DATA = Path(__file__).resolve().parent.parent / "data" / "materi.txt"


def generate(prompt: str) -> str:
    r = requests.post(
        f"{BASE_URL}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["response"]


def cosine_similarity(a: list, b: list) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


# TODO 1 — JAWABAN
def potong_dokumen(teks: str) -> list:
    return [p.strip() for p in teks.split("\n\n") if p.strip()]


# TODO 2 — JAWABAN
def embedding(teks: str) -> list:
    r = requests.post(
        f"{BASE_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": teks},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["embedding"]


# TODO 3 — JAWABAN
def ambil_konteks(query: str, potongan: list, k: int = 2) -> list:
    v = embedding(query)
    skor = [(cosine_similarity(v, embedding(p)), p) for p in potongan]
    skor.sort(key=lambda s: s[0], reverse=True)
    return [p for _, p in skor[:k]]


# TODO 4 — JAWABAN
def buat_prompt_rag(query: str, konteks: list) -> str:
    return (
        "Jawab pertanyaan HANYA berdasarkan konteks berikut. "
        "Jika jawabannya tidak ada di konteks, katakan tidak tahu.\n\n"
        "Konteks:\n" + "\n".join(konteks) + f"\n\nPertanyaan: {query}"
    )


def jawab_dengan_rag(query: str, potongan: list) -> str:
    konteks = ambil_konteks(query, potongan, k=2)
    return generate(buat_prompt_rag(query, konteks))


# ── Demo (sama dengan src/main.py) ───────────────────────────
def _potong(t, n=350):
    t = t.strip()
    return t if len(t) <= n else t[:n] + " ...[dipotong]"


QUERY = "Jam berapa laboratorium buka pada hari Sabtu, dan siapa kepala lab-nya?"


def demo_chunking():
    potongan = potong_dokumen(DATA.read_text(encoding="utf-8"))
    print(f"Dokumen terpecah menjadi {len(potongan)} potongan. Contoh:")
    for p in potongan[:3]:
        print(f"  - {p[:80]}...")


def demo_tanpa_rag():
    print(f"🧑 {QUERY}\n")
    print("🤖 (tanpa RAG):", _potong(generate(QUERY)))
    print("\n  ⚠ Model tidak tahu aturan lab kampus KITA — data itu tidak ada")
    print("    di data latihnya. Jawabannya menebak atau mengaku tidak tahu.")


def demo_dengan_rag():
    potongan = potong_dokumen(DATA.read_text(encoding="utf-8"))
    print(f"🧑 {QUERY}\n")
    konteks = ambil_konteks(QUERY, potongan, k=2)
    print("Potongan dokumen yang diambil (retrieval):")
    for kx in konteks:
        print(f"  - {kx[:80]}...")
    print("\n🤖 (dengan RAG):", _potong(jawab_dengan_rag(QUERY, potongan), 400))
    print("\n  💡 Jawaban benar: Sabtu 08.00-12.00, kepala lab Ibu Nurhayati.")
    print("     Cocokkan dengan data/materi.txt!")


def main():
    demo_list = [
        ("DEMO 1 — Chunking dokumen (TODO 1)", demo_chunking),
        ("DEMO 2 — Tanpa RAG: model tidak tahu (perlu TODO generate saja)", demo_tanpa_rag),
        ("DEMO 3 — Dengan RAG: retrieval + augmented prompt (TODO 1-4)", demo_dengan_rag),
    ]
    print(f"Model chat: {MODEL} | Model embedding: {EMBED_MODEL}")
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
