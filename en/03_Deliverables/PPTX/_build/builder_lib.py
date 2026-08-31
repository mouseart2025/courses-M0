"""
Chaihuo brand PPTX builder library — English M0 decks (brand rebuild).

Layout spec (per chaihuo-ppt-brand.md):
- Slide: 960x540 px == 10.0 x 5.625 in, white background
- Title zone: top 100 px; yellow chapter bar 6 px wide at left (x=40px)
- Content zone: 110-490 px (y 1.15 in -> 5.1 in)
- Footer zone: bottom 40 px, page number 10-12 pt
- Colors: white 70 / yellow #F3D230 15 / ink #000000 10 / red #D84144 5
- Fifth permitted color: code box fill #F5F5F5 + 1px ink border + monospace 14-16 pt
- No gradients, no shadows, no complex illustrations; icons: 2px ink stroke
  (fallback: yellow dot markers for list items)
- Font: Source Han Sans SC (fallback: PingFang SC / Noto Sans CJK SC / Arial)
- Red usage: per deck controlled; per page <= 1-2 elements

Notes (speaker notes) carry the Teacher's Guide instructor notes verbatim.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ------------------------------------------------------------------ palette
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
YELLOW = RGBColor(0xF3, 0xD2, 0x30)
INK    = RGBColor(0x00, 0x00, 0x00)
RED    = RGBColor(0xD8, 0x41, 0x44)
CODEBG = RGBColor(0xF5, 0xF5, 0xF5)

SW, SH = Inches(10), Inches(5.625)

FONT = "Source Han Sans SC"   # fallback handled by the viewer; see brand spec 3.1
MONO = "Source Code Pro"

# ------------------------------------------------------------------ primitives
def new_deck():
    prs = Presentation()
    prs.slide_width = SW
    prs.slide_height = SH
    return prs

def _blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])  # blank layout

def _no_shadow(shape):
    """Strip any shadow effect so no shape ever renders a drop shadow."""
    sp = shape._element.spPr
    el = sp.find("{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst")
    if el is not None:
        sp.remove(el)

def add_bg(slide):
    r = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    r.fill.solid(); r.fill.fore_color.rgb = WHITE
    r.line.fill.background()
    r.shadow.inherit = False
    _no_shadow(r)
    return r

def add_rect(slide, x, y, w, h, fill=WHITE, border=None, border_w=1.0):
    """Rectangle; border is an RGBColor or None. No shadow, no gradient."""
    r = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                               Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        r.fill.background()
    else:
        r.fill.solid(); r.fill.fore_color.rgb = fill
    if border is None:
        r.line.fill.background()
    else:
        r.line.color.rgb = border
        r.line.width = Pt(border_w)
    r.shadow.inherit = False
    _no_shadow(r)
    return r

def add_oval(slide, x, y, d, fill=YELLOW, border=None):
    o = slide.shapes.add_shape(MSO_SHAPE.OVAL,
                               Inches(x), Inches(y), Inches(d), Inches(d))
    if fill is None:
        o.fill.background()
    else:
        o.fill.solid(); o.fill.fore_color.rgb = fill
    if border is None:
        o.line.fill.background()
    else:
        o.line.color.rgb = border
        o.line.width = Pt(1)
    o.shadow.inherit = False
    _no_shadow(o)
    return o

def add_text(slide, x, y, w, h, text, size=20, bold=False, color=INK,
             align=PP_ALIGN.LEFT, font=FONT, mono=False, line_spacing=1.0,
             anchor=MSO_ANCHOR.TOP, wrap=True):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = align
    if line_spacing:
        p.line_spacing = line_spacing
    run = p.add_run()
    run.text = text
    f = run.font
    f.name = MONO if mono else font
    f.size = Pt(size)
    f.bold = bold
    f.color.rgb = color
    return tb

def add_multiline(slide, x, y, w, h, lines, size=20, bold=False, color=INK,
                  font=FONT, line_spacing=1.15, align=PP_ALIGN.LEFT,
                  anchor=MSO_ANCHOR.TOP):
    """lines: list of (text, overrides-dict) or plain str."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    first = True
    for item in lines:
        if isinstance(item, tuple):
            text, ov = item
        else:
            text, ov = item, {}
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = ov.get("align", align)
        p.line_spacing = ov.get("line_spacing", line_spacing)
        if ov.get("space_before"):
            p.space_before = Pt(ov["space_before"])
        if ov.get("space_after"):
            p.space_after = Pt(ov["space_after"])
        run = p.add_run()
        run.text = text
        f = run.font
        f.name = MONO if ov.get("mono") else ov.get("font", font)
        f.size = Pt(ov.get("size", size))
        f.bold = ov.get("bold", bold)
        f.color.rgb = ov.get("color", color)
    return tb

# ------------------------------------------------------------------ brand atoms
_FW = {}

def _text_width_pt(txt, size_pt, bold=False):
    """Estimate rendered width in points (Arial metrics, slightly wider than
    Source Han Sans for Latin — conservative)."""
    try:
        from PIL import ImageFont
        key = (int(round(size_pt)), bold)
        if key not in _FW:
            p = ("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold
                 else "/System/Library/Fonts/Supplemental/Arial.ttf")
            try:
                _FW[key] = ImageFont.truetype(p, int(round(size_pt * 96 / 72.0)))
            except Exception:
                _FW[key] = None
        f = _FW[key]
        if f is None:
            return len(txt) * size_pt * 0.52 * (1.08 if bold else 1.0)
        return f.getlength(txt) / 96.0 * 72.0
    except Exception:
        return len(txt) * size_pt * 0.52 * (1.08 if bold else 1.0)

def add_title_bar(slide, text, max_size=38, min_size=26):
    """Yellow chapter bar (6px) + black title; auto-fit font so the title stays
    on one line (per brand spec: 36-40pt, long titles step down, floor 26pt)."""
    add_rect(slide, 0.42, 0.24, 0.06, 0.62, fill=YELLOW, border=None)
    size = max_size
    while size > min_size and _text_width_pt(text, size, bold=True) > 8.55 * 72:
        size -= 2
    add_text(slide, 0.62, 0.16, 8.9, 0.85, text, size=size, bold=True)

def add_subtitle(slide, text, y=1.02, size=18, color=INK):
    add_text(slide, 0.62, y, 8.9, 0.4, text, size=size, color=color)

def add_footer(slide, page_no, total, deck_label):
    add_text(slide, 0.42, 5.22, 9.16, 0.3,
             f"Chaihuo Maker Academy · M0 · {deck_label} | {page_no:02d} / {total}",
             size=10, color=INK)

def add_card(slide, x, y, w, h, fill=WHITE, border=INK, border_w=1.0):
    return add_rect(slide, x, y, w, h, fill=fill, border=border, border_w=border_w)

def add_yellow_dot_item(slide, x, y, w, text, size=18, bold=False,
                        dot_r=0.055, gap=0.16, line_spacing=1.1):
    add_oval(slide, x, y + 0.10, dot_r * 2, fill=YELLOW, border=None)
    add_text(slide, x + gap, y, w - gap, 0.6, text, size=size, bold=bold,
             line_spacing=line_spacing)

def add_golden_line(slide, x, y, w, text, size=17, bar_w=0.06, h=0.52):
    """Golden-line quote box: yellow left border + wrapped text (h auto if None)."""
    if h is None:
        import math
        lines = max(1, math.ceil(_text_width_pt(text, size) / ((w - 0.22) * 72)))
        h = 0.12 + lines * size * 1.15 * 1.25 / 72.0
    add_rect(slide, x, y, bar_w, h, fill=YELLOW, border=None)
    add_text(slide, x + 0.22, y + 0.02, w - 0.22, h - 0.04, text, size=size,
             line_spacing=1.15)

def add_grey_box(slide, x, y, w, h, text, size=15, mono=True, fill=CODEBG):
    add_card(slide, x, y, w, h, fill=fill, border=INK, border_w=1.0)
    add_text(slide, x + 0.18, y + 0.10, w - 0.36, h - 0.2, text,
             size=size, mono=mono, line_spacing=1.2)

def add_red_rule_box(slide, x, y, w, h, title, body_lines, body_size=17):
    """Warning/rule box with red left border + red dot marker (the deck's red budget)."""
    add_rect(slide, x, y, 0.06, h, fill=RED, border=None)
    add_oval(slide, x + 0.18, y + 0.12, 0.11, fill=RED, border=None)
    add_text(slide, x + 0.40, y + 0.06, w - 0.55, 0.35, title, size=20, bold=True)
    add_multiline(slide, x + 0.40, y + 0.44, w - 0.55, h - 0.5, body_lines,
                  size=body_size, line_spacing=1.15)

def set_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text
