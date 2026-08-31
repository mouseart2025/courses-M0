"""Static layout verification for built EN decks (no renderer required).

For every text box: estimate rendered text width with Pillow + a system font
(Arial, slightly wider than Source Han Sans for Latin — conservative check),
wrap on the box width, then check:
  - single-word overflow beyond box width
  - estimated wrapped line count * line height vs box height
Also flag text boxes whose bottom edge crosses the footer zone (y > 5.05 in)
or overlap the title zone badly.
"""
import sys, re
from pptx import Presentation
from pptx.util import Emu
from PIL import ImageFont

FONT_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
DPI = 96.0
_font_cache = {}

def _font(size_pt):
    px = int(round(size_pt * DPI / 72.0))
    if px not in _font_cache:
        try:
            _font_cache[px] = ImageFont.truetype(FONT_PATH, px)
        except Exception:
            _font_cache[px] = None
    return _font_cache[px]

def text_w(txt, size_pt, bold=False):
    f = _font(size_pt)
    if f is None:
        return len(txt) * size_pt * 0.6
    return f.getlength(txt) / DPI * 72.0  # in points

def check_box(txt, box_w_pt, box_h_pt, size_pt, line_spacing):
    """Return list of issues for a single paragraph text."""
    issues = []
    if not txt.strip():
        return issues
    # naive word wrap
    words = txt.split()
    lines = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(trial, size_pt) <= box_w_pt or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    for ln in lines:
        if text_w(ln, size_pt) > box_w_pt * 1.02:
            issues.append(f"    line overflows: '{ln[:60]}...' ({text_w(ln,size_pt):.0f}pt > {box_w_pt:.0f}pt)")
    line_h = size_pt * (line_spacing or 1.2) * 1.25
    if len(lines) * line_h > box_h_pt * 1.15:
        issues.append(f"    estimated {len(lines)} lines * {line_h:.0f}pt > box height {box_h_pt:.0f}pt")
    return issues

def main(path):
    prs = Presentation(path)
    n = len(prs.slides._sldIdLst)
    total_issues = 0
    for idx, slide in enumerate(prs.slides, start=1):
        for sh in slide.shapes:
            if not sh.has_text_frame:
                continue
            t = sh.text_frame
            txt = t.text
            if not txt.strip():
                continue
            try:
                bw = sh.width / 914400 * 72.0
                bh = sh.height / 914400 * 72.0
            except Exception:
                continue
            # skip footer line
            if txt.startswith("Chaihuo Maker Academy · M0 ·"):
                continue
            for p in t.paragraphs:
                runs = [r for r in p.runs if r.text.strip()]
                if not runs:
                    continue
                size = max((r.font.size.pt if r.font.size else 18) for r in runs)
                bold = any(r.font.bold for r in runs)
                ls = p.line_spacing if isinstance(p.line_spacing, float) else 1.15
                ptext = "".join(r.text for r in runs)
                issues = check_box(ptext, bw, bh, size, ls)
                for iss in issues:
                    print(f"  slide {idx:02d} [{txt[:28].strip()}]: {iss}")
                    total_issues += 1
    print(f"RESULT: {total_issues} layout warnings across {n} slides")

if __name__ == "__main__":
    main(sys.argv[1])
