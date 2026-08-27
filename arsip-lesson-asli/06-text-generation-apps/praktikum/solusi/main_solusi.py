"""KUNCI JAWABAN — Praktikum 06 Text Generation Apps.
Coba kerjakan sendiri dulu di src/main.py; lihat ke sini bila mentok.
Uji: cp solusi/main_solusi.py src/main.py && python src/main.py
"""
import os

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
TIMEOUT = 300


# TODO 1 — JAWABAN
def buat_prompt_resep(jumlah: int, bahan: list, pantangan: str) -> str:
    return (
        f"Buatkan {jumlah} resep masakan menggunakan bahan berikut: "
        f"{', '.join(bahan)}. Hindari bahan/rasa: {pantangan}. "
        "Untuk tiap resep tulis nama, daftar bahan, dan langkah singkat."
    )


# TODO 2 — JAWABAN
def generate(prompt: str) -> str:
    r = requests.post(
        f"{BASE_URL}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["response"]


# TODO 3 — JAWABAN
def buat_prompt_belanja(resep_teks: str, bahan_dimiliki: list) -> str:
    return (
        f"Berikut resep: {resep_teks}\n"
        f"Saya sudah punya: {', '.join(bahan_dimiliki)}.\n"
        "Buat daftar belanja bahan yang masih harus dibeli saja, "
        "jangan sertakan bahan yang sudah saya punya."
    )


# ── Demo (sama dengan src/main.py) ───────────────────────────
BAHAN = ["ayam", "santan", "serai", "daun jeruk"]
PANTANGAN = "pedas"


def _potong(t, n=500):
    t = t.strip()
    return t if len(t) <= n else t[:n] + " ...[dipotong]"


def demo_resep():
    prompt = buat_prompt_resep(2, BAHAN, PANTANGAN)
    print("Prompt:", prompt, "\n")
    print(_potong(generate(prompt), 700))


def demo_belanja():
    resep = generate(buat_prompt_resep(1, BAHAN, PANTANGAN))
    dimiliki = ["ayam", "serai"]
    prompt = buat_prompt_belanja(resep, dimiliki)
    print(f"Bahan yang sudah dimiliki: {', '.join(dimiliki)}\n")
    print(_potong(generate(prompt)))
    print("\n  💡 Periksa: apakah ayam & serai IKUT muncul di daftar belanja?")
    print("     Kalau ikut, itulah pentingnya iterasi memperbaiki prompt!")


def main():
    demo_list = [
        ("DEMO 1 — Generator resep (TODO 1+2)", demo_resep),
        ("DEMO 2 — Daftar belanja pintar (TODO 3)", demo_belanja),
    ]
    print(f"Model yang dipakai: {MODEL}  (server: {BASE_URL})")
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
