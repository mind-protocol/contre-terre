#!/usr/bin/env python3
"""
Generate illustrated French PDF interior for Contre-Terre.
KDP paperback format: 5.5" x 8.5" (396 x 612 points).
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image,
    KeepTogether, BaseDocTemplate, PageTemplate, Frame, NextPageTemplate
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_PATH = os.path.join(BASE_DIR, "Contre-Terre_FR_Illustrated_Interior.pdf")

PAGE_W = 5.5 * inch   # 396 pt
PAGE_H = 8.5 * inch   # 612 pt

MARGIN_TOP = 0.75 * inch
MARGIN_BOTTOM = 0.75 * inch
MARGIN_OUTSIDE = 0.625 * inch
MARGIN_INSIDE = 0.875 * inch  # gutter

# ---------------------------------------------------------------------------
# Register fonts
# ---------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/liberation"

pdfmetrics.registerFont(TTFont("LiberationSerif", os.path.join(FONT_DIR, "LiberationSerif-Regular.ttf")))
pdfmetrics.registerFont(TTFont("LiberationSerif-Bold", os.path.join(FONT_DIR, "LiberationSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("LiberationSerif-Italic", os.path.join(FONT_DIR, "LiberationSerif-Italic.ttf")))
pdfmetrics.registerFont(TTFont("LiberationSerif-BoldItalic", os.path.join(FONT_DIR, "LiberationSerif-BoldItalic.ttf")))

pdfmetrics.registerFontFamily(
    "LiberationSerif",
    normal="LiberationSerif",
    bold="LiberationSerif-Bold",
    italic="LiberationSerif-Italic",
    boldItalic="LiberationSerif-BoldItalic",
)

FONT = "LiberationSerif"

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
style_body = ParagraphStyle(
    "Body",
    fontName=FONT,
    fontSize=11,
    leading=15,
    alignment=TA_JUSTIFY,
    spaceAfter=6,
    firstLineIndent=18,
)

style_body_first = ParagraphStyle(
    "BodyFirst",
    parent=style_body,
    firstLineIndent=0,
)

style_chapter_title = ParagraphStyle(
    "ChapterTitle",
    fontName=f"{FONT}-Bold",
    fontSize=18,
    leading=24,
    alignment=TA_CENTER,
    spaceBefore=72,
    spaceAfter=24,
)

style_scene_heading = ParagraphStyle(
    "SceneHeading",
    fontName=f"{FONT}-Italic",
    fontSize=13,
    leading=18,
    alignment=TA_LEFT,
    spaceBefore=18,
    spaceAfter=12,
)

style_separator = ParagraphStyle(
    "Separator",
    fontName=FONT,
    fontSize=11,
    leading=15,
    alignment=TA_CENTER,
    spaceBefore=12,
    spaceAfter=12,
)

style_centered = ParagraphStyle(
    "Centered",
    fontName=FONT,
    fontSize=11,
    leading=15,
    alignment=TA_CENTER,
)

style_centered_large = ParagraphStyle(
    "CenteredLarge",
    fontName=f"{FONT}-Bold",
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
)

style_centered_subtitle = ParagraphStyle(
    "CenteredSubtitle",
    fontName=f"{FONT}-Italic",
    fontSize=14,
    leading=20,
    alignment=TA_CENTER,
)

style_centered_author = ParagraphStyle(
    "CenteredAuthor",
    fontName=FONT,
    fontSize=14,
    leading=20,
    alignment=TA_CENTER,
)

style_copyright = ParagraphStyle(
    "Copyright",
    fontName=FONT,
    fontSize=9,
    leading=13,
    alignment=TA_LEFT,
)

style_dedication = ParagraphStyle(
    "Dedication",
    fontName=f"{FONT}-Italic",
    fontSize=13,
    leading=18,
    alignment=TA_CENTER,
)

style_epigraph = ParagraphStyle(
    "Epigraph",
    fontName=f"{FONT}-Italic",
    fontSize=11,
    leading=15,
    alignment=TA_CENTER,
)

style_epigraph_attr = ParagraphStyle(
    "EpigraphAttr",
    fontName=FONT,
    fontSize=10,
    leading=14,
    alignment=TA_CENTER,
)

style_colophon = ParagraphStyle(
    "Colophon",
    fontName=FONT,
    fontSize=9,
    leading=13,
    alignment=TA_CENTER,
)


# ---------------------------------------------------------------------------
# Image insertion specs per chapter
# ---------------------------------------------------------------------------
# Key: chapter number -> list of (image_filename, approximate_fraction_through_chapter)
CHAPTER_IMAGES = {
    1: [("scene_nandi_barefoot.png", 0.08)],
    3: [("scene_village_deaf.png", 0.20)],
    4: [("scene_senzo_death.png", 0.60)],
    5: [
        ("portrait_enama_contact_monde.png", 0.30),
        ("scene_jabu_drowning.png", 0.70),
    ],
    6: [
        ("scene_enama_sacrifice.png", 0.50),
        ("scene_sihle_alone.png", 0.80),
    ],
    7: [("scene_thabo_inyoni_death.png", 0.60)],
    8: [
        ("scene_nandi_charge_finale.png", 0.70),
        ("portrait_nandi_finale.png", 0.85),
        ("scene_silence_epilogue.png", 0.95),
    ],
}


def make_image_flowable(filename, max_width=3.5 * inch):
    """Create an Image flowable centered, max 3.5 inches wide, preserving aspect ratio."""
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"  WARNING: image not found: {path}")
        return None
    img = Image(path)
    # Scale to max_width preserving aspect ratio
    iw, ih = img.imageWidth, img.imageHeight
    if iw > 0:
        scale = min(max_width / iw, 1.0)
        img.drawWidth = iw * scale
        img.drawHeight = ih * scale
    img.hAlign = "CENTER"
    return img


def make_separator_image(chapter_num):
    """Create the separator image for a chapter."""
    filename = f"separator_ch{chapter_num:02d}.png"
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        print(f"  WARNING: separator not found: {path}")
        return None
    img = Image(path)
    max_w = 2.0 * inch
    iw, ih = img.imageWidth, img.imageHeight
    if iw > 0:
        scale = min(max_w / iw, 1.0)
        img.drawWidth = iw * scale
        img.drawHeight = ih * scale
    img.hAlign = "CENTER"
    return img


# ---------------------------------------------------------------------------
# Markdown parser
# ---------------------------------------------------------------------------
def process_inline(text):
    """Convert markdown inline formatting to reportlab XML tags."""
    # Handle em-dashes: ensure proper rendering
    text = text.replace("—", "\u2014")
    # Bold+italic ***text***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic *text*
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Escape ampersands not already escaped and not part of XML entities
    text = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#)', '&amp;', text)
    # Escape < > that are not tags
    # (be careful: we use <b>, <i>, etc.)
    return text


def parse_chapter(filepath):
    """
    Parse a chapter markdown file.
    Returns a list of elements, each being one of:
        ("chapter_title", text)
        ("scene_heading", text)
        ("separator", None)
        ("paragraph", text)   # text already has inline formatting
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    elements = []
    current_para = []

    def flush_para():
        if current_para:
            text = " ".join(current_para).strip()
            if text:
                elements.append(("paragraph", process_inline(text)))
            current_para.clear()

    for line in lines:
        stripped = line.rstrip("\n")

        # Chapter title: # ...
        if stripped.startswith("# ") and not stripped.startswith("## "):
            flush_para()
            elements.append(("chapter_title", stripped[2:].strip()))
            continue

        # Scene heading: ## ...
        if stripped.startswith("## "):
            flush_para()
            elements.append(("scene_heading", stripped[3:].strip()))
            continue

        # Scene break: ---
        if stripped.strip() == "---":
            flush_para()
            elements.append(("separator", None))
            continue

        # Empty line = paragraph break
        if stripped.strip() == "":
            flush_para()
            continue

        # Regular text line
        current_para.append(stripped)

    flush_para()
    return elements


# ---------------------------------------------------------------------------
# Build story
# ---------------------------------------------------------------------------
def build_story():
    story = []

    # -----------------------------------------------------------------------
    # 1. Half-title page
    # -----------------------------------------------------------------------
    story.append(Spacer(1, 2.5 * inch))
    story.append(Paragraph("CONTRE-TERRE", style_centered_large))
    story.append(PageBreak())

    # Blank verso
    story.append(Spacer(1, 1))
    story.append(PageBreak())

    # -----------------------------------------------------------------------
    # 2. Full title page
    # -----------------------------------------------------------------------
    story.append(Spacer(1, 2 * inch))
    story.append(Paragraph("CONTRE-TERRE", style_centered_large))
    story.append(Spacer(1, 24))
    story.append(Paragraph("NLR &amp; MIND", style_centered_author))
    story.append(Spacer(1, 36))
    story.append(Paragraph("\u2022", style_centered))
    story.append(Spacer(1, 24))
    story.append(Paragraph("Un roman g\u00e9ologique", style_centered_subtitle))
    story.append(PageBreak())

    # -----------------------------------------------------------------------
    # 3. Copyright page
    # -----------------------------------------------------------------------
    copyright_text = [
        "Contre-Terre",
        "\u00a9 2026 NLR &amp; MIND",
        "Tous droits r\u00e9serv\u00e9s.",
        "",
        "ISBN (broch\u00e9) : _______________",
        "ISBN (eBook) : _______________",
        "ASIN : _______________",
        "",
        "Premi\u00e8re \u00e9dition : 2026",
        "",
        "Aucune partie de cet ouvrage ne peut \u00eatre reproduite",
        "sous quelque forme que ce soit sans l\u2019autorisation \u00e9crite",
        "de l\u2019auteur, \u00e0 l\u2019exception de br\u00e8ves citations dans le cadre",
        "de critiques ou d\u2019articles.",
        "",
        "Ceci est une \u0153uvre de fiction.",
        "La terre, elle, ne s\u2019arr\u00eate jamais de trembler.",
        "",
        "Couverture : [\u00c0 compl\u00e9ter]",
        "Mise en page : [\u00c0 compl\u00e9ter]",
        "",
        "Contact : [email / site \u00e0 compl\u00e9ter]",
    ]
    story.append(Spacer(1, 2 * inch))
    for line in copyright_text:
        if line == "":
            story.append(Spacer(1, 8))
        else:
            story.append(Paragraph(line, style_copyright))
    story.append(PageBreak())

    # -----------------------------------------------------------------------
    # 4. Dedication page
    # -----------------------------------------------------------------------
    story.append(Spacer(1, 3 * inch))
    story.append(Paragraph("\u00c0 ceux qui ont dit oui.", style_dedication))
    story.append(PageBreak())

    # Blank verso
    story.append(Spacer(1, 1))
    story.append(PageBreak())

    # -----------------------------------------------------------------------
    # 5. Epigraph page
    # -----------------------------------------------------------------------
    story.append(Spacer(1, 2.5 * inch))
    story.append(Paragraph(
        "\u00ab\u2009Nous n\u2019avions rien d\u2019autre \u00e0 opposer au vent<br/>"
        "que la marche, et la marche, nous marchions.\u2009\u00bb",
        style_epigraph,
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "\u2014 Alain Damasio, <i>La Horde du Contrevent</i>",
        style_epigraph_attr,
    ))
    story.append(PageBreak())

    # Blank verso
    story.append(Spacer(1, 1))
    story.append(PageBreak())

    # -----------------------------------------------------------------------
    # 6. Chapters 1-8
    # -----------------------------------------------------------------------
    for ch_num in range(1, 9):
        ch_file = os.path.join(BASE_DIR, f"chapitre_{ch_num:02d}.md")
        print(f"Processing chapter {ch_num}: {ch_file}")
        elements = parse_chapter(ch_file)

        # Determine image insertion points for this chapter
        images_for_ch = CHAPTER_IMAGES.get(ch_num, [])

        # Count total paragraphs to determine insertion positions
        para_indices = [i for i, (typ, _) in enumerate(elements) if typ == "paragraph"]
        total_paras = len(para_indices)

        # Map each image to the paragraph index after which it should be inserted
        image_insertions = {}  # para_count -> list of image filenames
        for img_file, frac in images_for_ch:
            target_para = max(1, int(total_paras * frac))
            if target_para not in image_insertions:
                image_insertions[target_para] = []
            image_insertions[target_para].append(img_file)

        # Build flowables for this chapter
        para_count = 0
        first_para_in_section = True

        for elem_type, elem_text in elements:
            if elem_type == "chapter_title":
                # Page break before chapter
                story.append(PageBreak())
                # Separator image at top
                sep_img = make_separator_image(ch_num)
                if sep_img:
                    story.append(Spacer(1, 36))
                    story.append(sep_img)
                    story.append(Spacer(1, 18))
                # Chapter title
                story.append(Paragraph(process_inline(elem_text), style_chapter_title))
                first_para_in_section = True

            elif elem_type == "scene_heading":
                story.append(Spacer(1, 6))
                story.append(Paragraph(process_inline(elem_text), style_scene_heading))
                first_para_in_section = True

            elif elem_type == "separator":
                story.append(Paragraph("*\u2003*\u2003*", style_separator))
                first_para_in_section = True

            elif elem_type == "paragraph":
                para_count += 1
                if first_para_in_section:
                    story.append(Paragraph(elem_text, style_body_first))
                    first_para_in_section = False
                else:
                    story.append(Paragraph(elem_text, style_body))

                # Check for image insertion after this paragraph
                if para_count in image_insertions:
                    for img_file in image_insertions[para_count]:
                        img = make_image_flowable(img_file)
                        if img:
                            story.append(Spacer(1, 12))
                            story.append(img)
                            story.append(Spacer(1, 12))

    # -----------------------------------------------------------------------
    # 7. Colophon page
    # -----------------------------------------------------------------------
    story.append(PageBreak())
    story.append(Spacer(1, 3 * inch))
    colophon_lines = [
        "<b>Contre-Terre</b>",
        "",
        "Compos\u00e9 en Liberation Serif",
        "Format 5,5 \u00d7 8,5 pouces",
        "",
        "\u0152uvre \u00e9crite par NLR &amp; MIND",
        "Premi\u00e8re \u00e9dition \u2014 2026",
        "",
        "Imprim\u00e9 par Amazon KDP",
        "",
        "<i>La terre, elle, ne s\u2019arr\u00eate jamais de trembler.</i>",
    ]
    for line in colophon_lines:
        if line == "":
            story.append(Spacer(1, 8))
        else:
            story.append(Paragraph(line, style_colophon))

    return story


# ---------------------------------------------------------------------------
# Page number drawing (alternating margins for recto/verso)
# ---------------------------------------------------------------------------
def draw_page_number(canvas, doc):
    """Draw page number at bottom center."""
    page_num = canvas.getPageNumber()
    # Skip page numbers on front matter pages (first ~10 pages)
    if page_num <= 10:
        return
    canvas.saveState()
    canvas.setFont(FONT, 9)
    text = str(page_num)
    canvas.drawCentredString(PAGE_W / 2, MARGIN_BOTTOM - 18, text)
    canvas.restoreState()


# ---------------------------------------------------------------------------
# Custom doc template with alternating margins
# ---------------------------------------------------------------------------
def build_doc():
    """Create a BaseDocTemplate with recto/verso frames."""

    # For simplicity with alternating margins: use a single frame sized
    # for the smaller margin side (inside=gutter). The visual difference
    # between recto and verso is handled by the frame offset.

    # Recto (odd pages): gutter on left (inside = left = 0.875"),
    #                     outside on right = 0.625"
    frame_recto = Frame(
        MARGIN_INSIDE,          # x
        MARGIN_BOTTOM,          # y
        PAGE_W - MARGIN_INSIDE - MARGIN_OUTSIDE,  # width
        PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,       # height
        id="recto",
    )

    # Verso (even pages): gutter on right (inside = right = 0.875"),
    #                      outside on left = 0.625"
    frame_verso = Frame(
        MARGIN_OUTSIDE,         # x
        MARGIN_BOTTOM,          # y
        PAGE_W - MARGIN_INSIDE - MARGIN_OUTSIDE,  # width
        PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,       # height
        id="verso",
    )

    template_recto = PageTemplate(
        id="Recto",
        frames=[frame_recto],
        onPage=draw_page_number,
    )
    template_verso = PageTemplate(
        id="Verso",
        frames=[frame_verso],
        onPage=draw_page_number,
    )

    doc = BaseDocTemplate(
        OUTPUT_PATH,
        pagesize=(PAGE_W, PAGE_H),
        title="Contre-Terre",
        author="NLR & MIND",
        pageTemplates=[template_recto, template_verso],
    )

    return doc


class AlternatingPageAction:
    """Flowable-like action that alternates page templates on page transitions."""
    pass


def on_page_change(canvas, doc):
    """Switch between recto/verso templates based on page number."""
    page_num = canvas.getPageNumber()
    if page_num % 2 == 1:
        doc.handle_nextPageTemplate("Recto")
    else:
        doc.handle_nextPageTemplate("Verso")


def draw_page_number_with_switch(canvas, doc):
    """Combined: draw page number + switch template for next page."""
    draw_page_number(canvas, doc)
    on_page_change(canvas, doc)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"Generating PDF: {OUTPUT_PATH}")
    print(f"Page size: {PAGE_W}pt x {PAGE_H}pt ({PAGE_W/inch}\" x {PAGE_H/inch}\")")

    # Build a simple doc with alternating margins
    frame_recto = Frame(
        MARGIN_INSIDE,
        MARGIN_BOTTOM,
        PAGE_W - MARGIN_INSIDE - MARGIN_OUTSIDE,
        PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,
        id="recto",
    )
    frame_verso = Frame(
        MARGIN_OUTSIDE,
        MARGIN_BOTTOM,
        PAGE_W - MARGIN_INSIDE - MARGIN_OUTSIDE,
        PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,
        id="verso",
    )

    template_recto = PageTemplate(id="Recto", frames=[frame_recto],
                                   onPage=draw_page_number_with_switch)
    template_verso = PageTemplate(id="Verso", frames=[frame_verso],
                                   onPage=draw_page_number_with_switch)

    doc = BaseDocTemplate(
        OUTPUT_PATH,
        pagesize=(PAGE_W, PAGE_H),
        title="Contre-Terre",
        author="NLR & MIND",
        pageTemplates=[template_recto, template_verso],
    )

    story = build_story()

    print(f"Building PDF with {len(story)} flowable elements...")
    doc.build(story)
    print(f"Done! Output: {OUTPUT_PATH}")

    # File size
    size_mb = os.path.getsize(OUTPUT_PATH) / (1024 * 1024)
    print(f"File size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
