"""Praktikum Pertemuan 07 — Small Language Models (SLM): kecil vs besar.

Lengkapi kedua fungsi bertanda TODO, lalu jalankan:
    python src/main.py
"""
import os
import time

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
TIMEOUT = 300

# SLM super kecil (135 juta parameter) vs model "biasa" (3 miliar) vs besar (27 miliar)
MODEL_UJI = [
    os.environ.get("OLLAMA_MODEL_KECIL", "smollm2:135m"),
    os.environ.get("OLLAMA_MODEL_SEDANG", "llama3.2:latest"),
    os.environ.get("OLLAMA_MODEL_BESAR", "gemma3:27b"),
]


# ─────────────────────────────────────────────────────────────
# TODO 1: Panggil model tertentu + ukur waktunya
# ─────────────────────────────────────────────────────────────
def generate_model(model: str, prompt: str) -> tuple:
    """Kembalikan (jawaban, durasi_detik) dari `model` untuk `prompt`.

    Petunjuk:
    1. mulai = time.perf_counter()
    2. POST ke f"{BASE_URL}/api/generate" dengan
       {"model": model, "prompt": prompt, "stream": False}
    3. durasi = time.perf_counter() - mulai
    4. return (r.json()["response"], durasi)
    """
    raise NotImplementedError("TODO 1 (generate_model) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 2: Benchmark beberapa model — hasil terurut dari tercepat
# ─────────────────────────────────────────────────────────────
def bandingkan(daftar_model: list, prompt: str, fn=None) -> list:
    """Uji `prompt` pada tiap model, kembalikan list dict
    {"model": ..., "durasi": ..., "jawaban": ...}
    TERURUT dari durasi terkecil (tercepat dulu).

    Petunjuk:
    - fn adalah fungsi pemanggil model; jika None gunakan generate_model.
      (Parameter ini memudahkan pengujian tanpa server.)
    - Kumpulkan hasil tiap model, lalu sorted(..., key=lambda h: h["durasi"]).
    """
    raise NotImplementedError("TODO 2 (bandingkan) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# Demo — tidak perlu diubah
# ─────────────────────────────────────────────────────────────
def _potong(t, n=200):
    t = t.strip().replace("\n", " ")
    return t if len(t) <= n else t[:n] + " ...[dipotong]"


def demo_kecepatan():
    prompt = "Apa ibu kota Indonesia? Jawab satu kata."
    print(f'Prompt: "{prompt}"\n')
    for h in bandingkan(MODEL_UJI, prompt):
        print(f"  {h['durasi']:7.2f} dtk | {h['model']:24s} | {_potong(h['jawaban'], 60)}")
    print("\n  💡 Model kecil (135M parameter) biasanya jauh lebih cepat & murah.")


def demo_kualitas():
    prompt = (
        "Seorang petani punya 17 kambing. Semua kecuali 9 mati. "
        "Berapa kambing yang masih hidup? Jelaskan singkat."
    )
    print(f'Prompt (soal jebakan, jawaban benar: 9): "{prompt}"\n')
    for h in bandingkan(MODEL_UJI, prompt):
        print(f"--- {h['model']} ({h['durasi']:.2f} dtk) ---")
        print(f"  {_potong(h['jawaban'], 250)}\n")
    print("  💡 Di sinilah perbedaan muncul: model kecil cepat tapi mudah")
    print("     terjebak; model besar lebih bernalar tapi lambat & mahal.")


def main():
    demo_list = [
        ("DEMO 1 — Adu kecepatan: pertanyaan mudah (TODO 1+2)", demo_kecepatan),
        ("DEMO 2 — Adu kualitas: soal jebakan (TODO 1+2)", demo_kualitas),
    ]
    print(f"Model yang diuji: {', '.join(MODEL_UJI)}")
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
