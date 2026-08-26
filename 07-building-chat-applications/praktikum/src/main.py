"""Praktikum 07 — Membangun Aplikasi Chat.

Lengkapi ketiga fungsi bertanda TODO, lalu jalankan:
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


# ─────────────────────────────────────────────────────────────
# TODO 1: Panggil endpoint chat
# ─────────────────────────────────────────────────────────────
def chat(messages: list) -> str:
    """POST ke /api/chat dengan {"model": MODEL, "messages": messages,
    "stream": False}; jawaban di r.json()["message"]["content"].
    (Sama seperti TODO 3 praktikum 04.)
    """
    raise NotImplementedError("TODO 1 (chat) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 2: Kelola riwayat percakapan — fungsi murni
# ─────────────────────────────────────────────────────────────
def tambah_pesan(riwayat: list, role: str, content: str) -> list:
    """Kembalikan LIST BARU = riwayat + satu pesan {"role", "content"}.

    Penting: jangan mengubah (mutate) list `riwayat` asli —
    kembalikan salinan baru. Petunjuk: riwayat + [{...}].
    """
    raise NotImplementedError("TODO 2 (tambah_pesan) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# TODO 3: Batasi riwayat (manajemen context window) — murni
# ─────────────────────────────────────────────────────────────
def potong_riwayat(riwayat: list, maks: int) -> list:
    """Kembalikan riwayat dengan maksimal `maks` pesan:
    pesan pertama (system) HARUS selalu dipertahankan,
    sisanya ambil pesan-pesan TERAKHIR.

    Contoh: 10 pesan, maks=4 -> [system] + 3 pesan terakhir.
    Jika len(riwayat) <= maks, kembalikan apa adanya.
    """
    raise NotImplementedError("TODO 3 (potong_riwayat) belum dikerjakan")


# ─────────────────────────────────────────────────────────────
# Demo — tidak perlu diubah
# ─────────────────────────────────────────────────────────────
def _potong(t, n=300):
    t = t.strip()
    return t if len(t) <= n else t[:n] + " ...[dipotong]"


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
        print(f"🤖 {_potong(jawaban)}")
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
    print(f"🤖 {_potong(jawaban)}")


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
        ("DEMO 1 — Chatbot yang 'mengingat' (TODO 1+2)", demo_memori),
        ("DEMO 2 — Tanpa riwayat = amnesia (TODO 1)", demo_tanpa_riwayat),
        ("DEMO 3 — Memangkas riwayat (TODO 3)", demo_potong_riwayat),
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
