"""Uji jawaban praktikum 07. Jalankan dari folder praktikum/:  pytest -q"""
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
def test_tambah_pesan_menambah_di_akhir():
    r = main.tambah_pesan([], "user", "halo")
    assert r == [{"role": "user", "content": "halo"}]


def test_tambah_pesan_tidak_mengubah_asli():
    asli = [{"role": "system", "content": "s"}]
    baru = main.tambah_pesan(asli, "user", "hai")
    assert len(asli) == 1, "list asli tidak boleh berubah (jangan pakai .append)"
    assert len(baru) == 2


# ── TODO 3 (murni) ───────────────────────────────────────────
def test_potong_riwayat_pertahankan_system():
    riwayat = [{"role": "system", "content": "s"}] + [
        {"role": "user", "content": f"p{i}"} for i in range(1, 8)
    ]
    hasil = main.potong_riwayat(riwayat, maks=4)
    assert len(hasil) == 4
    assert hasil[0]["role"] == "system"
    assert [p["content"] for p in hasil[1:]] == ["p5", "p6", "p7"]


def test_potong_riwayat_tidak_perlu_dipotong():
    riwayat = [{"role": "system", "content": "s"}, {"role": "user", "content": "a"}]
    assert main.potong_riwayat(riwayat, maks=5) == riwayat


# ── TODO 1 ───────────────────────────────────────────────────
@butuh_server
def test_chat_mengembalikan_teks():
    j = main.chat(
        [
            {"role": "system", "content": "Jawab singkat."},
            {"role": "user", "content": "Apa ibu kota Indonesia?"},
        ]
    )
    assert isinstance(j, str) and j.strip()
