"""Uji jawaban praktikum 11. Jalankan dari folder praktikum/:  pytest -q"""
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
def test_definisi_tools_format():
    tools = main.definisi_tools()
    assert isinstance(tools, list) and len(tools) == 1
    t = tools[0]
    assert t["type"] == "function"
    assert t["function"]["name"] == "get_jadwal_praktikum"
    assert "hari" in t["function"]["parameters"]["properties"]
    assert t["function"]["parameters"]["required"] == ["hari"]


# ── TODO 2 (murni) ───────────────────────────────────────────
def test_jalankan_tool_hari_ada():
    hasil = main.jalankan_tool("get_jadwal_praktikum", {"hari": "Rabu"})
    assert "Kecerdasan Buatan" in hasil


def test_jalankan_tool_hari_kosong():
    hasil = main.jalankan_tool("get_jadwal_praktikum", {"hari": "minggu"})
    assert "tidak ada" in hasil.lower()


def test_jalankan_tool_tidak_dikenal():
    hasil = main.jalankan_tool("tool_asing", {})
    assert "tidak dikenal" in hasil.lower()


# ── TODO 3 ───────────────────────────────────────────────────
@butuh_server
def test_chat_dengan_tools_mengembalikan_dict_message():
    pesan = main.chat_dengan_tools(
        [{"role": "user", "content": "Praktikum apa hari senin?"}]
    )
    assert isinstance(pesan, dict)
    assert "content" in pesan or "tool_calls" in pesan
