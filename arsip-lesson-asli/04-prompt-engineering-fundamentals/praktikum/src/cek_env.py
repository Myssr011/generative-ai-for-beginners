"""Cek kesiapan environment praktikum.

Jalankan:  python src/cek_env.py
Semua baris harus [OK] sebelum kamu lanjut ke langkah berikutnya.
"""
import importlib
import sys

BASE_URL = "https://ollama.if.unismuh.ac.id"
semua_ok = True


def cek(label: str, kondisi: bool, keterangan: str = "") -> None:
    global semua_ok
    tanda = "[OK]  " if kondisi else "[GAGAL]"
    print(f"{tanda} {label}" + (f" — {keterangan}" if keterangan else ""))
    if not kondisi:
        semua_ok = False


print("=" * 60)
print("CEK KESIAPAN ENVIRONMENT PRAKTIKUM 04")
print("=" * 60)

# 1. Versi Python
versi = sys.version_info
cek("Python >= 3.9", versi >= (3, 9), f"terdeteksi {versi.major}.{versi.minor}.{versi.micro}")

# 2. Library wajib
for nama in ("requests", "tiktoken", "pytest"):
    try:
        importlib.import_module(nama)
        cek(f"Library '{nama}' terpasang", True)
    except ImportError:
        cek(f"Library '{nama}' terpasang", False, "jalankan: pip install -r requirements.txt")

# 3. Koneksi ke server Ollama kampus + daftar model
try:
    import requests

    r = requests.get(f"{BASE_URL}/api/tags", timeout=10)
    r.raise_for_status()
    model_list = [m["name"] for m in r.json().get("models", [])]
    cek("Terhubung ke server Ollama kampus", True, BASE_URL)
    if model_list:
        print("\nModel yang tersedia di server:")
        for m in model_list:
            print(f"  - {m}")
        print("\nPilih salah satu model di atas, lalu set sebelum menjalankan main.py:")
        print(f'  export OLLAMA_MODEL="{model_list[0]}"')
    else:
        cek("Ada model yang tersedia", False, "server hidup tetapi belum ada model")
except Exception as e:  # noqa: BLE001 - laporkan apa pun penyebab gagal konek
    cek("Terhubung ke server Ollama kampus", False, f"{type(e).__name__}: {e}")

print("\n" + "=" * 60)
if semua_ok:
    print("SIAP! Lanjut kerjakan TODO di src/main.py")
else:
    print("BELUM SIAP — perbaiki dulu baris [GAGAL] di atas.")
    sys.exit(1)
