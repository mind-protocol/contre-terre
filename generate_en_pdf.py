#!/usr/bin/env python3
"""
Generate illustrated English PDF interior for Counter-Earth.
KDP paperback format: 5.5" x 8.5" (396 x 612 points).
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak,
    NextPageTemplate, PageTemplate, Frame, BaseDocTemplate,
    FrameBreak
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import Flowable
from reportlab.lib.colors import black

# --- Constants ---
PAGE_W = 5.5 * inch  # 396 pt
PAGE_H = 8.5 * inch  # 612 pt
MARGIN_TOP = 0.75 * inch
MARGIN_BOTTOM = 0.75 * inch
MARGIN_OUTSIDE = 0.625 * inch
MARGIN_INSIDE = 0.875 * inch  # gutter

BASE_DIR = "/home/mind-protocol/contre-terre"
DATA_DIR = os.path.join(BASE_DIR, "data")
EN_DIR = os.path.join(BASE_DIR, "en")
OUTPUT_PATH = os.path.join(BASE_DIR, "Counter-Earth_EN_Illustrated_Interior.pdf")

# --- Register fonts ---
FONT_DIR = "/usr/share/fonts/truetype/liberation"
try:
    pdfmetrics.registerFont(TTFont('LibSerif', os.path.join(FONT_DIR, 'LiberationSerif-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('LibSerif-Bold', os.path.join(FONT_DIR, 'LiberationSerif-Bold.ttf')))
    pdfmetrics.registerFont(TTFont('LibSerif-Italic', os.path.join(FONT_DIR, 'LiberationSerif-Italic.ttf')))
    pdfmetrics.registerFont(TTFont('LibSerif-BoldItalic', os.path.join(FONT_DIR, 'LiberationSerif-BoldItalic.ttf')))
    FONT_BODY = 'LibSerif'
    FONT_BOLD = 'LibSerif-Bold'
    FONT_ITALIC = 'LibSerif-Italic'
    FONT_BOLD_ITALIC = 'LibSerif-BoldItalic'
    print("Using Liberation Serif fonts.")
except Exception as e:
    print(f"Could not load Liberation Serif: {e}. Falling back to Times.")
    FONT_BODY = 'Times-Roman'
    FONT_BOLD = 'Times-Bold'
    FONT_ITALIC = 'Times-Italic'
    FONT_BOLD_ITALIC = 'Times-BoldItalic'

pdfmetrics.registerFontFamily(
    'BookFont',
    normal=FONT_BODY,
    bold=FONT_BOLD,
    italic=FONT_ITALIC,
    boldItalic=FONT_BOLD_ITALIC,
)

# --- Styles ---
styles = getSampleStyleSheet()

style_body = ParagraphStyle(
    'BookBody',
    fontName=FONT_BODY,
    fontSize=11,
    leading=15,
    alignment=TA_JUSTIFY,
    spaceAfter=4,
    firstLineIndent=18,
)

style_body_first = ParagraphStyle(
    'BookBodyFirst',
    parent=style_body,
    firstLineIndent=0,
)

style_chapter_title = ParagraphStyle(
    'ChapterTitle',
    fontName=FONT_BOLD,
    fontSize=18,
    leading=24,
    alignment=TA_CENTER,
    spaceBefore=72,
    spaceAfter=24,
)

style_scene_heading = ParagraphStyle(
    'SceneHeading',
    fontName=FONT_ITALIC,
    fontSize=13,
    leading=18,
    alignment=TA_LEFT,
    spaceBefore=18,
    spaceAfter=12,
)

style_scene_break = ParagraphStyle(
    'SceneBreak',
    fontName=FONT_BODY,
    fontSize=11,
    leading=15,
    alignment=TA_CENTER,
    spaceBefore=12,
    spaceAfter=12,
)

style_half_title = ParagraphStyle(
    'HalfTitle',
    fontName=FONT_BOLD,
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
)

style_full_title = ParagraphStyle(
    'FullTitle',
    fontName=FONT_BOLD,
    fontSize=22,
    leading=28,
    alignment=TA_CENTER,
)

style_subtitle = ParagraphStyle(
    'Subtitle',
    fontName=FONT_ITALIC,
    fontSize=14,
    leading=20,
    alignment=TA_CENTER,
)

style_author = ParagraphStyle(
    'Author',
    fontName=FONT_BODY,
    fontSize=14,
    leading=20,
    alignment=TA_CENTER,
)

style_copyright = ParagraphStyle(
    'Copyright',
    fontName=FONT_BODY,
    fontSize=9,
    leading=13,
    alignment=TA_CENTER,
    spaceBefore=0,
    spaceAfter=4,
)

style_dedication = ParagraphStyle(
    'Dedication',
    fontName=FONT_ITALIC,
    fontSize=12,
    leading=18,
    alignment=TA_CENTER,
)

style_epigraph = ParagraphStyle(
    'Epigraph',
    fontName=FONT_ITALIC,
    fontSize=11,
    leading=16,
    alignment=TA_CENTER,
)

style_epigraph_attr = ParagraphStyle(
    'EpigraphAttr',
    fontName=FONT_BODY,
    fontSize=10,
    leading=14,
    alignment=TA_CENTER,
)

style_colophon = ParagraphStyle(
    'Colophon',
    fontName=FONT_BODY,
    fontSize=10,
    leading=14,
    alignment=TA_CENTER,
)


# --- Image insertion config ---
# ch_num -> list of (image_filename, position_fraction)
CHAPTER_IMAGES = {
    1: [("scene_nandi_barefoot.png", 0.15)],
    3: [("scene_village_deaf.png", 0.30)],
    4: [("scene_senzo_death.png", 0.60)],
    5: [("portrait_enama_contact_monde.png", 0.30), ("scene_jabu_drowning.png", 0.70)],
    6: [("scene_enama_sacrifice.png", 0.50), ("scene_sihle_alone.png", 0.80)],
    7: [("scene_thabo_inyoni_death.png", 0.60)],
    8: [("scene_nandi_charge_finale.png", 0.70), ("portrait_nandi_finale.png", 0.85), ("scene_silence_epilogue.png", 0.95)],
}

MAX_IMG_WIDTH = 3.5 * inch
SEPARATOR_WIDTH = 2.0 * inch


def make_image(path, max_width):
    """Create an Image flowable, scaled to max_width while preserving ratio."""
    if not os.path.exists(path):
        print(f"  WARNING: Image not found: {path}")
        return None
    img = Image(path)
    w, h = img.imageWidth, img.imageHeight
    if w <= 0 or h <= 0:
        return None
    ratio = h / w
    display_w = min(max_width, w)
    display_h = display_w * ratio
    # Limit height to 4 inches
    if display_h > 4 * inch:
        display_h = 4 * inch
        display_w = display_h / ratio
    img = Image(path, width=display_w, height=display_h)
    img.hAlign = 'CENTER'
    return img


def process_markdown_inline(text):
    """Convert markdown inline formatting to reportlab XML tags."""
    # Handle em-dashes (already present as — in the text)
    # Handle bold+italic ***text*** or ___text___
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Handle bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Handle italic *text*
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Escape ampersands that aren't already entities
    # (reportlab XML needs &amp; but we may already have &mdash; etc.)
    # Actually, let's be careful: replace & only if not followed by amp; or #
    text = text.replace('&', '&amp;')
    # Fix double-escaped
    text = text.replace('&amp;amp;', '&amp;')
    # Handle < and > that aren't our tags
    # We need to be careful not to break our <b>, <i>, </b>, </i> tags
    # Leave them as-is since they shouldn't appear in the novel text
    return text


def parse_chapter(filepath):
    """
    Parse a chapter markdown file.
    Returns a list of elements:
      ('title', text)
      ('scene', text)
      ('break', None)
      ('para', text)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    elements = []
    current_para = []

    def flush_para():
        if current_para:
            text = ' '.join(current_para).strip()
            if text:
                elements.append(('para', text))
            current_para.clear()

    for line in lines:
        line = line.rstrip('\n')

        # Chapter title: # ...
        if line.startswith('# '):
            flush_para()
            elements.append(('title', line[2:].strip()))
            continue

        # Scene heading: ## ...
        if line.startswith('## '):
            flush_para()
            elements.append(('scene', line[3:].strip()))
            continue

        # Scene break: ---
        if line.strip() == '---':
            flush_para()
            elements.append(('break', None))
            continue

        # Empty line: paragraph boundary
        if line.strip() == '':
            flush_para()
            continue

        # Regular text line: part of a paragraph
        current_para.append(line.strip())

    flush_para()
    return elements


def build_chapter_flowables(ch_num, elements):
    """Build reportlab flowables for a chapter."""
    flowables = []

    # Page break before chapter
    flowables.append(PageBreak())

    # Separator image at start of chapter
    sep_path = os.path.join(DATA_DIR, f"separator_ch{ch_num:02d}.png")
    sep_img = make_image(sep_path, SEPARATOR_WIDTH)
    if sep_img:
        flowables.append(Spacer(1, 36))
        flowables.append(sep_img)
        flowables.append(Spacer(1, 12))

    # Get image insertion points for this chapter
    img_inserts = CHAPTER_IMAGES.get(ch_num, [])

    # Collect only paragraphs for position calculation
    para_elements = [e for e in elements if e[0] == 'para']
    total_paras = len(para_elements)

    # Calculate insertion indices
    img_at_para = {}  # para_index -> list of image filenames
    for img_file, fraction in img_inserts:
        target_idx = int(total_paras * fraction)
        target_idx = max(0, min(target_idx, total_paras - 1))
        if target_idx not in img_at_para:
            img_at_para[target_idx] = []
        img_at_para[target_idx].append(img_file)

    para_count = 0
    first_para_in_section = True

    for etype, etext in elements:
        if etype == 'title':
            flowables.append(Paragraph(process_markdown_inline(etext), style_chapter_title))
            first_para_in_section = True

        elif etype == 'scene':
            flowables.append(Paragraph(process_markdown_inline(etext), style_scene_heading))
            first_para_in_section = True

        elif etype == 'break':
            flowables.append(Paragraph('*&nbsp;&nbsp;&nbsp;*&nbsp;&nbsp;&nbsp;*', style_scene_break))
            first_para_in_section = True

        elif etype == 'para':
            # Check if we need to insert an image before this paragraph
            if para_count in img_at_para:
                for img_file in img_at_para[para_count]:
                    img_path = os.path.join(DATA_DIR, img_file)
                    img = make_image(img_path, MAX_IMG_WIDTH)
                    if img:
                        flowables.append(Spacer(1, 12))
                        flowables.append(img)
                        flowables.append(Spacer(1, 12))

            processed = process_markdown_inline(etext)
            if first_para_in_section:
                flowables.append(Paragraph(processed, style_body_first))
                first_para_in_section = False
            else:
                flowables.append(Paragraph(processed, style_body))

            para_count += 1

            # Check if we need to insert an image after this paragraph
            # (for the last paragraph match)
            if para_count in img_at_para:
                for img_file in img_at_para[para_count]:
                    img_path = os.path.join(DATA_DIR, img_file)
                    img = make_image(img_path, MAX_IMG_WIDTH)
                    if img:
                        flowables.append(Spacer(1, 12))
                        flowables.append(img)
                        flowables.append(Spacer(1, 12))

    return flowables


class AlternatingPageTemplate(BaseDocTemplate):
    """Document with alternating margins for odd/even pages (mirrored for binding)."""

    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(self, filename, **kwargs)

        # Frame for odd pages (right-hand): gutter on left
        frame_odd = Frame(
            MARGIN_INSIDE,  # x: gutter margin on left
            MARGIN_BOTTOM,
            PAGE_W - MARGIN_INSIDE - MARGIN_OUTSIDE,  # width
            PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,  # height
            id='odd'
        )

        # Frame for even pages (left-hand): gutter on right
        frame_even = Frame(
            MARGIN_OUTSIDE,  # x: outside margin on left
            MARGIN_BOTTOM,
            PAGE_W - MARGIN_INSIDE - MARGIN_OUTSIDE,  # width
            PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,  # height
            id='even'
        )

        # Single centered frame for front matter
        frame_center = Frame(
            MARGIN_INSIDE,
            MARGIN_BOTTOM,
            PAGE_W - MARGIN_INSIDE - MARGIN_OUTSIDE,
            PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,
            id='center'
        )

        template_odd = PageTemplate(id='odd', frames=[frame_odd], onPage=self._on_odd_page)
        template_even = PageTemplate(id='even', frames=[frame_even], onPage=self._on_even_page)
        template_front = PageTemplate(id='front', frames=[frame_center], onPage=self._on_front_page)

        self.addPageTemplates([template_front, template_odd, template_even])

    def _on_odd_page(self, canvas, doc):
        pass

    def _on_even_page(self, canvas, doc):
        pass

    def _on_front_page(self, canvas, doc):
        pass

    def afterPage(self):
        """Switch between odd/even templates based on page number."""
        # Page numbers: 1-based. Odd pages get 'odd' template, even get 'even'.
        # This runs AFTER a page is finished, so self.page is the page just finished.
        next_page = self.page + 1
        if next_page % 2 == 1:
            self._nextPageTemplateIndex = 1  # 'odd' (index 1 in our list)
        else:
            self._nextPageTemplateIndex = 2  # 'even' (index 2 in our list)


def build_front_matter():
    """Build the front matter flowables."""
    flowables = []

    # --- Half-title page ---
    flowables.append(Spacer(1, 2.5 * inch))
    flowables.append(Paragraph("COUNTER-EARTH", style_half_title))
    flowables.append(PageBreak())

    # --- Blank verso ---
    flowables.append(Spacer(1, 1))
    flowables.append(PageBreak())

    # --- Full title page ---
    flowables.append(Spacer(1, 2 * inch))
    flowables.append(Paragraph("COUNTER-EARTH", style_full_title))
    flowables.append(Spacer(1, 24))
    flowables.append(Paragraph("NLR &amp; MIND", style_author))
    flowables.append(Spacer(1, 24))
    flowables.append(Paragraph("A geological novel", style_subtitle))
    flowables.append(PageBreak())

    # --- Copyright page ---
    flowables.append(Spacer(1, 3 * inch))
    copyright_lines = [
        "Counter-Earth",
        "Originally published in French as <i>Contre-Terre</i>",
        "",
        "\u00a9 2026 NLR &amp; MIND",
        "All rights reserved.",
        "",
        "First English edition: 2026",
        "",
        "This is a work of fiction.",
        "The earth, however, never stops shaking.",
    ]
    for line in copyright_lines:
        if line == "":
            flowables.append(Spacer(1, 8))
        else:
            flowables.append(Paragraph(line, style_copyright))
    flowables.append(PageBreak())

    # --- Dedication page ---
    flowables.append(Spacer(1, 2.5 * inch))
    flowables.append(Paragraph("For those who said yes.", style_dedication))
    flowables.append(PageBreak())

    # --- Blank verso ---
    flowables.append(Spacer(1, 1))
    flowables.append(PageBreak())

    # --- Epigraph page ---
    flowables.append(Spacer(1, 2 * inch))
    flowables.append(Paragraph(
        "\u201cWe had nothing to oppose the wind but the march,<br/>and the march, we marched.\u201d",
        style_epigraph
    ))
    flowables.append(Spacer(1, 12))
    flowables.append(Paragraph(
        "\u2014 Alain Damasio, <i>The Horde of Counterwind</i>",
        style_epigraph_attr
    ))
    flowables.append(PageBreak())

    # Switch to alternating body templates
    flowables.append(NextPageTemplate('odd'))

    # --- Blank verso before chapter 1 ---
    flowables.append(Spacer(1, 1))

    return flowables


def build_colophon():
    """Build colophon page."""
    flowables = []
    flowables.append(PageBreak())
    flowables.append(Spacer(1, 3 * inch))
    flowables.append(Paragraph(
        "Counter-Earth was written by NLR &amp; MIND<br/>"
        "between February and March 2026.<br/>"
        "Originally published in French as <i>Contre-Terre</i>.",
        style_colophon
    ))
    return flowables


def main():
    print("Building Counter-Earth English illustrated interior PDF...")

    doc = AlternatingPageTemplate(
        OUTPUT_PATH,
        pagesize=(PAGE_W, PAGE_H),
        title="Counter-Earth",
        author="NLR & MIND",
    )

    all_flowables = []

    # Front matter
    print("Building front matter...")
    all_flowables.extend(build_front_matter())

    # Chapters
    for ch_num in range(1, 9):
        ch_file = os.path.join(EN_DIR, f"chapter_{ch_num:02d}.md")
        print(f"Processing chapter {ch_num}: {ch_file}")
        elements = parse_chapter(ch_file)
        ch_flowables = build_chapter_flowables(ch_num, elements)
        all_flowables.extend(ch_flowables)

    # Colophon
    print("Building colophon...")
    all_flowables.extend(build_colophon())

    # Build PDF
    print(f"Generating PDF: {OUTPUT_PATH}")
    doc.build(all_flowables)
    print(f"Done! Output: {OUTPUT_PATH}")

    # File size
    size_mb = os.path.getsize(OUTPUT_PATH) / (1024 * 1024)
    print(f"File size: {size_mb:.1f} MB")


if __name__ == '__main__':
    main()
