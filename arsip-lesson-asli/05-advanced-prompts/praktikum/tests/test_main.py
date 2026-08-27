"""Uji jawaban praktikum 05. Jalankan dari folder praktikum/:  pytest -q"""
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


# ── TODO 2: prompt_cot (murni) ───────────────────────────────
def test_prompt_cot_memuat_soal_dan_instruksi():
    p = main.prompt_cot("Berapa 2+3?")
    assert "Berapa 2+3?" in p
    assert "langkah demi langkah" in p.lower()
    assert "JAWABAN" in p


# ── TODO 4: prompt_refine (murni) ────────────────────────────
def test_prompt_refine_memuat_kedua_bagian():
    p = main.prompt_refine("jawaban lama", "tugas awal xyz")
    assert "jawaban lama" in p
    assert "tugas awal xyz" in p
    assert "kritik" in p.lower() or "perbaik" in p.lower()


# ── TODO 1: generate ─────────────────────────────────────────
@butuh_server
def test_generate_tanpa_temperature():
    j = main.generate("Sebutkan satu warna. Jawab satu kata.")
    assert isinstance(j, str) and j.strip()


@butuh_server
def test_generate_dengan_temperature():
    j = main.generate("Sebutkan satu buah. Jawab satu kata.", temperature=0.2)
    assert isinstance(j, str) and j.strip()


# ── TODO 3: self_consistency ─────────────────────────────────
@butuh_server
def test_self_consistency_jumlah_jawaban():
    hasil = main.self_consistency("Berapa 4+4? Jawab angka saja.", n=2)
    assert isinstance(hasil, list) and len(hasil) == 2
    assert all(isinstance(j, str) and j.strip() for j in hasil)
