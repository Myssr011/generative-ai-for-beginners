"""Uji jawaban praktikum 06. Jalankan dari folder praktikum/:  pytest -q"""
import pytest
import requests

import main


def _server_tersedia():
    try:
        return requests.get(f"{main.BASE_URL}/api/tags", timeout=5).ok
    except requests.RequestException:
        return False


butuh_server = pytest.mark.skipif(
    not _server_tersedia(), reason="server Ollama kampus tidak terjangkau"
)


# ── TODO 1 (murni) ───────────────────────────────────────────
def test_prompt_resep_memuat_semua_unsur():
    p = main.buat_prompt_resep(3, ["telur", "tahu"], "asin")
    assert "3" in p
    assert "telur" in p and "tahu" in p
    assert "asin" in p


# ── TODO 3 (murni) ───────────────────────────────────────────
def test_prompt_belanja_memuat_resep_dan_bahan():
    p = main.buat_prompt_belanja("Resep opor spesial", ["ayam", "garam"])
    assert "Resep opor spesial" in p
    assert "ayam" in p and "garam" in p
    assert "beli" in p.lower() or "belanja" in p.lower()


# ── TODO 2 ───────────────────────────────────────────────────
@butuh_server
def test_generate_mengembalikan_teks():
    j = main.generate("Sebutkan satu nama sayur. Jawab satu kata.")
    assert isinstance(j, str) and j.strip()
