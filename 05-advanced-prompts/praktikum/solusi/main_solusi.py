"""KUNCI JAWABAN — Praktikum 05 Advanced Prompts.
Coba kerjakan sendiri dulu di src/main.py; lihat ke sini bila mentok.
Uji: cp solusi/main_solusi.py src/main.py && python src/main.py
"""
import os

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
TIMEOUT = 300

SOAL = (
    "Di lab ada 12 komputer. 3 rusak, lalu kampus membeli 5 komputer baru, "
    "tetapi 2 dipinjam jurusan lain. Berapa komputer yang bisa dipakai praktikum?"
)


# TODO 1 — JAWABAN
def generate(prompt: str, temperature: float = None) -> str:
    body = {"model": MODEL, "prompt": prompt, "stream": False}
    if temperature is not None:
        body["options"] = {"temperature": temperature}
    r = requests.post(f"{BASE_URL}/api/generate", json=body, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()["response"]


# TODO 2 — JAWABAN
def prompt_cot(soal: str) -> str:
    return (
        f"{soal}\n\n"
        "Mari berpikir langkah demi langkah. Tulis penalaranmu, "
        'lalu akhiri dengan baris "JAWABAN: <angka/jawaban akhir>".'
    )


# TODO 3 — JAWABAN
def self_consistency(soal: str, n: int = 3) -> list:
    return [generate(prompt_cot(soal), temperature=0.9) for _ in range(n)]


# TODO 4 — JAWABAN
def prompt_refine(jawaban: str, instruksi_awal: str) -> str:
    return (
        f"Tugas awal: {instruksi_awal}\n"
        f"Jawaban sebelumnya: {jawaban}\n\n"
        "Beri 2 kritik singkat atas jawaban itu, lalu tulis versi "
        "yang sudah diperbaiki."
    )


# ── Demo (sama dengan src/main.py) ───────────────────────────
def _potong(t, n=350):
    t = t.strip()
    return t if len(t) <= n else t[:n] + " ...[dipotong]"


def demo_cot():
    print("Soal:", SOAL)
    print("\n--- Tanpa chain-of-thought ---")
    print(_potong(generate(SOAL + " Jawab langsung, satu angka saja.")))
    print("\n--- Dengan chain-of-thought ---")
    print(_potong(generate(prompt_cot(SOAL)), 600))


def demo_temperature():
    prompt = "Buat satu slogan kreatif untuk lab informatika. Jawab 1 kalimat."
    for t in (0.0, 1.0):
        print(f"\n--- temperature={t} (2x percobaan) ---")
        for i in (1, 2):
            print(f"  {i}. {_potong(generate(prompt, temperature=t), 120)}")


def demo_self_consistency():
    jawaban = self_consistency(SOAL, n=3)
    for i, j in enumerate(jawaban, 1):
        akhir = j.strip().splitlines()[-1] if j.strip() else "(kosong)"
        print(f"  Percobaan {i}: {akhir[:100]}")
    print("\n  💡 Ambil jawaban yang paling sering muncul (majority vote).")


def demo_refine():
    instruksi = "Tulis 1 paragraf ajakan mengikuti praktikum AI untuk mahasiswa baru."
    v1 = generate(instruksi)
    print("--- Versi 1 ---")
    print(_potong(v1, 250))
    v2 = generate(prompt_refine(v1, instruksi))
    print("\n--- Setelah self-refine ---")
    print(_potong(v2, 400))


def main():
    demo_list = [
        ("DEMO 1 — Chain-of-Thought (TODO 1+2)", demo_cot),
        ("DEMO 2 — Temperature rendah vs tinggi (TODO 1)", demo_temperature),
        ("DEMO 3 — Self-consistency (TODO 3)", demo_self_consistency),
        ("DEMO 4 — Self-refine (TODO 1+4)", demo_refine),
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
