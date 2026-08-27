"""Praktikum 15 — RAG (Retrieval Augmented Generation).

Lengkapi keempat fungsi bertanda TODO, lalu jalankan:
    python src/main.py
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


# ── Sudah disediakan (dipelajari di praktikum 04 & 08) ────────
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


# ─────────────────────────────────────────────────────────────
# TODO 1: Chunking — memecah dokumen menjadi potongan
# ─────────────────────────────────────────────────────────────
def potong_dokumen(teks: str) -> list:
    """Pecah `teks` menjadi list potongan (chunk) per PARAGRAF.

    Petunjuk:
    1. Paragraf dipisahkan baris kosong: teks.split("\\n\\n")
    2. Buang spasi tepi tiap paragraf (.strip())
    3. Abaikan paragraf kosong.
    """
    raise NotImplementedError("TODO 1 (potong_dokumen) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 2: Embedding — teks menjadi vektor
# ─────────────────────────────────────────────────────────────
def embedding(teks: str) -> list:
    """POST ke /api/embeddings dengan {"model": EMBED_MODEL,
    "prompt": teks}; kembalikan r.json()["embedding"].
    (Sama seperti praktikum 08.)
    """
    raise NotImplementedError("TODO 2 (embedding) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 3: Retrieval — ambil potongan paling relevan
# ─────────────────────────────────────────────────────────────
def ambil_konteks(query: str, potongan: list, k: int = 2) -> list:
    """Kembalikan `k` potongan paling relevan dengan `query`
    (list of string, terurut dari paling relevan).

    Petunjuk:
    1. v = embedding(query)
    2. skor tiap potongan = cosine_similarity(v, embedding(potongan))
    3. urutkan menurun, ambil k, kembalikan STRING-nya saja.
    """
    raise NotImplementedError("TODO 3 (ambil_konteks) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 4: Augmented prompt — fungsi murni
# ─────────────────────────────────────────────────────────────
def buat_prompt_rag(query: str, konteks: list) -> str:
    """Susun prompt yang menyuruh model menjawab HANYA dari konteks.

    Prompt harus memuat semua isi `konteks` dan `query`. Contoh pola:
        Jawab pertanyaan HANYA berdasarkan konteks berikut.
        Jika jawabannya tidak ada di konteks, katakan tidak tahu.

        Konteks:
        {konteks digabung baris baru}

        Pertanyaan: {query}
    """
    raise NotImplementedError("TODO 4 (buat_prompt_rag) belum dikerjakan")


# ── Pipeline lengkap (memakai keempat TODO-mu) ───────────────
def jawab_dengan_rag(query: str, potongan: list) -> str:
    konteks = ambil_konteks(query, potongan, k=2)
    return generate(buat_prompt_rag(query, konteks))


# ─────────────────────────────────────────────────────────────
# Demo — tidak perlu diubah
# ─────────────────────────────────────────────────────────────
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
