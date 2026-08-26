"""Uji jawaban praktikum 08. Jalankan dari folder praktikum/:  pytest -q"""
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


# ── TODO 2 (murni) ───────────────────────────────────────────
def test_cosine_vektor_identik():
    assert main.cosine_similarity([1.0, 0.0], [1.0, 0.0]) == pytest.approx(1.0)


def test_cosine_vektor_tegak_lurus():
    assert main.cosine_similarity([1.0, 0.0], [0.0, 1.0]) == pytest.approx(0.0)


def test_cosine_tidak_terpengaruh_panjang_vektor():
    assert main.cosine_similarity([2.0, 0.0], [7.0, 0.0]) == pytest.approx(1.0)


# ── TODO 1 ───────────────────────────────────────────────────
@butuh_server
def test_embedding_mengembalikan_vektor():
    v = main.embedding("halo dunia")
    assert isinstance(v, list) and len(v) > 100
    assert all(isinstance(x, float) for x in v[:5])


# ── TODO 3 ───────────────────────────────────────────────────
@butuh_server
def test_cari_terurut_dan_sebanyak_k():
    hasil = main.cari("cara membuat chatbot", main.DOKUMEN, k=3)
    assert len(hasil) == 3
    skor = [s for s, _ in hasil]
    assert skor == sorted(skor, reverse=True)
    assert "chatbot" in hasil[0][1]  # dokumen pertemuan 07 harus paling relevan
