"""Praktikum Pertemuan 02 — Prompt Engineering: Dasar & Teknik Lanjutan.

Gabungan praktikum lesson 04 (prompt engineering fundamentals) dan
lesson 05 (advanced prompts). Ada 7 fungsi bertanda TODO:

  Bagian A — Dasar   : TODO 1-4 (token, generate, chat, few-shot)
  Bagian B — Lanjutan: TODO 5-7 (chain-of-thought, self-consistency, self-refine)

Jalankan:
    python src/main.py

Demo yang TODO-nya belum selesai otomatis dilewati, jadi kamu bisa
mengerjakan dan menguji satu per satu.
"""
import os

import requests
import tiktoken

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
# Ganti sesuai model yang tersedia (lihat hasil `python src/cek_env.py`)
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
# Server kampus bisa lambat saat dipakai ramai-ramai — sabar ya :)
TIMEOUT = 300

# Soal cerita untuk demo Bagian B
SOAL = (
    "Di lab ada 12 komputer. 3 rusak, lalu kampus membeli 5 komputer baru, "
    "tetapi 2 dipinjam jurusan lain. Berapa komputer yang bisa dipakai praktikum?"
)


# ═════════════════════════════════════════════════════════════
# BAGIAN A — PROMPT ENGINEERING DASAR (materi lesson 04)
# ═════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# TODO 1: Tokenization
# ─────────────────────────────────────────────────────────────
def hitung_token(teks: str) -> int:
    """Kembalikan jumlah token dari `teks`."""
    # cl100k_base = skema tokenisasi yang dipakai model-model OpenAI modern
    enc = tiktoken.get_encoding("cl100k_base")
    token = enc.encode(teks)          # contoh: "Halo dunia" -> [39, 12812, 28479]
    return len(token)


# ─────────────────────────────────────────────────────────────
# TODO 2: Prompt tunggal via /api/generate (+ kontrol temperature)
# ─────────────────────────────────────────────────────────────
def generate(prompt: str, temperature: float = None) -> str:
    """Kirim `prompt` ke server Ollama dan kembalikan teks jawabannya.

    `temperature` opsional: 0.0 = konsisten/deterministik, 1.0 = kreatif.
    Bila None, server memakai nilai default model.
    """
    body = {"model": MODEL, "prompt": prompt, "stream": False}
    if temperature is not None:
        body["options"] = {"temperature": temperature}
    r = requests.post(f"{BASE_URL}/api/generate", json=body, timeout=TIMEOUT)
    r.raise_for_status()               # error-kan bila status bukan 2xx
    return r.json()["response"]


# ─────────────────────────────────────────────────────────────
# TODO 3: Percakapan multi-role via /api/chat
# ─────────────────────────────────────────────────────────────
def chat(messages: list) -> str:
    """Kirim percakapan (system/user/assistant) dan kembalikan jawaban model."""
    r = requests.post(
        f"{BASE_URL}/api/chat",
        json={
            "model": MODEL,
            "messages": messages,      # kunci "messages", bukan "prompt"
            "stream": False,
        },
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    # Perhatikan: jawaban ada di "message" (tunggal), beda dengan
    # "messages" (jamak) yang kita kirim.
    return r.json()["message"]["content"]


# ─────────────────────────────────────────────────────────────
# TODO 4: Menyusun prompt few-shot
# ─────────────────────────────────────────────────────────────
def buat_prompt_few_shot(contoh: list, input_baru: str) -> str:
    """Susun prompt few-shot dari daftar pasangan (input, output)."""
    baris = [f"{masukan} => {keluaran}" for masukan, keluaran in contoh]
    baris.append(f"{input_baru} =>")   # baris terakhir tanpa jawaban: dilanjutkan model
    return "\n".join(baris)


# ═════════════════════════════════════════════════════════════
# BAGIAN B — TEKNIK LANJUTAN (materi lesson 05)
# ═════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# TODO 5: Chain-of-Thought — fungsi murni penyusun prompt
# ─────────────────────────────────────────────────────────────
def prompt_cot(soal: str) -> str:
    return (
        f"{soal}\n\n"
        "Mari berpikir langkah demi langkah. Tulis penalaranmu, "
        'lalu akhiri dengan baris "JAWABAN: <angka/jawaban akhir>".'
    )


# ─────────────────────────────────────────────────────────────
# TODO 6: Self-consistency — tanya berulang, bandingkan jawaban
# ─────────────────────────────────────────────────────────────
def self_consistency(soal: str, n: int = 3) -> list:
    return [generate(prompt_cot(soal), temperature=0.9) for _ in range(n)]


# ─────────────────────────────────────────────────────────────
# TODO 7: Self-refine — fungsi murni penyusun prompt kritik
# ─────────────────────────────────────────────────────────────
def prompt_refine(jawaban: str, instruksi_awal: str) -> str:
    return (
        f"Tugas awal: {instruksi_awal}\n"
        f"Jawaban sebelumnya: {jawaban}\n\n"
        "Beri 2 kritik singkat atas jawaban itu, lalu tulis versi "
        "yang sudah diperbaiki."
    )


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
        ("DEMO A1 — Tokenization (TODO 1)", demo_tokenization),
        ("DEMO A2 — Instruksi mengubah output (TODO 2)", demo_instruksi),
        ("DEMO A3 — System message / complex prompt (TODO 3)", demo_system_message),
        ("DEMO A4 — Fabrication (TODO 2)", demo_fabrication),
        ("DEMO A5 — Few-shot prompting (TODO 4 + TODO 2)", demo_few_shot),
        ("DEMO B1 — Chain-of-Thought (TODO 5 + TODO 2)", demo_cot),
        ("DEMO B2 — Temperature rendah vs tinggi (TODO 2)", demo_temperature),
        ("DEMO B3 — Self-consistency (TODO 6)", demo_self_consistency),
        ("DEMO B4 — Self-refine (TODO 7 + TODO 2)", demo_refine),
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
