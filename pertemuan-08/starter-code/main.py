"""Mini Project — Template Awal.

Kembangkan file ini sesuai tema project kelompokmu.
Fungsi dasar pemanggilan model sudah disediakan (hasil praktikum
pertemuan 2, 3, dan 4) — fokuslah menggabungkan minimal 2 konsep
dari pertemuan 1-7 di fungsi main().

Jalankan:
    python main.py
"""
import os

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
EMBED_MODEL = os.environ.get("OLLAMA_EMBED_MODEL", "bge-m3:latest")
TIMEOUT = 300


def generate(prompt: str) -> str:
    """Prompt tunggal -> teks jawaban (lihat pertemuan-02)."""
    r = requests.post(
        f"{BASE_URL}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["response"]


def chat(messages: list) -> str:
    """Percakapan multi-role -> jawaban model (lihat pertemuan-03)."""
    r = requests.post(
        f"{BASE_URL}/api/chat",
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["message"]["content"]


def embedding(teks: str) -> list:
    """Teks -> vektor embedding (lihat pertemuan-04 & 06)."""
    r = requests.post(
        f"{BASE_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": teks},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["embedding"]


def main():
    # TODO: rakit aplikasimu di sini.
    # Contoh kerangka loop chat sederhana:
    #   riwayat = [{"role": "system", "content": "<system prompt kelompokmu>"}]
    #   while True:
    #       tanya = input("🧑 ")
    #       if tanya.lower() in ("exit", "keluar"):
    #           break
    #       riwayat.append({"role": "user", "content": tanya})
    #       jawab = chat(riwayat)
    #       riwayat.append({"role": "assistant", "content": jawab})
    #       print(f"🤖 {jawab}")
    print("Template mini project — mulai koding di fungsi main()!")
    print(f"Server: {BASE_URL} | Model: {MODEL}")


if __name__ == "__main__":
    main()
