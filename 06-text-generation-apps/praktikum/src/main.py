"""Praktikum 06 — Aplikasi Text Generation (Recipe App).

Lengkapi ketiga fungsi bertanda TODO, lalu jalankan:
    python src/main.py
"""
import os

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
# Server kampus bisa lambat saat dipakai ramai-ramai — sabar ya :)
TIMEOUT = 300


# ─────────────────────────────────────────────────────────────
# TODO 1: Template prompt resep — fungsi murni
# ─────────────────────────────────────────────────────────────
def buat_prompt_resep(jumlah: int, bahan: list, pantangan: str) -> str:
    """Susun prompt yang meminta `jumlah` resep dari daftar `bahan`,
    menghindari `pantangan`.

    Prompt harus memuat: angka `jumlah`, SEMUA bahan (pisahkan dengan
    koma), dan kata pantangan. Contoh pola:
        Buatkan {jumlah} resep masakan menggunakan bahan berikut:
        {bahan dipisah koma}. Hindari bahan/rasa: {pantangan}.
        Untuk tiap resep tulis nama, daftar bahan, dan langkah singkat.
    """
    raise NotImplementedError("TODO 1 (buat_prompt_resep) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 2: Panggil model
# ─────────────────────────────────────────────────────────────
def generate(prompt: str) -> str:
    """POST ke /api/generate (model MODEL, stream False), kembalikan
    r.json()["response"] — sama seperti praktikum 04.
    """
    raise NotImplementedError("TODO 2 (generate) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 3: Template prompt daftar belanja — fungsi murni
# ─────────────────────────────────────────────────────────────
def buat_prompt_belanja(resep_teks: str, bahan_dimiliki: list) -> str:
    """Susun prompt daftar belanja untuk `resep_teks`, TANPA menyertakan
    bahan yang sudah dimiliki.

    Prompt harus memuat resep_teks dan semua bahan_dimiliki. Contoh pola:
        Berikut resep: {resep_teks}
        Saya sudah punya: {bahan dipisah koma}.
        Buat daftar belanja bahan yang masih harus dibeli saja.
    """
    raise NotImplementedError("TODO 3 (buat_prompt_belanja) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# Demo — tidak perlu diubah
# ─────────────────────────────────────────────────────────────
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
