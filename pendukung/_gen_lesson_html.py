# Convert setiap file .md di folder pelajaran (00-21) menjadi .html
# agar materi bisa dibaca langsung di browser.
# Sumber: terjemahan bahasa Indonesia di translations/id, output ke folder pertemuan utama.
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
SOURCE = ROOT / "translations" / "id"

TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 2rem 1.5rem;
    color: #1f2328; background: #ffffff;
  }}
  h1, h2, h3, h4 {{ line-height: 1.25; margin-top: 1.8em; }}
  h1 {{ border-bottom: 1px solid #d1d9e0; padding-bottom: .3em; }}
  h2 {{ border-bottom: 1px solid #d1d9e0; padding-bottom: .3em; }}
  a {{ color: #0969da; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  img {{ max-width: 100%; height: auto; }}
  pre {{
    background: #f6f8fa; padding: 1em; overflow-x: auto;
    border-radius: 6px; font-size: 85%;
  }}
  code {{
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
    background: #f6f8fa; padding: .2em .4em; border-radius: 4px; font-size: 85%;
  }}
  pre code {{ background: none; padding: 0; }}
  table {{ border-collapse: collapse; display: block; overflow-x: auto; }}
  th, td {{ border: 1px solid #d1d9e0; padding: 6px 13px; }}
  th {{ background: #f6f8fa; }}
  blockquote {{
    border-left: 4px solid #d1d9e0; margin: 0; padding: 0 1em; color: #59636e;
  }}
  hr {{ border: none; border-top: 1px solid #d1d9e0; margin: 2em 0; }}
  @media (prefers-color-scheme: dark) {{
    body {{ color: #e6edf3; background: #0d1117; }}
    h1, h2 {{ border-color: #30363d; }}
    a {{ color: #4493f8; }}
    pre, code, th {{ background: #161b22; }}
    th, td {{ border-color: #30363d; }}
    blockquote {{ border-color: #30363d; color: #9198a1; }}
    hr {{ border-color: #30363d; }}
  }}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def first_heading(md_text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    return re.sub(r"[#*`\[\]]", "", m.group(1)).strip() if m else fallback


# Banner video: [![alt](gambar)](link-youtube)
BANNER_RE = re.compile(
    r"\[!\[[^\]]*\]\([^)]*\)\]\((https?://(?:www\.)?(?:youtu\.be|youtube\.com)[^)]*)\)"
)
# Baris keterangan di bawah banner, mis. "> _Klik gambar di atas untuk menonton video_"
CAPTION_RE = re.compile(r"^>.*video.*$\n?", re.IGNORECASE | re.MULTILINE)


def ambil_dan_hapus_video(text: str):
    """Kembalikan (teks tanpa banner video, url video pertama atau None)."""
    m = BANNER_RE.search(text)
    if not m:
        return text, None
    url = m.group(1)
    text = BANNER_RE.sub("", text)
    text = CAPTION_RE.sub("", text)
    return text, url


def md_links_to_html(html: str) -> str:
    # Arahkan tautan relatif .md ke versi .html agar navigasi antar file tetap jalan
    def repl(m):
        href = m.group(1)
        if href.startswith(("http://", "https://")):
            return m.group(0)
        new = re.sub(r"\.md(?=$|[?#])", ".html", href, count=1)
        return f'href="{new}"'

    return re.sub(r'href="([^"]+\.md(?:[?#][^"]*)?)"', repl, html)


def convert(md_file: Path, out_dir: Path):
    text = md_file.read_text(encoding="utf-8")
    # Path relatif dari translations/id/<lesson>/ disesuaikan ke <lesson>/ di root
    text = text.replace("../../../", "../")
    text, video_url = ambil_dan_hapus_video(text)
    body = markdown.markdown(
        text, extensions=["extra", "toc", "sane_lists", "nl2br"]
    )
    body = md_links_to_html(body)
    title = first_heading(text, md_file.stem)
    out = out_dir / (md_file.stem + ".html")
    out.write_text(TEMPLATE.format(title=title, body=body), encoding="utf-8")
    return out, title, video_url


def youtube_embed(url: str):
    m = re.search(r"(?:youtu\.be/|[?&]v=)([\w-]{6,})", url)
    return f"https://www.youtube.com/embed/{m.group(1)}" if m else None


def tulis_daftar_video(video_list):
    """Tulis DAFTAR-VIDEO.md dan DAFTAR-VIDEO.html di root repo."""
    baris_md = [
        "# Daftar Video Pertemuan",
        "",
        "Kumpulan video dari seluruh pertemuan. Banner video tidak lagi",
        "ditampilkan di halaman materi tiap pertemuan \u2014 semuanya ada di sini.",
        "",
        "| Pertemuan | Materi | Video |",
        "| :-- | :-- | :-- |",
    ]
    kartu = []
    for folder, judul, url in video_list:
        link = f"[\u25b6 Tonton]({url})" if url else "\u2014"
        baris_md.append(f"| {folder[:2]} | [{judul}](./{folder}/README.md) | {link} |")
        if url:
            embed = youtube_embed(url)
            player = (
                f'<iframe src="{embed}" title="{judul}" loading="lazy" allowfullscreen></iframe>'
                if embed
                else f'<p><a href="{url}">\u25b6 Tonton di YouTube</a></p>'
            )
            kartu.append(
                f'<div class="kartu"><h2>{folder[:2]} \u2014 <a href="./{folder}/README.html">{judul}</a></h2>{player}</div>'
            )
    (ROOT / "DAFTAR-VIDEO.md").write_text("\n".join(baris_md) + "\n", encoding="utf-8")

    body = (
        "<h1>Daftar Video Pertemuan</h1>\n"
        "<p>Semua video pembelajaran dikumpulkan di halaman ini. "
        "Klik judul untuk membuka materi pertemuannya.</p>\n"
        "<style>.kartu{margin:2rem 0}.kartu iframe{width:100%;aspect-ratio:16/9;border:0;border-radius:10px}</style>\n"
        + "\n".join(kartu)
    )
    (ROOT / "DAFTAR-VIDEO.html").write_text(
        TEMPLATE.format(title="Daftar Video Pertemuan", body=body), encoding="utf-8"
    )


def main():
    lesson_dirs = sorted(
        d for d in SOURCE.iterdir() if d.is_dir() and re.match(r"^\d{2}-", d.name)
    )
    total = 0
    video_list = []
    for d in lesson_dirs:
        out_dir = ROOT / d.name
        for md_file in sorted(d.glob("*.md")):
            out, title, video_url = convert(md_file, out_dir)
            if md_file.name == "README.md":
                video_list.append((d.name, title, video_url))
            print(f"  {out.relative_to(ROOT)}")
            total += 1
    tulis_daftar_video(video_list)
    n_video = sum(1 for _, _, u in video_list if u)
    print(f"\nSelesai: {total} file HTML dibuat di {len(lesson_dirs)} folder pertemuan.")
    print(f"Daftar video: {n_video} video dikumpulkan di DAFTAR-VIDEO.md / DAFTAR-VIDEO.html")


if __name__ == "__main__":
    main()
