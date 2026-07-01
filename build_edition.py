#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the CORRECTED 2026 edition of the Horizon Comparative Analysis.

Produces a single self-contained HTML file that is visually/structurally
identical to Horizon_Comparative_Analysis_UNBIASED_2026.html (per
Comparative_Analysis_DESIGN_SPEC.md) but fed the CORRECTED data from the
multi-agent audit:

  * Same-spec normalization applied CONSISTENTLY (spec 6.3) — accuracy by
    guarantee, trigger by trigger model — removing the one-directional
    Accuracy inflation the audit found (Recommendation 1).
  * Verified factual spec corrections (Fierce CT Rival XP -> Ti/C3 carbon/
    0.5 MOA/6 lb; Christensen MPR real 6.9 lb; chambering undercounts;
    Seekins real published MSRPs) (Recommendation 2).
  * Current 2026-07-01 MSRPs for every rifle (Horizon + competitors).
  * A NEW section — 04 / DELIVERY — the customer-sentiment / promise-vs-
    delivery lens, kept on the same visual system.

Reuses the original file's exact <style> block, embedded logo, and the 14
Horizon photos, so the skin is byte-identical. All numeric changes are either
(a) reproducible from a stated rule or (b) an anchored factual override listed
in BUILD_NOTES.md — nothing is invented.
"""
import re, json, math, html as ihtml

SRC = "Horizon_Comparative_Analysis_UNBIASED_2026.html"
OUT = "Horizon_Comparative_Analysis_UNBIASED_2026_CORRECTED.html"

raw = open(SRC, encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", raw, re.S).group(1)
HERO = dict(re.findall(r'<img alt="([^"]*)" src="(data:image/[^"]+)"', raw))

# ------------------------------------------------------------------ scoring
W = dict(acc=.20, feat=.15, wt=.15, stock=.12, cham=.10, barrel=.09, trig=.09, mag=.05, val=.05)
ORDER = [("acc","Accuracy","20%"),("feat","Accessories","15%"),("wt","Weight / Handling","15%"),
         ("stock","Stock / Chassis","12%"),("cham","Caliber / chambering","10%"),
         ("barrel","Barrel","9%"),("trig","Trigger","9%"),("mag","Magazine","5%"),("val","Value (MSRP)","5%")]
KEYS = [k for k,_,_ in ORDER]
def total(s): return round(sum(s[k]*W[k] for k in W), 2)

# ------------------------------------------------ base data parsed from original
pages = re.split(r'<section class="page', raw)[1:]
ROWLBL = ['Accuracy 20%','Accessories 15%','Weight / Handling 15%','Stock / Chassis 12%',
          'Caliber / chambering 10%','Barrel 9%','Trigger 9%','Magazine 5%','Value (MSRP) 5%']
def clean1(s): return re.sub(r'\s+',' ', ihtml.unescape(re.sub(r'<[^>]+>',' ', s))).strip()

HZ, MATCH, CS, HERO_META, ORD_MODELS = {}, {}, {}, {}, []
for p in pages:
    if 'class="matrix"' not in p: continue
    name = clean1(re.search(r'class="name">(.*?)</div>', p, re.S).group(1))
    ORD_MODELS.append(name)
    tb = re.search(r'<table class="matrix">.*?<tbody>(.*?)</tbody>', p, re.S).group(1)
    rowvals = {}
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', tb, re.S):
        cells = [clean1(c) for c in re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)]
        if cells: rowvals[cells[0]] = cells[1:]
    thead = re.search(r'<thead>(.*?)</thead>', p, re.S).group(1)
    cols = [clean1(t) for t in re.findall(r'<th[^>]*>(.*?)</th>', thead, re.S)][1:]
    comps = cols[1:]
    HZ[name] = {k: float(rowvals[l][0]) for k,l in zip(KEYS, ROWLBL)}
    MATCH[name] = comps
    for ci,c in enumerate(comps, 1):
        if c not in CS: CS[c] = {k: float(rowvals[l][ci]) for k,l in zip(KEYS, ROWLBL)}
    fam = re.search(r'MODEL \d+ · ([^<]+)</span>', p).group(1).strip()
    ch = re.search(r'class="chamber">(.*?)</div>', p, re.S).group(1)
    parts = re.split(r'<br\s*/?>', ch)
    cham = clean1(parts[0]).replace('Chamberings:','').strip(': ').strip()
    barrel = clean1(parts[1]).replace('Barrel:','').strip(': ').strip() if len(parts)>1 else ''
    HERO_META[name] = dict(fam=fam, cham=cham, barrel=barrel,
        eyebrow=clean1(re.search(r'class="eyebrow">(.*?)</div>', p, re.S).group(1)),
        spec=clean1(re.search(r'class="role">(.*?)</div>', p, re.S).group(1)))

# ------------------------------------------------------------- CORRECTION LAYER
def acc_for(name):
    if name.startswith("Seekins"): return 8.5   # 1.0 claim + per-rifle fired test target (demonstrated proof, +1 tier)
    if name.startswith("Fierce"):  return 8.5 if "Carbon Rogue" in name else 9.0   # Rogue .75; rest .5 incl CT Rival XP (corrected)
    return 8.0                                   # Bergara / Christensen 1.0 claim
def trig_for(name):
    if name == "Seekins HIT Pro M3": return 9.5   # TriggerTech Diamond
    if name.startswith("Seekins"):  return 9.0   # PH3 / NRL(Primary, corrected) / Element = TriggerTech
    if name.startswith("Fierce"):   return 9.0   # TriggerTech (Bix'n Andy on Rogue-family unverified in our audit -> conservative)
    if name.startswith("Bergara"):  return 9.0 if "Premier" in name else 8.0   # Premier=TT; B-14=Performance
    return 9.0                                   # Christensen = TriggerTech
OVERRIDES = {   # documented, anchored factual corrections (see BUILD_NOTES.md)
 "Fierce CT Rival XP":       {"barrel":8.7, "wt":8.9, "cham":8.2},  # Ti action + C3 carbon barrel + 0.5 MOA + 6 lb; 7 chamberings
 "Christensen MPR":          {"wt":8.6, "cham":8.8},                # real 6.9 lb (not 8-10); 12 chamberings
 "Seekins Element M3":       {"cham":9.0},                          # verified 10 chamberings
 "Bergara Premier Cima Pro": {"cham":8.8},                          # verified 9 incl 22/25 Creedmoor
 "Fierce Reaper H-TAC 2.0":  {"cham":8.6},                          # verified 10 chamberings
 "Fierce MTN Reaper 2.0":    {"cham":8.6},                          # verified 10 chamberings
 "Seekins HIT Pro M3":       {"val":8.2},                           # real $2,400 (report est ~$2,800)
 "Seekins Havak PH3 NRL":    {"val":8.0},                           # real $2,295 published
}
for n,d in HZ.items():
    d["acc"] = 9.0                               # every Horizon rifle: 0.5 MOA guarantee
    d["trig"] = 9.5 if n == "Venatic Riff" else 9.0   # Riff SBR ships TriggerTech Diamond
for c,d in CS.items():
    d["acc"] = acc_for(c); d["trig"] = trig_for(c)
    for k,v in OVERRIDES.get(c, {}).items(): d[k] = v

# ------------------------------------------------ competitor display / pricing
COMP_PRICE = {  # current 2026-07-01 published MSRP (numeric), see PRICE_REFERENCE.md
 "Seekins Havak PH3":1895, "Seekins Havak PH3 NRL":2295, "Seekins Element M3":2895, "Seekins HIT Pro M3":2400,
 "Fierce Carbon Rogue":2150, "Fierce CT Rival XP":2999, "Fierce Carbon Rage LR":3450,
 "Fierce MTN Reaper 2.0":3199, "Fierce Reaper H-TAC 2.0":2699,
 "Bergara Premier Cima Pro":3099, "Bergara Premier MgLite":3099, "Bergara B-14 Sq. Crest":1879,
 "Bergara B-14 Wilderness":1099, "Bergara Premier LRP":2000, "Bergara B-14 Ridge (450 BM)":999,
 "Christensen Ridgeline FFT Ti":2549.99, "Christensen Mesa FFT":1499.99, "Christensen MPR":2299.99,
 "Christensen Ridgeline":2049.99, "Christensen Mesa FFT (450 BM)":1499.99,
}
def money(n):
    return ("${:,.2f}".format(n)) if (n % 1) else ("${:,d}".format(int(n)))
def comp_msrp_str(col):
    s = money(COMP_PRICE[col])
    if col == "Bergara Premier LRP": return "≈"+s+" (disc.)"
    return s
DISPLAY = {"Bergara Premier LRP": "Bergara Premier LRP †"}
def disp(col): return DISPLAY.get(col, col)

HZ_PRICE = {  # current base MSRP (numeric)
 "Venatic Carbon 2":3999, "Venatic 2":3799, "Venatic DM":4499, "Vandal Prime 2":2999,
 "Vandal Carbon 2":3399, "Vandal DM":2999, "Venatic Riff":3799, "Venatic Max":3999,
 "Vandal 2":2299, "Vandal X":2799, "Vandal Dark II":2999, "Villain":2499,
 "Vandal Bloodline":2799, "Vena-Bull":9999,
}

# ------------------------------------------------------------------ engine
def ranked(m):
    rows = [("H", m, HZ[m], total(HZ[m]))] + [("C", c, CS[c], total(CS[c])) for c in MATCH[m]]
    return sorted(rows, key=lambda r: r[3], reverse=True)
def crit_leader(m, key):
    rows = [(m, HZ[m][key], True)] + [(disp(c), CS[c][key], False) for c in MATCH[m]]
    return max(rows, key=lambda r: r[1])
IDX = sorted(range(len(ORD_MODELS)), key=lambda i: total(HZ[ORD_MODELS[i]]), reverse=True)
RANK = {ORD_MODELS[i]: r+1 for r, i in enumerate(IDX)}   # overall rank by Horizon total
HZ_WINS = sum(1 for m in ORD_MODELS if ranked(m)[0][1] == m)

# ------------------------------------------------------------------ html helpers
def esc(s): return ihtml.escape(s)
def two_line(name):
    parts = name.split(" ", 1)
    return parts[0] + ("<br>" + parts[1] if len(parts) > 1 else "")
def runhead(tag):
    return ('<div class="runhead"><span class="brand">Horizon Firearms · Comparative Catalog</span>'
            f'<span class="tag">{tag}</span></div>')
def foot(right):
    return ('<div class="foot"><span>COMPARATIVE ANALYSIS — PUBLISHED-SPEC BASIS</span>'
            f'<span>{right}</span></div>')

# ------------------------------------------------------------------ pages
P = []

# ---- 1. COVER
n_rivals = len(CS)
P.append(f'''<section class="page cover"><div class="grid"></div><div class="sun"></div><div class="horizonline"></div>
<div class="cover-inner">
  <div class="coverbadge"><span class="coverlogo"></span></div>
  <div class="kicker">COMPARATIVE ANALYSIS · BOLT-ACTION RIFLES · 2026 · CORRECTED EDITION</div>
  <h1>Benchmark<span class="thin">re-scored with the rule applied to everyone</span></h1>
  <div class="sub">
    <p>A like-for-like comparison of every Horizon Core Series rifle against its nearest current-production rivals from Fierce, Seekins, Christensen Arms, and Bergara. This corrected edition applies the report's own same-spec scoring rule <b>consistently</b> — an identical guarantee earns an identical score for every brand, Horizon included — and refreshes every price and contested spec against live 2026 manufacturer sources.</p>
    <p>Where a competitor wins, it is named and ranked first. After correction, Horizon tops <b>{HZ_WINS} of {len(ORD_MODELS)}</b>.</p>
  </div>
  <div class="meta">
    <div><b>{n_rivals} Rivals</b>current production, role-matched</div>
    <div><b>9 Criteria</b>identical for every brand</div>
    <div><b>Live MSRP</b>pulled 2026-07-01</div>
  </div>
</div></section>''')

# ---- 2. METHOD & NEUTRALITY
crit_rows = "".join(
    f'<tr><td class="crit">{lab}</td><td class="w">{wt}</td><td>{desc}</td></tr>'
    for (k,lab,wt),desc in zip(ORDER, [
      "Published accuracy guarantee, scored by the guarantee tier — identical guarantees score identically. A maker shipping a per-rifle fired test target (demonstrated proof) is credited one tier above an unverified claim.",
      "Rails, bases, muzzle devices, bottom metal, bundled extras and configurability included as delivered.",
      "Carry weight and balance for the rifle's role; lighter is rewarded where the class calls for it.",
      "Stock or chassis quality, adjustability, material and fit for purpose.",
      "Breadth of factory chamberings actually offered on the model.",
      "Barrel maker, material (carbon vs steel), profile and finish.",
      "Trigger scored by trigger model — the same trigger earns the same score for every brand.",
      "Magazine type, capacity, feed reliability and bottom-metal design.",
      "MSRP value at the model's live 2026 price — weighted 5% by design (see neutrality note).",
    ]))
P.append(f'''<section class="page">
  {runhead("METHOD &amp; NEUTRALITY")}
  <div class="lead-num">01 / METHOD</div><h2 class="sect">How every rifle is scored</h2>
  <p class="intro">Each Horizon model is compared with the closest current-production rival from each competitor brand, matched on role/class and barrel construction. Every rifle — Horizon included — is scored on the same nine 0–10 criteria with fixed weights (below) and no brand weighting; the weighted total is the dot-product of scores and weights. This corrected edition changes none of that machinery. It changes the <b>inputs</b>: the same-spec rule below is now applied to Horizon exactly as to rivals, and every price and contested spec is refreshed against live 2026 sources.</p>
  <div class="rubric">
    <div class="rcell"><div class="swatch b0"></div><div class="band">0</div><div class="lab">No relevant offering</div></div>
    <div class="rcell"><div class="swatch b1"></div><div class="band">1–3</div><div class="lab">Poor — clear shortfall</div></div>
    <div class="rcell"><div class="swatch b4"></div><div class="band">4–6</div><div class="lab">Average to good</div></div>
    <div class="rcell"><div class="swatch b7"></div><div class="band">7</div><div class="lab">Good — no real caveat</div></div>
    <div class="rcell"><div class="swatch b8"></div><div class="band">8</div><div class="lab">Good, with added value</div></div>
    <div class="rcell"><div class="swatch b9"></div><div class="band">9</div><div class="lab">Very good — significant value</div></div>
    <div class="rcell"><div class="swatch b10"></div><div class="band">10</div><div class="lab">Excellent &amp; exceptional</div></div>
  </div>
  <table class="spec"><thead><tr><th style="width:22%">Criterion</th><th class="w" style="width:8%">Weight</th><th>What it rewards (applied identically to all brands)</th></tr></thead>
  <tbody>{crit_rows}</tbody></table>
  <div class="disc">NEUTRALITY &amp; WHAT CHANGED — This edition enforces the report's own stated rule that <b>a guarantee is a claim, not a measurement</b>, and applies it in both directions: an identical 0.5 MOA guarantee now scores identically for Horizon and Fierce (both 9.0), and an identical trigger scores identically for every brand. The prior edition credited Horizon +0.2–0.6 on the 20%-weighted Accuracy criterion that no rival with an equal guarantee received; that single-direction edge is removed here. Verified spec corrections are also applied (Fierce CT Rival XP is titanium / C3 carbon / 0.5 MOA / 6 lb; Christensen MPR is 6.9 lb, not 8–10; Seekins publishes MSRP; several chambering counts were low). <b>Value remains weighted 5%</b> — a disclosed choice that structurally mutes price; because Horizon is the highest-priced brand in most matchups, the real purchase-price gaps (hundreds of dollars, see spreads) are larger than that 5% conveys.</div>
</section>''')

# ---- 3. RESULTS INDEX
idx_rows = ""
for i in IDX:
    m = ORD_MODELS[i]; r = ranked(m); win = r[0]; hz = total(HZ[m])
    hzwin = win[1] == m
    wname = m if hzwin else disp(win[1])
    pill = ('<span class="pill win">Horizon tops</span>' if hzwin
            else f'<span class="pill edge">{esc(wname.split(" ",1)[0])} tops</span>')
    idx_rows += (f'<tr><td class="num">{RANK[m]}</td><td class="model">{esc(m)}</td>'
                 f'<td class="msrp">{money(HZ_PRICE[m])}</td><td class="score">{hz:.2f}</td>'
                 f'<td>{esc(wname)} ({win[3]:.2f})</td><td>{pill}</td></tr>')
P.append(f'''<section class="page">
  {runhead("RESULTS INDEX")}
  <div class="lead-num">02 / RESULTS</div><h2 class="sect">Every matchup, honest winner</h2>
  <p class="intro">With the same-spec rule applied consistently and specs/prices corrected, Horizon takes the top weighted score in <b>{HZ_WINS} of {len(ORD_MODELS)}</b> matchups — its genuine wins are the premium broad-chambering hunters (Venatic Carbon 2, Venatic 2) plus the uncontested-niche Vandal Bloodline. Vandal Prime 2 is now a coin-flip that tips to Fierce. Elsewhere a correctly-weighed Fierce, Seekins or Christensen leads. This is the paper picture; the delivery lens (04 / DELIVERY) tells a very different story.</p>
  <table class="index"><thead><tr><th>#</th><th>Horizon model</th><th class="msrp">MSRP</th><th class="score">Horizon</th><th>Top-scoring rifle in matchup</th><th>Result</th></tr></thead>
  <tbody>{idx_rows}</tbody></table>
  <div class="note">Ranked by the Horizon model's own weighted score, highest first. "Top-scoring rifle" is the highest weighted total in that matchup after correction. † = discontinued rival retained as legacy analog (no current-production replacement in class). Scores reflect published specifications, not measured performance.</div>
</section>''')

# ---- 4..17 MODEL SPREADS
def result_bar(m):
    hz = total(HZ[m]); r = ranked(m)
    rival = next(x for x in r if x[1] != m)  # highest-scoring competitor
    rv = rival[3]; rname = disp(rival[1])
    ticks = ""
    for pos,lab in [(0,"0"),(30,"3"),(60,"6"),(70,"7"),(80,"8"),(90,"9"),(100,"10")]:
        ticks += f'<div class="tick" style="left:{pos}%"></div><div class="ticklab" style="left:{pos}%">{lab}</div>'
    return f'''<div class="railwrap">
  <div class="rtitle"><span class="t">Weighted result — Horizon vs. leading competitor</span><span class="v">{hz:.2f}</span></div>
  <div class="rail">
    <div class="track"><i class="s0 b0"></i><i class="s13 b1"></i><i class="s46 b4"></i><i class="s7 b7"></i><i class="s8 b8"></i><i class="s9 b9"></i><i class="s10 b10"></i></div>
    {ticks}
    <div class="cmark" style="left:{rv*10:.1f}%"><span class="dot"></span><span class="ml">{esc(rname)} {rv:.2f}</span></div>
    <div class="hmark" style="left:{hz*10:.1f}%"><span class="ml">{esc(m)} {hz:.2f}</span><span class="dot"></span></div>
  </div>
  <div class="legend-line"><span class="h"><b></b>{esc(m)} (Horizon)</span><span class="c"><b></b>{esc(rname)} (best rival)</span></div>
</div>'''

def matrix(m):
    cols = MATCH[m]
    hz = HZ[m]
    head = f'<th class="c1">Criterion <span class="w">/ weight</span></th><th class="hz">{two_line(m)}</th>'
    head += "".join(f'<th>{two_line(disp(c))}</th>' for c in cols)
    body = ""
    for k,lab,wt in ORDER:
        vals = [(hz[k], True)] + [(CS[c][k], False) for c in cols]
        best = max(v for v,_ in vals)
        row = f'<td class="c1">{lab} <span class="w">{wt}</span></td>'
        for v,ishz in vals:
            cls = "num hz" if ishz else "num"
            if abs(v-best) < 1e-9: cls += " best"
            row += f'<td class="{cls}">{v:.1f}</td>'
        body += f"<tr>{row}</tr>"
    tots = [(total(hz), True)] + [(total(CS[c]), False) for c in cols]
    win = max(t for t,_ in tots)
    trow = '<td class="c1">Weighted total</td>'
    for t,ishz in tots:
        cls = "num hz" if ishz else "num"
        if abs(t-win) < 1e-9: cls += " win"
        trow += f'<td class="{cls}">{t:.2f}</td>'
    body += f'<tr class="total">{trow}</tr>'
    return f'<table class="matrix"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'

def leaders(m):
    out = ""
    for key,lab in [("acc","Accuracy"),("cham","Chamberings"),("wt","Weight"),("trig","Trigger"),("val","Value")]:
        who,sc,_ = crit_leader(m, key)
        out += f'<li><b>{lab}:</b> {esc(who)} ({sc:.1f})</li>'
    return f'<ul class="leadlist">{out}</ul>'

def analyst_note(m):
    r = ranked(m); hz = total(HZ[m]); n = len(r)
    hzrank = next(i for i,x in enumerate(r,1) if x[1] == m)
    if r[0][1] == m:
        second = r[1]
        lead = f'The {m} posts the top weighted score here ({hz:.2f} of 10), ahead of {esc(disp(second[1]))} ({second[3]:.2f}).'
    else:
        w = r[0]
        lead = f'{esc(disp(w[1]))} posts the top weighted score ({w[3]:.2f}); the {m} ranks #{hzrank} of {n} at {hz:.2f}.'
    ranks = sorted(KEYS, key=lambda k: HZ[m][k], reverse=True)
    lab = {k:l.lower() for k,l,_ in ORDER}
    top = f"{lab[ranks[0]]} ({HZ[m][ranks[0]]:.1f}) and {lab[ranks[1]]} ({HZ[m][ranks[1]]:.1f})"
    bot = f"{lab[ranks[-1]]} ({HZ[m][ranks[-1]]:.1f}) and {lab[ranks[-2]]} ({HZ[m][ranks[-2]]:.1f})"
    return (f'{lead} The Horizon model rates highest on {top} and lowest on {bot}. '
            f'Scores reflect published specifications, not measured performance.')

LRP_NOTE = " † Bergara Premier LRP is discontinued; its last-published spec is retained only as a legacy analog (no current-production Bergara replacement in this class)."
for i in IDX:
    m = ORD_MODELS[i]; meta = HERO_META[m]; r = ranked(m); win = r[0]
    wname = m if win[1]==m else disp(win[1])
    comp_note = " · ".join(f"{esc(disp(c))} {comp_msrp_str(c)}" for c in MATCH[m])
    extra = LRP_NOTE if any(c=="Bergara Premier LRP" for c in MATCH[m]) else ""
    img = HERO.get(m, "")
    P.append(f'''<section class="page">
  {runhead(f"MODEL {RANK[m]:02d} · {meta['fam']}")}
  <div class="hero">
    <div>
      <div class="eyebrow">{esc(meta['eyebrow'])}</div>
      <div class="name">{esc(m)}</div>
      <div class="role">{esc(meta['spec'])}</div>
      <div class="price">MSRP <b>{money(HZ_PRICE[m])}</b></div>
      <div class="chamber"><b>Chamberings:</b> {esc(meta['cham'])}<br><b>Barrel:</b> {esc(meta['barrel'])}</div>
    </div>
    <div>
      <span class="shot"><img alt="{esc(m)}" src="{img}"></span>
      <div class="specline">Horizon image (official). Competitors shown spec-only. <b>Top weighted score: {esc(wname)} ({win[3]:.2f}).</b></div>
    </div>
  </div>
  {result_bar(m)}
  {matrix(m)}
  <div class="callouts">
    <div class="callout"><h4>Category leaders</h4>{leaders(m)}</div>
    <div class="callout edge"><h4>Analyst note</h4><p>{analyst_note(m)}</p></div>
  </div>
  <div class="note">COMPETITOR MSRP (MSRP vs MSRP): {comp_note}. Current-production models only, live 2026-07-01.{extra}</div>
  {foot(f"{m.upper()} · P.{RANK[m]+3:02d}")}
</section>''')

# ---- 18. FIELD MAP (scatter)
def build_scatter():
    x0,y0,x1,y1 = 60,26,704,384
    pts = []  # (price, total, is_hz, rank, brand)
    for m in ORD_MODELS:
        pts.append((HZ_PRICE[m], total(HZ[m]), True, RANK[m], "HZ"))
    for c in CS:
        brand = next(b for b in ("Seekins","Fierce","Bergara","Christensen") if c.startswith(b))
        pts.append((COMP_PRICE[c], total(CS[c]), False, None, brand))
    tmin = min(p[1] for p in pts); tmax = max(p[1] for p in pts)
    ylo = min(7.0, tmin-0.1); yhi = max(9.0, tmax+0.1)
    def X(price): return x0 + (math.log10(price)-3)*(x1-x0)
    def Y(t): return y0 + (1-(t-ylo)/(yhi-ylo))*(y1-y0)
    BC = {"Seekins":"#2B2D30","Fierce":"#7A7A7A","Bergara":"#B3B3B3","Christensen":"#4F4F4F"}
    svg = [f'<svg viewBox="0 0 724 412" style="width:100%;border:1px solid var(--line);background:#fff">']
    # x gridlines
    for pr in (1000,1500,2000,3000,5000,10000):
        x = X(pr); lab = "$%gk" % (pr/1000)
        svg.append(f'<line x1="{x:.1f}" y1="{y0}" x2="{x:.1f}" y2="{y1}" stroke="rgba(26,26,26,.08)"/>')
        svg.append(f'<text x="{x:.1f}" y="{y1+14}" font-family="JetBrains Mono" font-size="9" fill="#6E6E6E" text-anchor="middle">{lab}</text>')
    svg.append(f'<text x="{(x0+x1)/2:.0f}" y="{y1+30}" font-family="Oswald" font-size="10" letter-spacing="1" fill="#444" text-anchor="middle" text-transform="uppercase">MSRP — LOG SCALE</text>')
    # y gridlines every .5
    yy = math.ceil(ylo*2)/2
    while yy <= yhi+1e-9:
        y = Y(yy)
        svg.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="rgba(26,26,26,.08)"/>')
        svg.append(f'<text x="{x0-8}" y="{y+3:.1f}" font-family="JetBrains Mono" font-size="9" fill="#6E6E6E" text-anchor="end">{yy:.1f}</text>')
        yy += 0.5
    svg.append(f'<text transform="translate(16,{(y0+y1)/2:.0f}) rotate(-90)" font-family="Oswald" font-size="10" letter-spacing="1" fill="#444" text-anchor="middle">WEIGHTED SCORE</text>')
    # competitors first
    for pr,t,ishz,rk,br in pts:
        if ishz: continue
        svg.append(f'<circle cx="{X(pr):.1f}" cy="{Y(t):.1f}" r="4.2" fill="{BC[br]}" stroke="#fff" stroke-width="0.8"/>')
    for pr,t,ishz,rk,br in pts:
        if not ishz: continue
        x=X(pr); y=Y(t)
        svg.append(f'<rect x="{x-6:.1f}" y="{y-6:.1f}" width="12" height="12" fill="#E8742C" stroke="#fff" stroke-width="1" transform="rotate(45 {x:.1f} {y:.1f})"/>')
        svg.append(f'<text x="{x:.1f}" y="{y+2.6:.1f}" font-family="JetBrains Mono" font-size="7.5" fill="#fff" text-anchor="middle">{rk}</text>')
    svg.append('</svg>')
    return "".join(svg)

leg = ('<div class="scatleg">'
       '<div class="lg"><i style="background:#E8742C;border-radius:0;transform:rotate(45deg)"></i>Horizon</div>'
       '<div class="lg"><i style="background:#2B2D30"></i>Seekins</div>'
       '<div class="lg"><i style="background:#7A7A7A"></i>Fierce</div>'
       '<div class="lg"><i style="background:#B3B3B3"></i>Bergara</div>'
       '<div class="lg"><i style="background:#4F4F4F"></i>Christensen</div></div>')
scatkey = "".join(f'<li><b>{RANK[ORD_MODELS[i]]}</b> {esc(ORD_MODELS[i])}</li>' for i in IDX)
total_rifles = len(ORD_MODELS) + len(CS)
P.append(f'''<section class="page">
  {runhead("FIELD MAP")}
  <div class="lead-num">03 / FIELD MAP</div><h2 class="sect">Price vs. weighted score</h2>
  <p class="intro">All {total_rifles} current-production rifles plotted by live MSRP (log scale) against their corrected weighted score. Horizon models are orange diamonds, numbered by overall rank; competitors are grey by brand. The vertical spread is compressed — after correcting the Accuracy inflation, the field is tightly packed on paper — while the horizontal spread (price) is wide: Horizon sits to the right (more expensive) at nearly every score band.</p>
  {leg}
  {build_scatter()}
  <div class="scatkeywrap"><div class="scatkeyhead">Horizon models by rank</div><ol class="scatkey">{scatkey}</ol></div>
  {foot(f"FIELD MAP · P.{len(P)+1:02d}")}
</section>''')

# ---- NEW: 04 / DELIVERY (customer sentiment)
SENT = [  # brand, acc, build, cs, val, rep, composite, confidence
 ("Horizon", 8.0,7.5,7.5,8.0,8.0,7.75,"Low–Med (~17)"),
 ("Seekins", 7.0,6.0,7.0,8.0,7.5,6.85,"Med (~70)"),
 ("Bergara", 7.0,6.5,5.5,8.5,7.0,6.70,"Med–High (~55)"),
 ("Christensen",6.0,4.5,5.0,5.0,4.5,5.10,"Med–High (~85)"),
 ("Fierce",  6.0,5.0,4.0,5.0,4.5,5.05,"Med (~48)"),
]
srows = ""
for b,a,bu,cs,va,rp,comp,conf in SENT:
    hz = ' class="win"' if b=="Horizon" else ''
    srows += (f'<tr><td class="model">{b}</td><td class="num">{a:.1f}</td><td class="num">{bu:.1f}</td>'
              f'<td class="num">{cs:.1f}</td><td class="num">{va:.1f}</td><td class="num">{rp:.1f}</td>'
              f'<td class="num"{hz}><b>{comp:.2f}</b></td><td class="mono" style="font-size:9px">{conf}</td></tr>')
quad = ('<pre style="font-family:JetBrains Mono;font-size:10px;line-height:1.35;color:#1A1A1A;'
        'background:var(--bone-3);border:1px solid var(--line);padding:12px 14px;margin:8px 0;white-space:pre">'
        '                    DELIVERS  (high owner sentiment)\n'
        '                            ^\n'
        '           Seekins          |          Horizon *\n'
        '        (strong on both)    |     (* thin / low-confidence)\n'
        ' spec-weak &lt;---------------+---------------&gt; spec-strong\n'
        '           Bergara          |          Fierce\n'
        '        (value moat,        |       Christensen\n'
        '         coin-flip CS)      |   (great on paper, gamble in hand)\n'
        '                            v\n'
        '                     GAMBLE  (low owner sentiment)</pre>')
P.append(f'''<section class="page">
  {runhead("DELIVERY · CUSTOMER SENTIMENT")}
  <div class="lead-num">04 / DELIVERY</div><h2 class="sect">Does the market believe each brand delivers?</h2>
  <p class="intro">The spec score above — even corrected — measures only the <b>promise</b> any brand can print. This section measures <b>delivery</b>: five researchers scored real owner sentiment (Rokslide, Snipers Hide, Reddit, Hunt Talk, AR15.com), independent lab/press tests, and warranty/CS signals (BBB, Trustpilot) on five 0–10 dimensions. A separate Confidence rating keeps the data asymmetry honest — Horizon is a low-volume boutique with ~5× less owner data than Christensen or Bergara, so its lead reads as "strong signal, unproven at scale," not a confirmed #1. Kept deliberately separate from the spec score: the two lenses sit on different scales and confidence levels.</p>
  <table class="index"><thead><tr><th>Brand</th><th class="score">Accuracy<br>in practice</th><th class="score">Build &amp;<br>reliability</th><th class="score">Warranty<br>/ CS</th><th class="score">Value<br>sentiment</th><th class="score">Reputation</th><th class="score">Composite</th><th>Confidence (≈ src)</th></tr></thead>
  <tbody>{srows}</tbody></table>
  <div class="note" style="margin-top:6px">Weights: Accuracy-in-practice 30% · Build &amp; reliability 30% · Warranty/CS 20% · Value sentiment 10% · Reputation 10%. Composite = weighted sum.</div>
  {quad}
  <div class="disc">THE INVERSION — The delivery ranking nearly <b>inverts</b> the spec ranking. The two brands strongest on paper (Fierce, Christensen) are the ones owners trust <b>least</b> to honor it: Fierce "roll the dice… shooter or a boat anchor," a $200 fee just to invoke the accuracy guarantee, slow CS (delivery 5.05); Christensen a documented ~25–30% QC "lottery," BBB grade D- (5.10). Seekins is the only rival strong on both axes (6.85). Horizon leads delivery (7.75) on thin data — every reachable source says it shoots the 0.5 MOA promise and buyers return, but there is no large-N check. The universal complaint across all four rivals is unit-to-unit QC variance and warranty friction — precisely the space a trusted-delivery brand can take share from, and the one axis a price-cutter cannot copy.</div>
  {foot(f"DELIVERY · P.{len(P)+1:02d}")}
</section>''')

# ---- APPENDIX A: one page per brand (corrected reference data)
REF = {
 "Seekins Precision": [
  ("Havak PH3","$1,895","Seekins PH3, 3-lug 60° / 416R SS, 16–26\"","TriggerTech 2.5–5 lb","1.0 MOA","AICS-pattern","≈7.0 lb","10: 308W, 22Cr, 25Cr, 6Cr, 6.5Cr, 6.5PRC, 7PRC, 7BC, 300WM, 300PRC"),
  ("Havak PH3 NRL","$2,295","Seekins PH3, 3-lug / 416R SS fluted, 24\"","TriggerTech Primary @2.5 lb","1.0 MOA","AICS-pattern","≈8.5 lb","4 (SA/24\"): 25Cr, 6Cr, 6.5Cr, 6.5PRC"),
  ("Havak Element M3","$2,895","Al/steel hybrid, 3-lug / carbon-wrapped 416R, 16/20/22\"","TriggerTech Primary @2.5 lb","1.0 MOA","AICS-pattern","≈6.0 lb","10: 22Cr, 6Cr, 25Cr, 6.5Cr, 6.5PRC, 308W, 7PRC, 7BC, 300WM, 300PRC"),
  ("Havak HIT Pro M3","$2,400","HIT Pro M3 folding chassis, 3-lug / 416R M24, 18/24\"","TriggerTech Diamond 4–32 oz","1.0 MOA","AICS-pattern, full ARCA","≈9.0 lb","7: .223 Wylde, 22Cr, 6Cr, 25Cr, 6.5Cr, 6.5PRC, 308W"),
 ],
 "Fierce Firearms": [
  ("Carbon Rogue (XP)","$2,150 (start)","Dual-lug SS 70°, DLC bolt / C3 carbon, 18/20/22\"","TriggerTech","0.75 MOA","Rogue C3 carbon stock","≈6.3 lb","11: 22Cr, 6Cr, 25Cr, 6.5Cr, 6.5PRC, 7RM, 7PRC, 7BC, 308W, 300WM, 300PRC"),
  ("CT Rival XP","$2,999","Dual-lug TITANIUM 70°, DLC bolt / C3 carbon, 20/22\"","TriggerTech","0.5 MOA","Rival XP 2.0 carbon, ARCA+Pic","≈6.0 lb","7: 22Cr, 25Cr, 6.5PRC, 280AI, 7BC, 7PRC, 300PRC"),
  ("Carbon Rage LR","$3,450","Tri-lug SS 70°, CRF / C3 carbon, NIX brake, 18–24\"","TriggerTech","0.5 MOA","Rage C3 carbon, ARCA+Pic","≈7.3 lb","10: 22Cr, 6Cr, 25Cr, 6.5Cr, 6.5PRC, 7BC, 7PRC, 28Nos, 300PRC, 338LM"),
  ("MTN Reaper 2.0","$3,199","2-lug Ti/SS 70°, DLC / C3 carbon, 18/20/22\"","TriggerTech","0.5 MOA","Ultra-Lite Mg folding chassis","≈5.6 lb","10: 22Cr, 25Cr, 6.5Cr, 6.5PRC, 7PRC, 7BC, 7RM, 308W, 300WM, 300PRC"),
  ("Reaper H-TAC 2.0","$2,699","2-lug SS 70°, DLC, AICS / C3 carbon, 16–22\"","TriggerTech","0.5 MOA","Carbon + folding alu chassis, ARCA","≈7.8 lb","10: 22Cr, 6.5Cr, 6.5PRC, 280AI, 7RM, 7PRC, 7BC, 308W, 300WM, 300PRC"),
 ],
 "Bergara": [
  ("Premier Cima Pro","$3,099","Premier 416SS, floating bolt head / CURE carbon, 20/22\"","TriggerTech","1.0 MOA","Autoclave carbon stock (5.5 lb SA)","≈5.5 lb","9: 22Cr, 25Cr, 308W, 6.5Cr, 6.5PRC, 300WM, 7RM, 7PRC, 300PRC"),
  ("Premier MgLite","$3,099","Premier, floating bolt head / CURE carbon, 22/24\"","TriggerTech","1.0 MOA","XLR Element 4.0 Mg chassis, folding","≈6.7 lb","6: 308W, 6.5Cr, 6.5PRC, 300WM, 7PRC, 300PRC"),
  ("B-14 Squared Crest","$1,879","B-14 two-lug / 4140 fluted, threaded, 20/22\"","Bergara Performance","1.0 MOA","100% carbon fiber (CF-RTM)","≈6.9 lb","6: 308W, 6.5Cr, 22-250, 6.5PRC, 7PRC, 300WM"),
  ("B-14 Wilderness Ridge","$1,099 (start)","B-14 two-lug / 4140 No.5, threaded, 20–24\"","Bergara Performance","1.0 MOA","Synthetic SoftTouch, camo","≈7.3 lb","8: 308W, 6.5Cr, 6.5PRC, 7PRC, 28Nos, 7RM, 300PRC, 300WM"),
  ("B-14 Ridge (base)","$999","B-14 two-lug / 4140 No.5, 18–24\"","Bergara Performance","1.0 MOA","Synthetic (GRP)","≈7.5 lb","13 incl. 450 Bushmaster, 308W, 6.5Cr, 22-250, 7-08, 6.5PRC"),
  ("Premier LRP †","≈$2,000 (disc.)","Premier / stainless, chassis","TriggerTech","1.0 MOA","Aluminum chassis","≈10.9 lb","Discontinued — legacy analog only"),
 ],
 "Christensen Arms": [
  ("Mesa FFT","$1,499.99","Steel / 416R stainless (no carbon wrap), Featherlight, threaded","TriggerTech","1.0 MOA","FFT carbon Sporter stock","≈5.9 lb","9: 22Cr, 25Cr, 6.5Cr, 6.5PRC, 7RM, 7PRC, 308W, 300WM, 300PRC"),
  ("Ridgeline FFT","$2,049.99","Steel Rem700 fp / 416R SS + carbon wrap, threaded","TriggerTech","1.0 MOA","FFT carbon Sporter stock","≈5.8 lb","24 calibers, 22Cr → 375 H&H"),
  ("Ridgeline FFT Titanium","$2,549.99","TITANIUM receiver / 416R SS + carbon wrap, Ti brake","TriggerTech","1.0 MOA","FFT carbon Sporter stock","≈5.3 lb","13: 22Cr → 300PRC"),
  ("MPR (Modern Precision)","$2,299.99","Steel Rem700 fp, 20 MOA / 416R SS + carbon wrap, Target","TriggerTech","1.0 MOA","7075 alu folding chassis, M-LOK","≈6.9 lb","12: .223, 22Cr, 25Cr, 6ARC, 6Cr, 6.5Cr, 6.5PRC, 7PRC, 308W, 300WM, 300PRC, 338LM"),
  ("Traverse","$2,649.99","Rem700-pattern / 416R SS + carbon wrap, threaded","TriggerTech","1.0 MOA","Carbon Monte-Carlo sporter","≈6.8 lb","14 incl. 22-250, 6.5PRC, 28Nos, 300PRC, 375 H&H"),
 ],
}
A_LEAD = {"Seekins Precision":"Every model referenced in any matchup appears here under its brand. Seekins publishes MSRP on its own product pages (the prior edition's \"MSRP not published — street estimate\" claim was incorrect and inflated Seekins prices 16–32%); the figures below are the exact live-site MSRPs. Seekins also ships a per-rifle fired sub-MOA test target — demonstrated proof credited one accuracy tier above an unverified claim."}
for ai,(brand,rows) in enumerate(REF.items(), 1):
    body = ""
    for model,msrp,build,trig,guar,mag,wt,cham in rows:
        body += (f'<tr><td class="model">{esc(model)}</td><td class="mono">{esc(msrp)}</td><td>{esc(build)}</td>'
                 f'<td>{esc(trig)}</td><td class="mono">{esc(guar)}</td><td>{esc(mag)}</td>'
                 f'<td class="mono">{esc(wt)}</td><td>{esc(cham)}</td></tr>')
    lead = f'<p class="intro">{A_LEAD[brand]}</p>' if brand in A_LEAD else ""
    P.append(f'''<section class="page">
  {runhead("APPENDIX A · COMPETITOR DATA")}
  <div class="lead-num">A{ai} / REFERENCE</div><h2 class="sect">Competitor reference — {esc(brand)}</h2>
  {lead}
  <div class="brandhead">{esc(brand)}</div>
  <table class="reftable"><thead><tr><th>Model</th><th>MSRP</th><th>Action / Barrel</th><th>Trigger</th><th>Guarantee</th><th>Magazine</th><th>Weight</th><th>Chamberings (representative)</th></tr></thead>
  <tbody>{body}</tbody></table>
  <div class="note">MSRP pulled 2026-07-01 from live manufacturer pages. † discontinued — retained as legacy analog only. Weights are published/representative starting figures; caliber and options vary.</div>
  {foot(f"APPENDIX · P.{len(P)+1:02d}")}
</section>''')

# ---- APPENDIX B (Sources & Method)
P.append(f'''<section class="page">
  {runhead("APPENDIX B · SOURCES &amp; METHOD")}
  <div class="lead-num">B / SOURCES</div><h2 class="sect">Sources, corrections &amp; limitations</h2>
  <p class="intro">This corrected edition was produced by an orchestrated multi-agent audit (10 researchers): five web-verified every spec, price and chambering against live 2026 manufacturer sources and tested the prior report against its own scoring rules; five researched owner-delivery sentiment across forums, lab/press tests and warranty signals. Findings were reconciled and the contested matchups recomputed under one consistent ruleset.</p>
  <div class="brandhead">What changed vs. the prior edition</div>
  <ul class="imp">
    <li><b>ACCURACY RULE APPLIED CONSISTENTLY</b> — an identical guarantee now scores identically for every brand (0.5 MOA = 9.0 for Horizon and Fierce alike); demonstrated proof (Seekins' per-rifle test target) is credited one tier above an unverified claim. This removes a one-directional edge worth +0.2–0.6 to Horizon on the 20%-weighted criterion.</li>
    <li><b>TRIGGER BY MODEL</b> — the same trigger earns the same score; Seekins HIT Pro M3 (TriggerTech Diamond) is credited accordingly, PH3 NRL corrected to TriggerTech Primary.</li>
    <li><b>FIERCE CT RIVAL XP RECLASSIFIED</b> — titanium action, full C3 carbon barrel, 0.5 MOA, ~6 lb (the prior "steel / 0.75 MOA / ~7 lb" described a different rifle).</li>
    <li><b>CHRISTENSEN MPR WEIGHT CORRECTED</b> — real ≈6.9 lb, not the "8–10 lb" previously scored.</li>
    <li><b>SEEKINS MSRP</b> — Seekins publishes MSRP; real figures ($1,895 / $2,295 / $2,895 / $2,400) replace the inflated street estimates.</li>
    <li><b>CHAMBERING COUNTS CORRECTED</b> — Seekins Element M3 (10), Bergara Premier Cima Pro (9, incl. 22/25 Creedmoor), Fierce Reaper models (10) were previously undercounted.</li>
    <li><b>LIVE PRICING</b> — every MSRP refreshed to 2026-07-01, incl. Christensen's cuts (Mesa FFT $1,499.99, Ridgeline FFT Ti $2,549.99) and Bergara's discontinuations (Premier LRP, Ridgeback).</li>
    <li><b>SOURCE FIX</b> — Fierce's site is fiercearms.com (the prior fiercefirearms.com does not resolve).</li>
  </ul>
  <div class="brandhead">Primary sources</div>
  <ul class="imp">
    <li><b>MANUFACTURER SITES</b> — horizonfirearms.com/core-firearms · seekinsprecision.com · fiercearms.com · bergara.online · christensenarms.com (all pulled 2026-07-01).</li>
    <li><b>DELIVERY SENTIMENT</b> — Rokslide, Snipers Hide, Reddit, Hunt Talk, AR15.com owner threads; independent lab/press tests; BBB &amp; Trustpilot for warranty/CS signals.</li>
  </ul>
  <div class="disc">LIMITATIONS — Scores are built on published specifications and live MSRP, not measured performance; a corrected accuracy score still reflects a guarantee, not a shot group. The delivery lens (§04) is confidence-rated because owner-data volume is uneven — Horizon's lead rests on thin, low-N data. Value is weighted 5% by design, understating real purchase-price gaps. Two spreads (Venatic Riff 13″ SBR, Vena-Bull .375/.408 CheyTac) have no true current-production analog in the set; their rival scores are directional, not head-to-head.</div>
  {foot(f"APPENDIX · P.{len(P)+1:02d}")}
</section>''')

# ---- APPENDIX C (Improvement Areas) — from consolidated assessment §8
P.append(f'''<section class="page">
  {runhead("APPENDIX C · IMPROVEMENT AREAS")}
  <div class="lead-num">C / IMPROVE</div><h2 class="sect">Where Horizon can gain — highest-value moves</h2>
  <p class="intro">Ranked by competitive impact, each tied to the criterion it moves. The top three target the heaviest criteria on which Horizon currently loses (Accuracy 20%, Weight 15%, Caliber 10%); the throughline is that Horizon's durable edge is not the spec sheet — where rivals match or beat it — but demonstrated delivery on the promise, the one axis a price-cutter cannot copy and the whole field is weak on.</p>
  <div class="brandhead">Tier 1 — highest leverage</div>
  <ul class="imp">
    <li><b>TURN THE GUARANTEE INTO DELIVERED PROOF</b> — Ship a fired, per-rifle test target (as Seekins does) and make the no-fee, no-questions warranty a marketed weapon. Every rival's dominant complaint is failing to deliver the promise consistently (Fierce's $200 fee-to-claim, Christensen's D-, Bergara's coin-flip). Publicize the confirmed no-fee guarantee; capture and publish owner-reported group sizes and warranty-honor rates. (Accuracy 20% + the delivery lens.)</li>
    <li><b>BROADEN CHAMBERINGS ON FOCUSED MODELS</b> — Single-caliber models (Vandal Dark II, Villain, Vandal X, Bloodline) score 3.5–4.5 on Caliber vs rivals' 8.6–9.0; this is exactly where the Seekins Element M3 beats us. As the originator of 22 Creedmoor, Horizon should own a broad proprietary menu, or frame the single-calibers as intent. (Caliber 10% — largest recurring deficit.)</li>
    <li><b>FIELD A SUB-6 LB MOUNTAIN OPTION</b> — Horizon hunters run 7–7.5 lb where Christensen Ti is ~5.3 lb and Fierce carbon 5.6–6.3 lb; weight is where the mountain matchups are lost outright. The forthcoming XLR-Atom magnesium-chassis SBR is the first sub-6 lb answer — extend the lightweight approach to a full-length mountain SKU. (Weight 15% — second-heaviest.)</li>
  </ul>
  <div class="brandhead">Tier 2 — clean, lower-cost gains</div>
  <ul class="imp">
    <li><b>STANDARDIZE THE PREMIUM TRIGGER ON CHASSIS VANDALS</b> — chassis rivals ship the TriggerTech Diamond; a low-cost BOM change closes a buyer-noticed gap. (Trigger 9%.)</li>
    <li><b>MAKE THE PRICE PREMIUM LEGIBLE</b> — Horizon is +$300 to +$900 above the nearest analog at most tiers (wider vs Christensen/Bergara chassis guns). Either sharpen a value tier or make the premium visible via proof targets, lifetime support and demonstrated build. (Value — 5% in scoring, decisive in real purchases.)</li>
    <li><b>PUBLISH COMPLETE, VERIFIABLE SPEC SHEETS</b> — several Horizon weights and trigger grades are unpublished, unlike every competitor; cheap credibility that supports the premium-justification story.</li>
    <li><b>OFFER LEFT-HAND ACTIONS &amp; WIDER CONFIGURATION</b>, and improve restock transparency — both widen the addressable market and protect conversion.</li>
  </ul>
  <div class="disc">STRATEGIC THROUGHLINE — Demonstrated delivery and transparency are how a premium-priced brand earns its premium. That is the one position Bergara's pricing, Fierce's carbon and Christensen's weight cannot take, because it is built on a reputation for living up to the promise — not on a spec sheet. Prove it (per-rifle targets, no-friction warranty, published sentiment) and protect it as volume grows, because the unit-to-unit QC variance that sank every rival appears precisely as volume scales.</div>
  {foot(f"APPENDIX · P.{len(P)+1:02d}")}
</section>''')

# ------------------------------------------------------------------ assemble
html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f'<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>Horizon Firearms — Comparative Analysis 2026 (Unbiased · Corrected)</title>'
        f'<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>{"".join(P)}</body></html>')
html = html.replace('<span class="brand">Horizon Firearms · Comparative Catalog</span>',
                    '<span class="logo" role="img" aria-label="Horizon Firearms"></span>')
open(OUT, "w", encoding="utf-8").write(html)
print(f"Wrote {OUT}  ({len(html):,} bytes, {len(P)} pages)  Horizon tops {HZ_WINS}/{len(ORD_MODELS)}")
