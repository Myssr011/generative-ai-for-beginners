"""Uji jawaban praktikum pertemuan 06. Jalankan dari folder praktikum/:  pytest -q"""
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


def _panggil_server(fn, *args, **kwargs):
    """Jalankan fungsi ber-server; skip (bukan gagal) bila server sibuk/timeout."""
    try:
        return fn(*args, **kwargs)
    except requests.RequestException:
        pytest.skip("server AI kampus sibuk/timeout — jalankan ulang nanti")


# ── TODO 1 (murni) ───────────────────────────────────────────
def test_potong_dokumen_per_paragraf():
    teks = "Paragraf satu.\n\nParagraf dua.\n\n\n\nParagraf tiga."
    hasil = main.potong_dokumen(teks)
    assert hasil == ["Paragraf satu.", "Paragraf dua.", "Paragraf tiga."]


def test_potong_dokumen_file_asli():
    potongan = main.potong_dokumen(main.DATA.read_text(encoding="utf-8"))
    assert len(potongan) >= 5
    assert all(p.strip() for p in potongan)


# ── TODO 4 (murni) ───────────────────────────────────────────
def test_buat_prompt_rag_memuat_konteks_dan_query():
    p = main.buat_prompt_rag("kapan lab buka?", ["Lab buka Senin.", "Lab tutup Minggu."])
    assert "Lab buka Senin." in p
    assert "Lab tutup Minggu." in p
    assert "kapan lab buka?" in p
    assert "konteks" in p.lower()


# ── TODO 2 ───────────────────────────────────────────────────
@butuh_server
def test_embedding_mengembalikan_vektor():
    v = _panggil_server(main.embedding, "halo dunia")
    assert isinstance(v, list) and len(v) > 100


# ── TODO 3 ───────────────────────────────────────────────────
@butuh_server
def test_ambil_konteks_relevan():
    potongan = main.potong_dokumen(main.DATA.read_text(encoding="utf-8"))
    hasil = _panggil_server(
        main.ambil_konteks, "jam operasional laboratorium hari sabtu", potongan, k=2
    )
    assert len(hasil) == 2
    assert any("07.30" in h or "Sabtu" in h for h in hasil)
