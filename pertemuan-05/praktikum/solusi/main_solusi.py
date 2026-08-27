"""KUNCI JAWABAN — Praktikum Pertemuan 05 Function Calling.
Coba kerjakan sendiri dulu di src/main.py; lihat ke sini bila mentok.
"""
import json
import os

import requests

BASE_URL = os.environ.get("OLLAMA_BASE_URL", "https://ollama.if.unismuh.ac.id")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:latest")
TIMEOUT = 300

JADWAL = {
    "senin": "Praktikum Basis Data, 08.00-10.00, Lab 1",
    "rabu": "Praktikum Kecerdasan Buatan, 13.00-15.00, Lab 2",
    "jumat": "Praktikum Jaringan Komputer, 09.00-11.00, Lab 3",
}


# TODO 1 — JAWABAN
def definisi_tools() -> list:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_jadwal_praktikum",
                "description": "Dapatkan jadwal praktikum untuk hari tertentu",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hari": {
                            "type": "string",
                            "description": "Nama hari, misal: senin",
                        }
                    },
                    "required": ["hari"],
                },
            },
        }
    ]


# TODO 2 — JAWABAN
def jalankan_tool(nama: str, argumen: dict) -> str:
    if nama == "get_jadwal_praktikum":
        hari = argumen["hari"].lower()
        return JADWAL.get(hari, "Tidak ada praktikum hari itu.")
    return f"Tool {nama} tidak dikenal."


# TODO 3 — JAWABAN
def chat_dengan_tools(messages: list) -> dict:
    r = requests.post(
        f"{BASE_URL}/api/chat",
        json={
            "model": MODEL,
            "messages": messages,
            "tools": definisi_tools(),
            "stream": False,
        },
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    return r.json()["message"]


# ── Demo (sama dengan src/main.py) ───────────────────────────
def demo_function_calling():
    pertanyaan = "Praktikum apa yang ada hari rabu, dan di lab mana?"
    print(f"🧑 {pertanyaan}\n")
    messages = [
        {"role": "system", "content": "Kamu asisten jadwal. Gunakan tool bila perlu."},
        {"role": "user", "content": pertanyaan},
    ]

    pesan = chat_dengan_tools(messages)
    tool_calls = pesan.get("tool_calls")
    if not tool_calls:
        print("Model menjawab langsung tanpa tool (coba jalankan ulang):")
        print(" ", (pesan.get("content") or "").strip()[:300])
        return

    print("1) Model MEMINTA pemanggilan tool:")
    messages.append(pesan)
    for tc in tool_calls:
        nama = tc["function"]["name"]
        argumen = tc["function"]["arguments"]
        if isinstance(argumen, str):
            argumen = json.loads(argumen)
        print(f"   -> {nama}({argumen})")

        hasil = jalankan_tool(nama, argumen)
        print(f"2) Kode KITA mengeksekusi tool: {hasil}")
        messages.append({"role": "tool", "content": hasil})

    final = chat_dengan_tools(messages)
    print(f"\n3) Jawaban akhir model:\n🤖 {(final.get('content') or '').strip()[:400]}")
    print("\n  💡 Model TIDAK menjalankan fungsi — ia hanya MEMINTA. Kode kitalah")
    print("     yang mengeksekusi, lalu hasilnya dikirim balik. Itulah function calling.")


def demo_tanpa_tool():
    print("Pertanyaan yang sama TANPA tools — model terpaksa menebak:")
    r = requests.post(
        f"{BASE_URL}/api/chat",
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": "Praktikum apa hari rabu di kampus ini?"}],
            "stream": False,
        },
        timeout=TIMEOUT,
    )
    r.raise_for_status()
    print(" ", r.json()["message"]["content"].strip()[:300])
    print("\n  ⚠ Tanpa akses data, jawabannya mengarang atau mengaku tidak tahu.")


def main():
    demo_list = [
        ("DEMO 1 — Alur lengkap function calling (TODO 1+2+3)", demo_function_calling),
        ("DEMO 2 — Pembanding: tanpa tools", demo_tanpa_tool),
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
