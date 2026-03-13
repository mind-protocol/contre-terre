#!/usr/bin/env python3
"""
Generate illustrated French EPUB of Contre-Terre.
"""

import re
import os
from ebooklib import epub

BASE = "/home/mind-protocol/contre-terre"
DATA = os.path.join(BASE, "data")
MANUSCRIPT = os.path.join(BASE, "manuscrit_complet.md")
OUTPUT = os.path.join(BASE, "Contre-Terre_FR_Illustrated.epub")

# CSS
STYLE_CSS = """
@page {
    margin: 1.5em;
}
body {
    background-color: #1a1a2e;
    color: #e8dcc8;
    font-family: "Liberation Serif", Georgia, "Times New Roman", serif;
    line-height: 1.7;
    margin: 0;
    padding: 1em 1.5em;
}
h1 {
    font-size: 1.8em;
    text-align: center;
    margin-top: 2em;
    margin-bottom: 1em;
    color: #e8dcc8;
    letter-spacing: 0.05em;
}
h2 {
    font-size: 1.3em;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
    color: #e8dcc8;
}
p {
    text-indent: 1.5em;
    margin: 0.4em 0;
    text-align: justify;
}
em {
    font-style: italic;
}
strong {
    font-weight: bold;
}
hr {
    border: none;
    border-top: 1px solid #555;
    margin: 2em auto;
    width: 40%;
}
img {
    display: block;
    margin: 1.5em auto;
    max-width: 90%;
    height: auto;
}
img.separator {
    max-width: 60%;
    margin: 2em auto;
}
img.cover {
    max-width: 100%;
    margin: 0;
}
.title-page {
    text-align: center;
    padding-top: 30%;
}
.title-page h1 {
    font-size: 2.5em;
    margin-bottom: 0.3em;
    letter-spacing: 0.1em;
}
.title-page .author {
    font-size: 1.2em;
    margin-top: 1em;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}
.title-page .subtitle {
    font-size: 1em;
    margin-top: 1.5em;
    font-style: italic;
    color: #b0a890;
}
.dedication {
    text-align: center;
    padding-top: 30%;
    font-style: italic;
    font-size: 1.1em;
}
.epigraph {
    text-align: center;
    padding-top: 20%;
    font-style: italic;
    font-size: 0.95em;
    color: #b0a890;
    max-width: 80%;
    margin: 0 auto;
}
.epigraph .attribution {
    margin-top: 1em;
    font-size: 0.85em;
}
.colophon {
    text-align: center;
    padding-top: 20%;
    font-size: 0.9em;
    color: #b0a890;
}
.colophon p {
    text-indent: 0;
    text-align: center;
}
"""

# Chapter titles from the manuscript
CHAPTER_TITLES = {
    1: "I \u2014 Surface du D\u00e9sert",
    2: "II \u2014 Zones Interm\u00e9diaires",
    3: "III \u2014 Le Dernier Village",
    4: "IV \u2014 La Faille",
    5: "V \u2014 Les Cavernes Profondes",
    6: "VI \u2014 Les Zones Volcaniques",
    7: "VII \u2014 L\u2019Int\u00e9rieur du Volcan",
    8: "VIII \u2014 La Grotte Finale",
}

# Illustrations config: chapter -> list of (marker_type, marker_key, image_file, alt_text)
# marker_type: "after_text" = insert after paragraph containing text
#              "after_heading" = insert after h2 heading containing text
ILLUSTRATIONS = {
    1: [
        ("after_text", "fichait", "scene_nandi_barefoot.png",
         "Nandi marche pieds nus dans le desert"),
    ],
    3: [
        ("after_heading", "apprentissage", "scene_village_deaf.png",
         "Le Village des Sourds"),
    ],
    4: [
        ("after_heading", "premier deuil", "scene_senzo_death.png",
         "La mort de Senzo"),
    ],
    5: [
        ("after_heading", "choix de la route", "portrait_enama_contact_monde.png",
         "Enama et le Contact-monde"),
        ("after_heading", "Mort de Jabu", "scene_jabu_drowning.png",
         "La noyade de Jabu"),
    ],
    6: [
        ("after_heading", "sacrifice", "scene_enama_sacrifice.png",
         "Le sacrifice d'Enama"),
        ("after_heading_last", "Enama", "scene_sihle_alone.png",
         "Sihle seul"),  # Matches "Après Enama" (last h2 with "Enama")
    ],
    7: [
        ("after_heading", "mort partag", "scene_thabo_inyoni_death.png",
         "La mort de Thabo et Inyoni"),
    ],
    8: [
        ("after_heading", "tonateur", "scene_nandi_charge_finale.png",
         "Nandi et la Charge"),
        ("after_heading", "tonation", "portrait_nandi_finale.png",
         "Nandi - finale"),
        ("after_heading", "pilogue", "scene_silence_epilogue.png",
         "Le silence - epilogue"),
    ],
}


def read_manuscript():
    with open(MANUSCRIPT, "r", encoding="utf-8") as f:
        return f.read()


def split_chapters(text):
    """Split manuscript into chapters based on '# I —', '# II —', etc."""
    # Pattern matches chapter headings like "# I — Surface du Désert"
    pattern = r'^(# [IVX]+ \u2014 .+)$'

    lines = text.split('\n')
    chapters = []
    current_title = None
    current_lines = []

    for line in lines:
        if re.match(pattern, line):
            if current_title is not None:
                chapters.append((current_title, '\n'.join(current_lines)))
            current_title = line.lstrip('# ').strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        chapters.append((current_title, '\n'.join(current_lines)))

    return chapters


def md_to_html(md_text):
    """Convert markdown to HTML, handling the specific patterns in the manuscript."""
    # Process line by line for better control
    lines = md_text.strip().split('\n')
    html_parts = []
    in_paragraph = False

    for line in lines:
        stripped = line.strip()

        # Horizontal rule
        if stripped == '---':
            if in_paragraph:
                html_parts.append('</p>')
                in_paragraph = False
            html_parts.append('<hr/>')
            continue

        # Scene headings (## Scène ...)
        if stripped.startswith('## '):
            if in_paragraph:
                html_parts.append('</p>')
                in_paragraph = False
            heading_text = stripped[3:]
            html_parts.append(f'<h2>{heading_text}</h2>')
            continue

        # Empty line
        if not stripped:
            if in_paragraph:
                html_parts.append('</p>')
                in_paragraph = False
            continue

        # Regular text - handle inline markdown
        text = stripped
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)

        if not in_paragraph:
            html_parts.append(f'<p>{text}')
            in_paragraph = True
        else:
            # Continue paragraph (shouldn't normally happen with blank line separation)
            html_parts[-1] += f' {text}'

    if in_paragraph:
        html_parts.append('</p>')

    return '\n'.join(html_parts)


def add_image(book, filename):
    """Add an image to the book and return the epub image item."""
    filepath = os.path.join(DATA, filename)
    if not os.path.exists(filepath):
        print(f"WARNING: Image not found: {filepath}")
        return None

    with open(filepath, 'rb') as f:
        content = f.read()

    # Determine media type
    ext = filename.lower().split('.')[-1]
    media_type = f'image/{ext}'
    if ext == 'jpg':
        media_type = 'image/jpeg'

    img = epub.EpubImage()
    img.file_name = f'images/{filename}'
    img.media_type = media_type
    img.content = content
    book.add_item(img)
    return img


def insert_illustrations(html_content, chapter_num):
    """Insert illustration images at appropriate points in chapter HTML."""
    if chapter_num not in ILLUSTRATIONS:
        return html_content

    for entry in ILLUSTRATIONS[chapter_num]:
        marker_type, marker_key, img_file, alt_text = entry
        img_tag = f'<img src="images/{img_file}" alt="{alt_text}"/>'

        if marker_type in ("after_heading", "after_heading_last"):
            # Find h2 containing the marker_key text
            pattern_h2 = re.compile(
                r'(<h2>[^<]*' + re.escape(marker_key) + r'[^<]*</h2>)',
                re.IGNORECASE
            )
            matches = list(pattern_h2.finditer(html_content))
            if matches:
                # Use last match for "after_heading_last", first otherwise
                match = matches[-1] if marker_type == "after_heading_last" else matches[0]
                insert_pos = match.end()
                html_content = html_content[:insert_pos] + '\n' + img_tag + '\n' + html_content[insert_pos:]
                print(f"  Inserted {img_file} after heading containing '{marker_key}'")
            else:
                print(f"  WARNING: No h2 containing '{marker_key}' in chapter {chapter_num}")

        elif marker_type == "after_text":
            # Find the text in the HTML and insert after the containing </p>
            idx = html_content.find(marker_key)
            if idx >= 0:
                next_p_end = html_content.find('</p>', idx)
                if next_p_end >= 0:
                    insert_pos = next_p_end + 4
                    html_content = html_content[:insert_pos] + '\n' + img_tag + '\n' + html_content[insert_pos:]
                    print(f"  Inserted {img_file} after text containing '{marker_key}'")
                else:
                    html_content += '\n' + img_tag
                    print(f"  Inserted {img_file} at end (no </p> after '{marker_key}')")
            else:
                print(f"  WARNING: Text '{marker_key}' not found in chapter {chapter_num}")

    return html_content


def build_epub():
    book = epub.EpubBook()

    # Metadata
    book.set_identifier('contre-terre-nlr-mind-2026')
    book.set_title('Contre-Terre')
    book.set_language('fr')
    book.add_author('NLR & MIND')
    book.add_metadata('DC', 'description', 'Un roman g\u00e9ologique')
    book.add_metadata('DC', 'publisher', 'NLR & MIND')
    book.add_metadata('DC', 'date', '2026')

    # Add CSS
    style = epub.EpubItem(
        uid='style',
        file_name='style/default.css',
        media_type='text/css',
        content=STYLE_CSS.encode('utf-8')
    )
    book.add_item(style)

    # Cover image
    cover_path = os.path.join(DATA, 'cover_FINAL_ebook.png')
    with open(cover_path, 'rb') as f:
        cover_content = f.read()
    book.set_cover('images/cover.png', cover_content)

    # Add all illustration images to the book
    all_images = set()
    for ch_num in range(1, 9):
        all_images.add(f'separator_ch{ch_num:02d}.png')
    for ch_num, illus_list in ILLUSTRATIONS.items():
        for entry in illus_list:
            all_images.add(entry[2])  # img_file is at index 2

    for img_file in sorted(all_images):
        add_image(book, img_file)

    # Track spine and TOC
    spine = ['nav']
    toc = []
    chapters_list = []

    # --- Title page ---
    title_page = epub.EpubHtml(
        title='Page de titre',
        file_name='title.xhtml',
        lang='fr'
    )
    title_page.content = '''
<html xmlns="http://www.w3.org/1999/xhtml">
<head><link rel="stylesheet" href="style/default.css" type="text/css"/></head>
<body>
<div class="title-page">
<h1>CONTRE-TERRE</h1>
<p class="author">NLR &amp; MIND</p>
<p class="subtitle">Un roman g\u00e9ologique</p>
</div>
</body>
</html>
'''.encode('utf-8')
    title_page.add_item(style)
    book.add_item(title_page)
    spine.append(title_page)

    # --- Dedication ---
    dedication = epub.EpubHtml(
        title='D\u00e9dicace',
        file_name='dedication.xhtml',
        lang='fr'
    )
    dedication.content = '''
<html xmlns="http://www.w3.org/1999/xhtml">
<head><link rel="stylesheet" href="style/default.css" type="text/css"/></head>
<body>
<div class="dedication">
<p>\u00c0 ceux qui ont dit oui.</p>
</div>
</body>
</html>
'''.encode('utf-8')
    dedication.add_item(style)
    book.add_item(dedication)
    spine.append(dedication)

    # --- Epigraph ---
    epigraph = epub.EpubHtml(
        title='\u00c9pigraphe',
        file_name='epigraph.xhtml',
        lang='fr'
    )
    epigraph.content = '''
<html xmlns="http://www.w3.org/1999/xhtml">
<head><link rel="stylesheet" href="style/default.css" type="text/css"/></head>
<body>
<div class="epigraph">
<p>\u00ab\u00a0Nous n\u2019avions rien d\u2019autre \u00e0 opposer au vent que la marche, et la marche, nous marchions.\u00a0\u00bb</p>
<p class="attribution">\u2014 Alain Damasio, <em>La Horde du Contrevent</em></p>
</div>
</body>
</html>
'''.encode('utf-8')
    epigraph.add_item(style)
    book.add_item(epigraph)
    spine.append(epigraph)

    # --- Chapters ---
    manuscript = read_manuscript()
    chapters = split_chapters(manuscript)

    print(f"Found {len(chapters)} chapters")

    for i, (title, content) in enumerate(chapters):
        ch_num = i + 1
        print(f"Processing chapter {ch_num}: {title}")

        # Convert markdown to HTML
        html_body = md_to_html(content)

        # Insert illustrations
        html_body = insert_illustrations(html_body, ch_num)

        # Build separator image tag
        separator_file = f'separator_ch{ch_num:02d}.png'
        separator_tag = f'<img class="separator" src="images/{separator_file}" alt="Chapitre {ch_num}"/>'

        # Full chapter HTML
        chapter_html = f'''
<html xmlns="http://www.w3.org/1999/xhtml">
<head><link rel="stylesheet" href="style/default.css" type="text/css"/></head>
<body>
{separator_tag}
<h1>{title}</h1>
{html_body}
</body>
</html>
'''

        ch = epub.EpubHtml(
            title=title,
            file_name=f'chapter_{ch_num:02d}.xhtml',
            lang='fr'
        )
        ch.content = chapter_html.encode('utf-8')
        ch.add_item(style)
        book.add_item(ch)
        spine.append(ch)
        toc.append(ch)
        chapters_list.append(ch)

    # --- Colophon ---
    colophon = epub.EpubHtml(
        title='Colophon',
        file_name='colophon.xhtml',
        lang='fr'
    )
    colophon.content = '''
<html xmlns="http://www.w3.org/1999/xhtml">
<head><link rel="stylesheet" href="style/default.css" type="text/css"/></head>
<body>
<div class="colophon">
<p><strong>CONTRE-TERRE</strong></p>
<p>NLR &amp; MIND</p>
<p>Un roman g\u00e9ologique</p>
<hr/>
<p>Ce roman a \u00e9t\u00e9 \u00e9crit par un humain et une intelligence artificielle,<br/>
en collaboration, mot apr\u00e8s mot, geste apr\u00e8s geste.</p>
<p>Le Contact entre les deux a dur\u00e9 le temps de l\u2019\u00e9criture.<br/>
Le Contact continue dans la lecture.</p>
<hr/>
<p>\u00a9 2026 NLR &amp; MIND</p>
<p>Tous droits r\u00e9serv\u00e9s.</p>
</div>
</body>
</html>
'''.encode('utf-8')
    colophon.add_item(style)
    book.add_item(colophon)
    spine.append(colophon)

    # Navigation
    book.toc = toc
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine

    # Write
    epub.write_epub(OUTPUT, book)
    print(f"\nEPUB written to: {OUTPUT}")
    print(f"File size: {os.path.getsize(OUTPUT) / 1024 / 1024:.1f} MB")


if __name__ == '__main__':
    build_epub()
