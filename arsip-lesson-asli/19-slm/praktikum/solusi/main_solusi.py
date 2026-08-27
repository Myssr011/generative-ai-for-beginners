"""KUNCI JAWABAN — Praktikum 19 SLM.
Coba kerjakan sendiri dulu di src/main.py; lihat ke sini bila mentok.
"""
import os
import time

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
TIMEOUT = 300

MODEL_UJI = [
    os.environ.get("OLLAMA_MODEL_KECIL", "smollm2:135m"),
    os.environ.get("OLLAMA_MODEL_SEDANG", "llama3.2:latest"),
    os.environ.get("OLLAMA_MODEL_BESAR", "gemma3:27b"),
]


# TODO 1 — JAWABAN
def generate_model(model: str, prompt: str) -> tuple:
    mulai = time.perf_counter()
    r = requests.post(
        f"{BASE_URL}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    durasi = time.perf_counter() - mulai
    return (r.json()["response"], durasi)


# TODO 2 — JAWABAN
def bandingkan(daftar_model: list, prompt: str, fn=None) -> list:
    if fn is None:
        fn = generate_model
    hasil = []
    for model in daftar_model:
        jawaban, durasi = fn(model, prompt)
        hasil.append({"model": model, "durasi": durasi, "jawaban": jawaban})
    return sorted(hasil, key=lambda h: h["durasi"])


# ── Demo (sama dengan src/main.py) ───────────────────────────
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
