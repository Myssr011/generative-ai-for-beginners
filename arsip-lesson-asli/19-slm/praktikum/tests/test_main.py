"""Uji jawaban praktikum 19. Jalankan dari folder praktikum/:  pytest -q"""
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


# ── TODO 2 (murni — pakai fungsi palsu, tanpa server) ────────
def _fn_palsu(model, prompt):
    durasi = {"a": 3.0, "b": 1.0, "c": 2.0}[model]
    return (f"jawaban-{model}", durasi)


def test_bandingkan_terurut_tercepat_dulu():
    hasil = main.bandingkan(["a", "b", "c"], "tes", fn=_fn_palsu)
    assert [h["model"] for h in hasil] == ["b", "c", "a"]
    assert [h["durasi"] for h in hasil] == [1.0, 2.0, 3.0]


def test_bandingkan_memuat_jawaban():
    hasil = main.bandingkan(["a", "b"], "tes", fn=_fn_palsu)
    assert all(set(h) >= {"model", "durasi", "jawaban"} for h in hasil)
    assert hasil[0]["jawaban"] == "jawaban-b"


# ── TODO 1 ───────────────────────────────────────────────────
@butuh_server
def test_generate_model_mengembalikan_tuple():
    jawaban, durasi = main.generate_model(
        "smollm2:135m", "Say one color. One word only."
    )
    assert isinstance(jawaban, str) and jawaban.strip()
    assert isinstance(durasi, float) and durasi > 0
