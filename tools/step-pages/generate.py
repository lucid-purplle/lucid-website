#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Generates the 20 workflow step detail pages from:
#   tools/step-pages/content.py   (the content data)
#   tools/step-pages/template.html (the page shell)
#
# Run from anywhere:
#   python3 tools/step-pages/generate.py            -> all 20 pages + grids
#   python3 tools/step-pages/generate.py --only ugc-6   -> just one page
#
# Output: workflow-{wf}-step-NN.html in the repo root, plus grid snippets
# (tools/step-pages/_grid-*.html) for pasting into the two parent
# workflow pages.
# ---------------------------------------------------------------------------
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import content as C  # noqa: E402


def esc(s):
    """HTML-escape text destined for a <pre> block or an attribute/text node."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_part(part):
    kind = part[0]
    if kind == "text":
        # html is trusted authored markup (may contain <strong>) — inserted as-is.
        return '    <p class="step-text">%s</p>' % part[1]
    if kind == "prompt":
        return ('    <div class="copy-block">\n'
                '      <pre class="prompt-pre js-copy-text">%s</pre>\n'
                '      <button class="gallery-copy" type="button">Copy</button>\n'
                '    </div>') % esc(part[1])
    if kind == "raw":
        return part[1]
    raise ValueError("unknown part type: %r" % kind)


def step_filename(step):
    return "%s-%02d.html" % (C.WORKFLOWS[step["wf"]]["slug"], step["n"])


def build_page(step, template):
    wf = C.WORKFLOWS[step["wf"]]
    heading = "Step %02d — %s" % (step["n"], step["name"])
    content = "\n".join(render_part(p) for p in step["parts"])

    links = []
    if step["n"] > 1:
        links.append('      <a class="step-nav__link step-nav__prev" '
                      'href="%s-%02d.html">&larr; Previous step</a>'
                      % (wf["slug"], step["n"] - 1))
    if step["n"] < wf["total"]:
        links.append('      <a class="step-nav__link step-nav__next" '
                      'href="%s-%02d.html">Next step &rarr;</a>'
                      % (wf["slug"], step["n"] + 1))
    stepnav = '    <nav class="step-nav">\n' + "\n".join(links) + '\n    </nav>'

    kinds = [p[0] for p in step["parts"]]
    scripts = []
    if "raw" in kinds:  # the model-look grid needs the shared accordion
        scripts.append('<script src="assets/accordion.js?v=3" defer></script>')
    if "prompt" in kinds:
        scripts.append('<script src="assets/copy-button.js?v=3" defer></script>')

    html = template
    for token, value in (
        ("{{TITLE}}", esc(heading) + " — Lucid."),
        ("{{BACK_HREF}}", wf["page"]),
        ("{{BACK_LABEL}}", esc(wf["name"])),
        ("{{CATEGORY}}", esc(wf["name"])),
        ("{{HEADING}}", esc(heading)),
        ("{{CONTENT}}", content),
        ("{{STEPNAV}}", stepnav),
        ("{{SCRIPTS}}", "\n".join(scripts)),
    ):
        html = html.replace(token, value)
    return html


def build_grid(wf_key):
    wf = C.WORKFLOWS[wf_key]
    cards = []
    for step in [s for s in C.STEPS if s["wf"] == wf_key]:
        cards.append(
            '  <a class="step-card" href="%s-%02d.html">\n'
            '    <span class="step-card__num">Step %02d</span>\n'
            '    <span class="step-card__name">%s</span>\n'
            '    <span class="step-card__summary">%s</span>\n'
            '  </a>' % (wf["slug"], step["n"], step["n"],
                        esc(step["name"]), esc(step["summary"])))
    return '<div class="step-grid">\n' + "\n".join(cards) + '\n</div>'


def main():
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]

    with open(os.path.join(HERE, "template.html"), encoding="utf-8") as f:
        template = f.read()

    written = 0
    for step in C.STEPS:
        if only and only != "%s-%d" % (step["wf"], step["n"]):
            continue
        fn = step_filename(step)
        with open(os.path.join(ROOT, fn), "w", encoding="utf-8") as f:
            f.write(build_page(step, template))
        print("wrote", fn)
        written += 1

    if not only:
        for wf_key in C.WORKFLOWS:
            path = os.path.join(HERE, "_grid-%s.html" % wf_key)
            with open(path, "w", encoding="utf-8") as f:
                f.write(build_grid(wf_key) + "\n")
            print("wrote grid snippet", os.path.relpath(path, ROOT))

    print("done — %d step page(s) written" % written)


if __name__ == "__main__":
    main()
