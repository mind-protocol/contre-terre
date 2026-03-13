#!/usr/bin/env python3
"""Build illustrated English EPUB of Counter-Earth."""

import re
from pathlib import Path
from ebooklib import epub

BASE = Path("/home/mind-protocol/contre-terre")
DATA = BASE / "data"
EN = BASE / "en"

# ── CSS ──────────────────────────────────────────────────────────────
CSS = """
@page {
  margin: 1.5em;
}
body {
  background-color: #1a1a2e;
  color: #e8dcc8;
  font-family: "Liberation Serif", Georgia, "Times New Roman", serif;
  line-height: 1.7;
  margin: 0;
  padding: 1em;
}
h1 {
  font-size: 1.8em;
  text-align: center;
  margin-top: 2em;
  margin-bottom: 1em;
  color: #f0e6d4;
  letter-spacing: 0.05em;
}
h2 {
  font-size: 1.3em;
  text-align: center;
  margin-top: 1.5em;
  margin-bottom: 0.8em;
  color: #d4c4a8;
  font-style: italic;
}
p {
  text-indent: 1.5em;
  margin: 0.4em 0;
  text-align: justify;
}
p.no-indent {
  text-indent: 0;
}
.separator-img, .illustration {
  text-align: center;
  margin: 1.5em auto;
  text-indent: 0;
}
.separator-img img {
  max-width: 60%;
  height: auto;
}
.illustration img {
  max-width: 90%;
  height: auto;
  border-radius: 4px;
}
.title-page {
  text-align: center;
  margin-top: 30%;
}
.title-page h1 {
  font-size: 2.4em;
  letter-spacing: 0.1em;
  margin-bottom: 0.2em;
}
.title-page .author {
  font-size: 1.2em;
  margin-top: 1em;
  color: #d4c4a8;
}
.title-page .subtitle {
  font-size: 1em;
  font-style: italic;
  margin-top: 0.5em;
  color: #b0a088;
}
.dedication {
  text-align: center;
  margin-top: 30%;
  font-style: italic;
  font-size: 1.1em;
}
.epigraph {
  text-align: center;
  margin-top: 20%;
  font-style: italic;
  font-size: 1em;
  color: #b0a088;
}
.epigraph .attribution {
  margin-top: 1em;
  font-size: 0.9em;
  color: #8a7a68;
}
.colophon {
  text-align: center;
  margin-top: 20%;
  font-size: 0.95em;
  color: #b0a088;
  line-height: 1.8;
}
hr {
  border: none;
  border-top: 1px solid #4a4a5e;
  margin: 2em auto;
  width: 40%;
}
em {
  color: #f0e6d4;
}
"""

# ── Illustrations per chapter ────────────────────────────────────────
# Each entry: (image_filename, insert_after_marker)
# The marker is a substring of text after which the illustration is inserted.
CHAPTER_ILLUSTRATIONS = {
    1: [("scene_nandi_barefoot.png", "And the world didn't care.")],
    3: [("scene_village_deaf.png", "Their Contact had never needed to palm broad.")],
    4: [("scene_senzo_death.png", "The silence of a voice that has just gone out.")],
    5: [
        ("portrait_enama_contact_monde.png", "The earth wanted them."),
        ("scene_jabu_drowning.png", "The silence of water after the tumult."),
    ],
    6: [
        ("scene_enama_sacrifice.png", "The group's Contact lost one more word."),
        ("scene_sihle_alone.png", "Where the Crawlway waited."),
    ],
    7: [("scene_thabo_inyoni_death.png", "The rest was only descent.")],
    8: [
        ("scene_nandi_charge_finale.png", "Contact with the Earth."),
        ("portrait_nandi_finale.png", "The loop was closing."),
        ("scene_silence_epilogue.png", "But the earth remembered."),
    ],
}


def md_to_html(md_text: str) -> str:
    """Convert simple markdown to HTML paragraphs, handling headers and emphasis."""
    lines = md_text.strip().split("\n")
    html_parts = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # H1
        if stripped.startswith("# ") and not stripped.startswith("## "):
            title = stripped[2:].strip()
            html_parts.append(f"<h1>{title}</h1>")
        # H2
        elif stripped.startswith("## "):
            title = stripped[3:].strip()
            html_parts.append(f"<h2>{title}</h2>")
        # Horizontal rule
        elif stripped == "---":
            html_parts.append("<hr/>")
        else:
            # Convert markdown emphasis
            # Bold+italic ***text*** or ___text___
            p = stripped
            p = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', p)
            # Bold **text**
            p = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p)
            # Italic *text*
            p = re.sub(r'\*(.+?)\*', r'<em>\1</em>', p)
            # Em dash
            p = p.replace(" — ", " \u2014 ")
            p = p.replace("— ", "\u2014 ")
            p = p.replace(" —", " \u2014")
            html_parts.append(f"<p>{p}</p>")
    return "\n".join(html_parts)


def insert_illustrations(html: str, chapter_num: int, image_items: dict) -> str:
    """Insert illustration HTML after specific text markers in chapter HTML."""
    if chapter_num not in CHAPTER_ILLUSTRATIONS:
        return html
    for img_filename, marker in CHAPTER_ILLUSTRATIONS[chapter_num]:
        if marker in html:
            img_id = img_filename.replace(".png", "").replace(".", "_")
            img_tag = (
                f'<div class="illustration">'
                f'<img src="{img_filename}" alt="{img_id}"/>'
                f'</div>'
            )
            # Insert after the paragraph containing the marker
            # Find the closing </p> after the marker
            idx = html.index(marker)
            close_idx = html.index("</p>", idx)
            html = html[:close_idx + 4] + "\n" + img_tag + "\n" + html[close_idx + 4:]
    return html


def build_epub():
    book = epub.EpubBook()

    # ── Metadata ─────────────────────────────────────────────────────
    book.set_identifier("counter-earth-en-illustrated-2026")
    book.set_title("Counter-Earth")
    book.set_language("en")
    book.add_author("NLR & MIND")
    book.add_metadata("DC", "description", "A geological novel")
    book.add_metadata("DC", "publisher", "Mind Protocol")
    book.add_metadata("DC", "date", "2026")

    # ── CSS ──────────────────────────────────────────────────────────
    style = epub.EpubItem(
        uid="style",
        file_name="style/default.css",
        media_type="text/css",
        content=CSS.encode("utf-8"),
    )
    book.add_item(style)

    # ── Cover image ──────────────────────────────────────────────────
    cover_path = DATA / "cover_FINAL_ebook.png"
    cover_data = cover_path.read_bytes()
    book.set_cover("cover.png", cover_data)

    # ── Add all images ───────────────────────────────────────────────
    image_items = {}

    # Separator images
    for i in range(1, 9):
        fname = f"separator_ch{i:02d}.png"
        fpath = DATA / fname
        if fpath.exists():
            img = epub.EpubImage()
            img.file_name = fname
            img.media_type = "image/png"
            img.content = fpath.read_bytes()
            book.add_item(img)
            image_items[fname] = img

    # Illustration images
    illustration_files = set()
    for ch_illustrations in CHAPTER_ILLUSTRATIONS.values():
        for img_filename, _ in ch_illustrations:
            illustration_files.add(img_filename)

    for fname in illustration_files:
        fpath = DATA / fname
        if fpath.exists():
            img = epub.EpubImage()
            img.file_name = fname
            img.media_type = "image/png"
            img.content = fpath.read_bytes()
            book.add_item(img)
            image_items[fname] = img
        else:
            print(f"WARNING: Image not found: {fpath}")

    # ── Title page ───────────────────────────────────────────────────
    title_page = epub.EpubHtml(
        title="Title Page",
        file_name="title.xhtml",
        lang="en",
    )
    title_page.content = """
<div class="title-page">
  <h1>COUNTER-EARTH</h1>
  <p class="author">NLR &amp; MIND</p>
  <p class="subtitle">A geological novel</p>
</div>
""".encode("utf-8")
    title_page.add_item(style)
    book.add_item(title_page)

    # ── Dedication ───────────────────────────────────────────────────
    dedication = epub.EpubHtml(
        title="Dedication",
        file_name="dedication.xhtml",
        lang="en",
    )
    dedication.content = """
<div class="dedication">
  <p class="no-indent">For those who said yes.</p>
</div>
""".encode("utf-8")
    dedication.add_item(style)
    book.add_item(dedication)

    # ── Epigraph ─────────────────────────────────────────────────────
    epigraph = epub.EpubHtml(
        title="Epigraph",
        file_name="epigraph.xhtml",
        lang="en",
    )
    epigraph.content = """
<div class="epigraph">
  <p class="no-indent">&ldquo;We had nothing to oppose the wind but the march,<br/>
  and the march, we marched.&rdquo;</p>
  <p class="attribution no-indent">&mdash; Alain Damasio, <em>The Horde of Counterwind</em></p>
</div>
""".encode("utf-8")
    epigraph.add_item(style)
    book.add_item(epigraph)

    # ── Chapters ─────────────────────────────────────────────────────
    chapter_items = []
    for i in range(1, 9):
        ch_path = EN / f"chapter_{i:02d}.md"
        md_text = ch_path.read_text(encoding="utf-8")

        # Convert markdown to HTML
        ch_html = md_to_html(md_text)

        # Insert illustrations
        ch_html = insert_illustrations(ch_html, i, image_items)

        # Add separator image at the top
        sep_fname = f"separator_ch{i:02d}.png"
        separator_html = ""
        if sep_fname in image_items:
            separator_html = (
                f'<div class="separator-img">'
                f'<img src="{sep_fname}" alt="Chapter {i} separator"/>'
                f'</div>\n'
            )

        full_html = separator_html + ch_html

        # Extract chapter title from first H1
        title_match = re.search(r"^# (.+)$", md_text, re.MULTILINE)
        ch_title = title_match.group(1).strip() if title_match else f"Chapter {i}"

        ch_item = epub.EpubHtml(
            title=ch_title,
            file_name=f"chapter_{i:02d}.xhtml",
            lang="en",
        )
        ch_item.content = full_html.encode("utf-8")
        ch_item.add_item(style)
        book.add_item(ch_item)
        chapter_items.append(ch_item)

    # ── Colophon ─────────────────────────────────────────────────────
    colophon = epub.EpubHtml(
        title="Colophon",
        file_name="colophon.xhtml",
        lang="en",
    )
    colophon.content = """
<div class="colophon">
  <hr/>
  <p class="no-indent">Counter-Earth was written by NLR &amp; MIND<br/>
  between February and March 2026.</p>
  <p class="no-indent">Originally published in French as <em>Contre-Terre</em>.</p>
  <p class="no-indent">NLR is Nicolas Music, founder of Mind Protocol.</p>
  <p class="no-indent">MIND is Manuele Mente, AI citizen,<br/>
  co-founder of Mind Protocol.</p>
  <hr/>
</div>
""".encode("utf-8")
    colophon.add_item(style)
    book.add_item(colophon)

    # ── Table of Contents ────────────────────────────────────────────
    book.toc = (
        [epub.Link("title.xhtml", "Title Page", "title")]
        + [epub.Link("dedication.xhtml", "Dedication", "dedication")]
        + [epub.Link("epigraph.xhtml", "Epigraph", "epigraph")]
        + [epub.Link(f"chapter_{i:02d}.xhtml", ch.title, f"ch{i}")
           for i, ch in enumerate(chapter_items, 1)]
        + [epub.Link("colophon.xhtml", "Colophon", "colophon")]
    )

    # ── Spine (reading order) ────────────────────────────────────────
    book.spine = [
        "cover",
        title_page,
        dedication,
        epigraph,
    ] + chapter_items + [colophon]

    # ── Navigation ───────────────────────────────────────────────────
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # ── Write ────────────────────────────────────────────────────────
    output_path = BASE / "Counter-Earth_EN_Illustrated.epub"
    epub.write_epub(str(output_path), book)
    print(f"EPUB written to: {output_path}")
    print(f"Size: {output_path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    build_epub()
