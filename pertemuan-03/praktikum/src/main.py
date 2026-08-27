"""Praktikum Pertemuan 03 — Aplikasi Text Generation & Chat.

Gabungan praktikum lesson 06 (recipe app) dan lesson 07 (chat app).
Ada 6 fungsi bertanda TODO:

  Bagian A — Recipe app: TODO 1-3 (prompt resep, generate, daftar belanja)
  Bagian B — Chat app  : TODO 4-6 (chat, kelola riwayat, potong riwayat)

Jalankan:
    python src/main.py
"""
import os

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
# Server kampus bisa lambat saat dipakai ramai-ramai — sabar ya :)
TIMEOUT = 300

SYSTEM = (
    "Kamu adalah asisten akademik Fakultas Teknik. Jawab singkat, ramah, "
    "dalam bahasa Indonesia."
)


# ═════════════════════════════════════════════════════════════
# BAGIAN A — RECIPE APP (materi lesson 06)
# ═════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# TODO 1: Template prompt resep — fungsi murni
# ─────────────────────────────────────────────────────────────
def buat_prompt_resep(jumlah: int, bahan: list, pantangan: str) -> str:
    return (
        f"Buatkan {jumlah} resep masakan menggunakan bahan berikut: "
        f"{', '.join(bahan)}. Hindari bahan/rasa: {pantangan}. "
        "Untuk tiap resep tulis nama, daftar bahan, dan langkah singkat."
    )


# ─────────────────────────────────────────────────────────────
# TODO 2: Panggil model
# ─────────────────────────────────────────────────────────────
def generate(prompt: str) -> str:
    r = requests.post(
        f"{BASE_URL}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["response"]


# ─────────────────────────────────────────────────────────────
# TODO 3: Template prompt daftar belanja — fungsi murni
# ─────────────────────────────────────────────────────────────
def buat_prompt_belanja(resep_teks: str, bahan_dimiliki: list) -> str:
    return (
        f"Berikut resep: {resep_teks}\n"
        f"Saya sudah punya: {', '.join(bahan_dimiliki)}.\n"
        "Buat daftar belanja bahan yang masih harus dibeli saja, "
        "jangan sertakan bahan yang sudah saya punya."
    )


# ═════════════════════════════════════════════════════════════
# BAGIAN B — CHAT APP (materi lesson 07)
# ═════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# TODO 4: Panggil endpoint chat
# ─────────────────────────────────────────────────────────────
def chat(messages: list) -> str:
    r = requests.post(
        f"{BASE_URL}/api/chat",
        json={"model": MODEL, "messages": messages, "stream": False},
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["message"]["content"]


# ─────────────────────────────────────────────────────────────
# TODO 5: Kelola riwayat percakapan — fungsi murni
# ─────────────────────────────────────────────────────────────
def tambah_pesan(riwayat: list, role: str, content: str) -> list:
    # riwayat + [...] membuat list BARU, tidak mengubah yang asli
    return riwayat + [{"role": role, "content": content}]


# ─────────────────────────────────────────────────────────────
# TODO 6: Batasi riwayat (manajemen context window) — murni
# ─────────────────────────────────────────────────────────────
def potong_riwayat(riwayat: list, maks: int) -> list:
    if len(riwayat) <= maks:
        return riwayat
    # pesan pertama (system) + (maks-1) pesan terakhir
    return [riwayat[0]] + riwayat[-(maks - 1):]


# ─────────────────────────────────────────────────────────────
# Demo — tidak perlu diubah. Jalankan: python src/main.py
# ─────────────────────────────────────────────────────────────
BAHAN = ["ayam", "santan", "serai", "daun jeruk"]
PANTANGAN = "pedas"


def _potong(t, n=400):
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


def demo_memori():
    riwayat = [{"role": "system", "content": SYSTEM}]
    giliran = [
        "Halo! Namaku Budi, mahasiswa Informatika semester 3.",
        "Aku kesulitan memahami rekursi.",
        "Siapa namaku dan semester berapa aku? Jawab singkat.",
    ]
    for ucapan in giliran:
        riwayat = tambah_pesan(riwayat, "user", ucapan)
        jawaban = chat(riwayat)
        riwayat = tambah_pesan(riwayat, "assistant", jawaban)
        print(f"\n🧑 {ucapan}")
        print(f"🤖 {_potong(jawaban, 300)}")
    print("\n  💡 Model 'ingat' nama Budi karena SELURUH riwayat dikirim ulang")
    print("     setiap giliran — bukan karena model punya memori sendiri!")


def demo_tanpa_riwayat():
    print("Pertanyaan yang sama, tetapi TANPA mengirim riwayat:")
    jawaban = chat(
        [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": "Siapa namaku? Jawab singkat."},
        ]
    )
    print(f"🤖 {_potong(jawaban, 300)}")


def demo_potong_riwayat():
    riwayat = [{"role": "system", "content": SYSTEM}]
    for i in range(1, 8):
        riwayat = tambah_pesan(riwayat, "user", f"pesan ke-{i}")
    hasil = potong_riwayat(riwayat, maks=4)
    print(f"Riwayat awal : {len(riwayat)} pesan")
    print(f"Setelah potong (maks=4): {len(hasil)} pesan")
    for p in hasil:
        print(f"  - [{p['role']}] {p['content'][:50]}")
    print("\n  💡 Context window terbatas — aplikasi chat nyata harus memangkas")
    print("     riwayat, tetapi system message tidak boleh ikut terbuang.")


def main():
    demo_list = [
        ("DEMO A1 — Generator resep (TODO 1+2)", demo_resep),
        ("DEMO A2 — Daftar belanja pintar (TODO 3)", demo_belanja),
        ("DEMO B1 — Chatbot yang 'mengingat' (TODO 4+5)", demo_memori),
        ("DEMO B2 — Tanpa riwayat = amnesia (TODO 4)", demo_tanpa_riwayat),
        ("DEMO B3 — Memangkas riwayat (TODO 6)", demo_potong_riwayat),
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
