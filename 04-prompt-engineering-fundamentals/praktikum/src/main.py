"""Praktikum 04 — Prompt Engineering Fundamentals.

Lengkapi keempat fungsi bertanda TODO di bawah, lalu jalankan:

    python src/main.py

Fungsi yang belum dikerjakan akan dilewati otomatis oleh demo,
jadi kamu bisa mengerjakan dan menguji satu per satu.
"""
import os

import requests
import tiktoken

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
# Ganti sesuai model yang tersedia (lihat hasil `python src/cek_env.py`)
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")
# Server kampus bisa lambat saat dipakai ramai-ramai — sabar ya :)
TIMEOUT = 300


# ─────────────────────────────────────────────────────────────
# TODO 1: Tokenization
# ─────────────────────────────────────────────────────────────
def hitung_token(teks: str) -> int:
    """Kembalikan jumlah token dari `teks`.

    Petunjuk:
    1. Ambil encoder   : enc = tiktoken.get_encoding("cl100k_base")
    2. Encode teks     : token = enc.encode(teks)
    3. Kembalikan panjang daftar token itu (len).
    """
    raise NotImplementedError("TODO 1 (hitung_token) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 2: Prompt tunggal via /api/generate
# ─────────────────────────────────────────────────────────────
def generate(prompt: str) -> str:
    """Kirim `prompt` ke server Ollama dan kembalikan teks jawabannya.

    Petunjuk:
    1. POST ke f"{BASE_URL}/api/generate" dengan
       json={"model": MODEL, "prompt": prompt, "stream": False}
       dan timeout=TIMEOUT.
    2. Panggil r.raise_for_status() untuk memastikan tidak error.
    3. Teks jawaban ada di kunci "response" dari r.json().
    """
    raise NotImplementedError("TODO 2 (generate) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 3: Percakapan multi-role via /api/chat
# ─────────────────────────────────────────────────────────────
def chat(messages: list) -> str:
    """Kirim percakapan (system/user/assistant) dan kembalikan jawaban model.

    `messages` berbentuk:
        [{"role": "system", "content": "..."},
         {"role": "user",   "content": "..."}]

    Petunjuk:
    1. POST ke f"{BASE_URL}/api/chat" dengan
       json={"model": MODEL, "messages": messages, "stream": False}
       dan timeout=TIMEOUT.
    2. Jawaban ada di r.json()["message"]["content"].
    """
    raise NotImplementedError("TODO 3 (chat) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 4: Menyusun prompt few-shot
# ─────────────────────────────────────────────────────────────
def buat_prompt_few_shot(contoh: list, input_baru: str) -> str:
    """Susun prompt few-shot dari daftar pasangan (input, output).

    Format tiap contoh (satu baris per contoh):
        {input} => {output}
    Baris terakhir (tanpa jawaban, biar dilanjutkan model):
        {input_baru} =>

    Contoh hasil untuk contoh=[("The player ran the bases", "Baseball")]
    dan input_baru="The player made a slam-dunk":

        The player ran the bases => Baseball
        The player made a slam-dunk =>
    """
    raise NotImplementedError("TODO 4 (buat_prompt_few_shot) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# Demo — tidak perlu diubah. Jalankan: python src/main.py
# ─────────────────────────────────────────────────────────────
def _potong(teks: str, n: int = 400) -> str:
    teks = teks.strip()
    return teks if len(teks) <= n else teks[:n] + " ...[dipotong]"


def demo_tokenization():
    for kalimat in (
        "Halo, selamat datang di praktikum prompt engineering!",
        "Hello, welcome to the prompt engineering lab!",
    ):
        print(f'  "{kalimat}"')
        print(f"   -> {hitung_token(kalimat)} token\n")


def demo_instruksi():
    variasi = [
        ("Instruksi polos", "Jelaskan fotosintesis."),
        (
            "Instruksi detail",
            "Jelaskan fotosintesis untuk siswa SMP dalam 1 paragraf, "
            "lalu beri 3 poin penting.",
        ),
        (
            "Instruksi berformat",
            "Jelaskan fotosintesis untuk siswa SMP. Jawab HANYA dalam format "
            'JSON dengan kunci "ringkasan" (string) dan "poin_penting" (list 3 string).',
        ),
    ]
    for judul, prompt in variasi:
        print(f"\n--- {judul} ---")
        print(f"Prompt : {prompt}")
        print(f"Jawaban: {_potong(generate(prompt))}")


def demo_system_message():
    pesan = [
        {
            "role": "system",
            "content": "Kamu adalah guru SD. Jawab dengan bahasa sangat sederhana, "
            "maksimal 1 paragraf, lalu 3 bullet point.",
        },
        {"role": "user", "content": "Apa itu gravitasi?"},
    ]
    print(f"System : {pesan[0]['content']}")
    print(f"User   : {pesan[1]['content']}")
    print(f"Jawaban: {_potong(chat(pesan))}")


def demo_fabrication():
    prompt = "Buat rencana pelajaran sejarah tentang Perang Mars tahun 2076."
    print(f"Prompt : {prompt}")
    print(f"Jawaban: {_potong(generate(prompt))}")
    print("\n  ⚠ Perang Mars 2076 TIDAK PERNAH terjadi. Perhatikan betapa")
    print("    meyakinkannya jawaban model — inilah yang disebut fabrication.")


def demo_few_shot():
    contoh = [
        ("The player ran the bases", "Baseball"),
        ("The player hit an ace", "Tennis"),
        ("The player hit a six", "Cricket"),
    ]
    prompt = buat_prompt_few_shot(contoh, "The player made a slam-dunk")
    print("Prompt few-shot yang dikirim:")
    print("  " + prompt.replace("\n", "\n  "))
    print(f"\nJawaban: {_potong(generate(prompt), 100)}")


def main():
    demo_list = [
        ("DEMO 1 — Tokenization (TODO 1)", demo_tokenization),
        ("DEMO 2 — Instruksi mengubah output (TODO 2)", demo_instruksi),
        ("DEMO 3 — System message / complex prompt (TODO 3)", demo_system_message),
        ("DEMO 4 — Fabrication (TODO 2)", demo_fabrication),
        ("DEMO 5 — Few-shot prompting (TODO 4 + TODO 2)", demo_few_shot),
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
