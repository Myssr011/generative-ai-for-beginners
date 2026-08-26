"""Cek kesiapan environment praktikum. Jalankan: python src/cek_env.py"""
import importlib
import sys

BASE_URL = "https://ollama.if.unismuh.ac.id"
semua_ok = True


def cek(label, kondisi, keterangan=""):
    global semua_ok
    print(("[OK]  " if kondisi else "[GAGAL]") + f" {label}" + (f" — {keterangan}" if keterangan else ""))
    if not kondisi:
        semua_ok = False


print("=" * 60 + "\nCEK KESIAPAN ENVIRONMENT PRAKTIKUM\n" + "=" * 60)
v = sys.version_info
cek("Python >= 3.9", v >= (3, 9), f"terdeteksi {v.major}.{v.minor}.{v.micro}")
for nama in ("requests", "pytest"):
    try:
        importlib.import_module(nama)
        cek(f"Library '{nama}' terpasang", True)
    except ImportError:
        cek(f"Library '{nama}' terpasang", False, "jalankan: pip install -r requirements.txt")
try:
    import requests

    r = requests.get(f"{BASE_URL}/api/tags", timeout=10)
    r.raise_for_status()
    model_list = [m["name"] for m in r.json().get("models", [])]
    cek("Terhubung ke server Ollama kampus", True, BASE_URL)
    print("\nModel yang tersedia di server:")
    for m in model_list:
        print(f"  - {m}")
    if model_list:
        print(f'\nSet model sebelum menjalankan main.py:\n  export OLLAMA_MODEL="{model_list[0]}"')
except Exception as e:  # noqa: BLE001
    cek("Terhubung ke server Ollama kampus", False, f"{type(e).__name__}: {e}")

print("\n" + "=" * 60)
if semua_ok:
    print("SIAP! Lanjut kerjakan TODO di src/main.py")
else:
    print("BELUM SIAP — perbaiki dulu baris [GAGAL] di atas.")
    sys.exit(1)
