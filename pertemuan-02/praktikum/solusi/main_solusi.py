"""KUNCI JAWABAN — Praktikum Pertemuan 02 (Prompt Engineering Dasar & Lanjutan).

Berisi ketujuh TODO yang SUDAH LENGKAP, sebagai rujukan.
Coba kerjakan sendiri dulu di src/main.py; buka file ini bila mentok,
pahami barisnya, lalu tulis ulang dengan pengertianmu sendiri.
"""
import os

import requests
import tiktoken

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
TIMEOUT = 300


# TODO 1 — JAWABAN
def hitung_token(teks: str) -> int:
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(teks))


# TODO 2 — JAWABAN
def generate(prompt: str, temperature: float = None) -> str:
    body = {"model": MODEL, "prompt": prompt, "stream": False}
    if temperature is not None:
        body["options"] = {"temperature": temperature}
    r = requests.post(f"{BASE_URL}/api/generate", json=body, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()["response"]


# TODO 3 — JAWABAN
def chat(messages: list) -> str:
    r = requests.post(
        f"{BASE_URL}/api/chat",
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["message"]["content"]


# TODO 4 — JAWABAN
def buat_prompt_few_shot(contoh: list, input_baru: str) -> str:
    baris = [f"{masukan} => {keluaran}" for masukan, keluaran in contoh]
    baris.append(f"{input_baru} =>")
    return "\n".join(baris)


# TODO 5 — JAWABAN
def prompt_cot(soal: str) -> str:
    return (
        f"{soal}\n\n"
        "Mari berpikir langkah demi langkah. Tulis penalaranmu, "
        'lalu akhiri dengan baris "JAWABAN: <angka/jawaban akhir>".'
    )


# TODO 6 — JAWABAN
def self_consistency(soal: str, n: int = 3) -> list:
    return [generate(prompt_cot(soal), temperature=0.9) for _ in range(n)]


# TODO 7 — JAWABAN
def prompt_refine(jawaban: str, instruksi_awal: str) -> str:
    return (
        f"Tugas awal: {instruksi_awal}\n"
        f"Jawaban sebelumnya: {jawaban}\n\n"
        "Beri 2 kritik singkat atas jawaban itu, lalu tulis versi "
        "yang sudah diperbaiki."
    )
