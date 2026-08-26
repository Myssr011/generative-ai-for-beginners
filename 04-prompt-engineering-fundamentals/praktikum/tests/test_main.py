"""Uji jawaban praktikum. Jalankan dari folder praktikum/:  pytest -q"""
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


# ── TODO 1: hitung_token ─────────────────────────────────────
def test_hitung_token_teks_kosong():
    assert main.hitung_token("") == 0


def test_hitung_token_teks_panjang_lebih_banyak():
    pendek = main.hitung_token("Halo")
    panjang = main.hitung_token(
        "Halo semuanya, selamat datang di praktikum prompt engineering hari ini"
    )
    assert pendek >= 1
    assert panjang > pendek


# ── TODO 4: buat_prompt_few_shot (fungsi murni, tanpa server) ─
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


# ── TODO 2: generate ─────────────────────────────────────────
@butuh_server
def test_generate_mengembalikan_teks():
    jawaban = main.generate("Sebutkan satu nama warna. Jawab satu kata saja.")
    assert isinstance(jawaban, str)
    assert jawaban.strip() != ""


# ── TODO 3: chat ─────────────────────────────────────────────
@butuh_server
def test_chat_mengembalikan_teks():
    pesan = [
        {"role": "system", "content": "Jawab singkat dalam bahasa Indonesia."},
        {"role": "user", "content": "Apa ibu kota Indonesia?"},
    ]
    jawaban = main.chat(pesan)
    assert isinstance(jawaban, str)
    assert jawaban.strip() != ""
