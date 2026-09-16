#!/usr/bin/env python3
"""Render the contribution activity graph as a committed SVG asset.

Same reasoning as the streak card next to it: a hosted renderer is called at
page-view time, and when it is slow or down GitHub's image proxy caches the
failure. The endpoint this replaced now answers 402 permanently. Generating the
SVG in CI removes the page-view dependency entirely.

Usage:
    activity_graph.py <login> <output.svg>   # needs GITHUB_TOKEN
    activity_graph.py --self-check
"""

import json
import os
import sys
import urllib.request

W, H = 495, 195
PAD_L, PAD_R, PAD_T, PAD_B = 40, 16, 44, 26
BG, BORDER, LINE, POINT, TITLE, LABEL, GRID = (
    "#0B1020", "#1E2A44", "#22D3EE", "#A78BFA", "#22D3EE", "#8FA3BF", "#1E2A44",
)
FONT = '"Segoe UI", Ubuntu, sans-serif'
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
# Minimum gap between month labels, so a 495px axis does not collide with itself.
LABEL_GAP = 62

QUERY = """query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks { firstDay contributionDays { contributionCount } }
      }
    }
  }
}"""


def fetch_weeks(login, token):
    """Return [(first_day, total)] for each week of the trailing year."""
    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}",
                 "Content-Type": "application/json",
                 "User-Agent": "daezoxx-profile-activity-graph"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if "errors" in payload:
        raise SystemExit(f"GitHub API error: {payload['errors']}")
    weeks = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [(w["firstDay"], sum(d["contributionCount"] for d in w["contributionDays"]))
            for w in weeks]


def render(weeks, title="Contribution Activity"):
    if len(weeks) < 2:
        raise ValueError("need at least two weeks of data to draw a line")

    plot_w, plot_h = W - PAD_L - PAD_R, H - PAD_T - PAD_B
    peak = max(1, max(total for _, total in weeks))
    step = plot_w / (len(weeks) - 1)

    def x(i):
        return PAD_L + step * i

    def y(total):
        return PAD_T + plot_h * (1 - total / peak)

    points = [(x(i), y(total)) for i, (_, total) in enumerate(weeks)]
    line = " ".join(f"{px:.1f},{py:.1f}" for px, py in points)
    baseline = PAD_T + plot_h
    area = (f"M{points[0][0]:.1f},{baseline:.1f} L"
            + " L".join(f"{px:.1f},{py:.1f}" for px, py in points)
            + f" L{points[-1][0]:.1f},{baseline:.1f} Z")

    parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' "
        f"viewBox='0 0 {W} {H}' role='img'>",
        "<defs><linearGradient id='fill' x1='0' y1='0' x2='0' y2='1'>"
        f"<stop offset='0%' stop-color='{LINE}' stop-opacity='0.35'/>"
        f"<stop offset='100%' stop-color='{LINE}' stop-opacity='0'/>"
        "</linearGradient></defs>",
        f"<rect width='{W}' height='{H}' rx='10' fill='{BG}' stroke='{BORDER}'/>",
        f"<text x='{PAD_L - 16}' y='26' fill='{TITLE}' font-family='{FONT}' "
        f"font-size='14' font-weight='600'>{title}</text>",
        f"<text x='{W - PAD_R}' y='26' fill='{LABEL}' font-family='{FONT}' "
        f"font-size='10' text-anchor='end'>weekly totals, past year</text>",
    ]

    for fraction in (0, 0.5, 1):
        value = peak * fraction
        gy = y(value)
        parts.append(f"<line x1='{PAD_L}' y1='{gy:.1f}' x2='{W - PAD_R}' y2='{gy:.1f}' "
                     f"stroke='{GRID}' stroke-width='1'/>")
        parts.append(f"<text x='{PAD_L - 6}' y='{gy + 3:.1f}' fill='{LABEL}' "
                     f"font-family='{FONT}' font-size='9' text-anchor='end'>{round(value)}</text>")

    parts.append(f"<path d='{area}' fill='url(#fill)'/>")
    parts.append(f"<polyline points='{line}' fill='none' stroke='{LINE}' "
                 "stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/>")
    for px, py in points:
        parts.append(f"<circle cx='{px:.1f}' cy='{py:.1f}' r='1.6' fill='{POINT}'/>")

    last_label, previous_month = -LABEL_GAP, None
    for i, (first_day, _) in enumerate(weeks):
        month = int(first_day[5:7])
        if month != previous_month and x(i) - last_label >= LABEL_GAP:
            parts.append(f"<text x='{x(i):.1f}' y='{H - 9}' fill='{LABEL}' "
                         f"font-family='{FONT}' font-size='9' text-anchor='middle'>"
                         f"{MONTHS[month - 1]}</text>")
            last_label = x(i)
        previous_month = month

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def self_check():
    weeks = [(f"2025-{(i // 4) % 12 + 1:02d}-0{i % 4 + 1}", i % 17) for i in range(53)]
    svg = render(weeks)
    assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
    assert svg.count("<circle") == 53, "one marker per week"
    assert "nan" not in svg.lower(), "no NaN coordinates"
    # Every drawn coordinate stays inside the canvas.
    import re
    for value in re.findall(r"c[xy]='([\d.]+)'", svg):
        assert 0 <= float(value) <= max(W, H)
    # A flat series must not divide by zero and must sit on the baseline.
    flat = render([("2025-01-01", 0), ("2025-01-08", 0)])
    assert f"cy='{H - PAD_B:.1f}'" in flat, flat
    print("self-check ok")


if __name__ == "__main__":
    if "--self-check" in sys.argv:
        self_check()
    else:
        login, output = sys.argv[1], sys.argv[2]
        token = os.environ["GITHUB_TOKEN"]
        with open(output, "w") as handle:
            handle.write(render(fetch_weeks(login, token)))
