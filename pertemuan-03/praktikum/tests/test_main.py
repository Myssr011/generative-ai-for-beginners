"""Uji jawaban praktikum pertemuan 03. Jalankan dari folder praktikum/:  pytest -q"""
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


# ── TODO 1: buat_prompt_resep (murni) ────────────────────────
def test_prompt_resep_memuat_semua_unsur():
    p = main.buat_prompt_resep(3, ["telur", "tahu"], "asin")
    assert "3" in p
    assert "telur" in p and "tahu" in p
    assert "asin" in p


# ── TODO 3: buat_prompt_belanja (murni) ──────────────────────
def test_prompt_belanja_memuat_resep_dan_bahan():
    p = main.buat_prompt_belanja("Resep opor spesial", ["ayam", "garam"])
    assert "Resep opor spesial" in p
    assert "ayam" in p and "garam" in p
    assert "beli" in p.lower() or "belanja" in p.lower()


# ── TODO 5: tambah_pesan (murni) ─────────────────────────────
def test_tambah_pesan_menambah_di_akhir():
    r = main.tambah_pesan([], "user", "halo")
    assert r == [{"role": "user", "content": "halo"}]


def test_tambah_pesan_tidak_mengubah_asli():
    asli = [{"role": "system", "content": "s"}]
    baru = main.tambah_pesan(asli, "user", "hai")
    assert len(asli) == 1, "list asli tidak boleh berubah (jangan pakai .append)"
    assert len(baru) == 2


# ── TODO 6: potong_riwayat (murni) ───────────────────────────
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


# ── TODO 2: generate ─────────────────────────────────────────
@butuh_server
def test_generate_mengembalikan_teks():
    j = _panggil_server(main.generate, "Sebutkan satu nama sayur. Jawab satu kata.")
    assert isinstance(j, str) and j.strip()


# ── TODO 4: chat ─────────────────────────────────────────────
@butuh_server
def test_chat_mengembalikan_teks():
    j = _panggil_server(
        main.chat,
        [
            {"role": "system", "content": "Jawab singkat."},
            {"role": "user", "content": "Apa ibu kota Indonesia?"},
        ],
    )
    assert isinstance(j, str) and j.strip()
