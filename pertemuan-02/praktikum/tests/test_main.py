"""Uji jawaban praktikum pertemuan 02. Jalankan dari folder praktikum/:  pytest -q"""
import pytest
import requests

import main


def _server_tersedia() -> bool:
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


# ── TODO 1: hitung_token (murni) ─────────────────────────────
def test_hitung_token_teks_kosong():
    assert main.hitung_token("") == 0


def test_hitung_token_teks_panjang_lebih_banyak():
    pendek = main.hitung_token("Halo")
    panjang = main.hitung_token(
        "Halo semuanya, selamat datang di praktikum prompt engineering hari ini"
    )
    assert pendek >= 1
    assert panjang > pendek


# ── TODO 4: buat_prompt_few_shot (murni) ─────────────────────
def test_buat_prompt_few_shot_format():
    contoh = [("apel", "buah"), ("bayam", "sayur")]
    hasil = main.buat_prompt_few_shot(contoh, "mangga")
    assert "apel => buah" in hasil
    assert "bayam => sayur" in hasil
    assert hasil.rstrip().endswith("mangga =>")


def test_buat_prompt_few_shot_urutan():
    contoh = [("a", "1"), ("b", "2")]
    hasil = main.buat_prompt_few_shot(contoh, "c")
    assert hasil.index("a => 1") < hasil.index("b => 2") < hasil.index("c =>")


# ── TODO 5: prompt_cot (murni) ───────────────────────────────
def test_prompt_cot_memuat_soal_dan_instruksi():
    p = main.prompt_cot("Berapa 2+3?")
    assert "Berapa 2+3?" in p
    assert "langkah demi langkah" in p.lower()
    assert "JAWABAN" in p


# ── TODO 7: prompt_refine (murni) ────────────────────────────
def test_prompt_refine_memuat_kedua_bagian():
    p = main.prompt_refine("jawaban lama", "tugas awal xyz")
    assert "jawaban lama" in p
    assert "tugas awal xyz" in p
    assert "kritik" in p.lower() or "perbaik" in p.lower()


# ── TODO 2: generate ─────────────────────────────────────────
@butuh_server
def test_generate_mengembalikan_teks():
    jawaban = _panggil_server(
        main.generate, "Sebutkan satu nama warna. Jawab satu kata saja."
    )
    assert isinstance(jawaban, str)
    assert jawaban.strip() != ""


@butuh_server
def test_generate_dengan_temperature():
    j = _panggil_server(
        main.generate, "Sebutkan satu buah. Jawab satu kata.", temperature=0.2
    )
    assert isinstance(j, str) and j.strip()


# ── TODO 3: chat ─────────────────────────────────────────────
@butuh_server
def test_chat_mengembalikan_teks():
    pesan = [
        {"role": "system", "content": "Jawab singkat dalam bahasa Indonesia."},
        {"role": "user", "content": "Apa ibu kota Indonesia?"},
    ]
    jawaban = _panggil_server(main.chat, pesan)
    assert isinstance(jawaban, str)
    assert jawaban.strip() != ""


# ── TODO 6: self_consistency (logika diuji TANPA server) ─────
def test_self_consistency_jumlah_jawaban(monkeypatch):
    panggilan = []

    def generate_palsu(prompt, temperature=None):
        panggilan.append(prompt)
        return f"JAWABAN: {len(panggilan)}"

    monkeypatch.setattr(main, "generate", generate_palsu)
    hasil = main.self_consistency("Berapa 4+4? Jawab angka saja.", n=3)
    assert isinstance(hasil, list) and len(hasil) == 3
    assert all(isinstance(j, str) and j.strip() for j in hasil)
    assert len(panggilan) == 3, "generate harus dipanggil sebanyak n kali"
