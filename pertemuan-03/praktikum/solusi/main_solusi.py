"""KUNCI JAWABAN — Praktikum Pertemuan 03 (Text Generation & Chat App).

Berisi keenam TODO yang SUDAH LENGKAP, sebagai rujukan.
Coba kerjakan sendiri dulu di src/main.py; buka file ini bila mentok.
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


# TODO 4 — JAWABAN
def chat(messages: list) -> str:
    r = requests.post(
        f"{BASE_URL}/api/chat",
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["message"]["content"]


# TODO 5 — JAWABAN
def tambah_pesan(riwayat: list, role: str, content: str) -> list:
    # riwayat + [...] membuat list BARU, tidak mengubah yang asli
    return riwayat + [{"role": role, "content": content}]


# TODO 6 — JAWABAN
def potong_riwayat(riwayat: list, maks: int) -> list:
    if len(riwayat) <= maks:
        return riwayat
    # pesan pertama (system) + (maks-1) pesan terakhir
    return [riwayat[0]] + riwayat[-(maks - 1):]
