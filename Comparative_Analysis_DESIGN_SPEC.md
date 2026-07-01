# Horizon Comparative Analysis (Unbiased) — Complete Design & Build Specification

**Purpose of this document.** This is a build manual, not a summary. Following it exactly will produce a *new* Comparative Analysis document — with different rifles, scores, prices, and competitors — whose pages are **visually and structurally indistinguishable** from the reference edition (`Horizon_Comparative_Analysis_UNBIASED_2026`). Every color, font, dimension, page template, and formula is given literally. Where a value is a rule ("winner cell is orange"), it is stated as a rule. Nothing is left to interpretation.

The document is generated as a **single self-contained HTML file** and rendered to PDF. Reproduce the HTML/CSS exactly; feed it new data through the schemas in §6–§7.

---

## 1. Output, canvas & rendering pipeline

| Property | Value |
|---|---|
| Page size | **US Letter, 8.5 in × 11 in**, portrait |
| Page bleed | Full-bleed; `@page { size: 8.5in 11in; margin: 0 }` |
| Model | **One `<section class="page">` per printed page.** Never allow a section to flow across pages. |
| Renderer | **WeasyPrint** (HTML→PDF). Chrome/print-to-PDF also acceptable if identical. |
| Fonts | Embedded (see §3). Do not rely on system fonts. |
| Color | RGB screen colors; advise **full-bleed / borderless** commercial print. |
| File | Emit one `.html`, then render to a same-named `.pdf`. |

**Page-fit rule (critical):** Every `.page` must fit its content within 11 in. The print CSS enforces `height:11in; overflow:hidden; page-break-inside:avoid`. If a spread's matrix grows (e.g., 5 competitors), tighten only padding/row height — never change the type scale. The reference runs **24 pages** with the page inventory in §5.

**Build approach:** a generator script assembles an array of page-section strings (`pages[]`), joins them, wraps them in the HTML shell (§8), and writes the file. This spec is renderer-agnostic: any engine that produces the same DOM+CSS is valid.

---

## 2. Grid, margins & spacing

- **Content page padding:** `.5in` top, `.7in` left/right, `.4in` bottom (`padding:.5in .7in .4in`).
- **Cover:** no padding on the section; an inner wrapper uses `.9in .8in` and is a full-height flex column.
- **Runhead:** top of every non-cover page; 2px solid ink underline; `margin-bottom:20px`.
- **Footer:** absolutely positioned, `left/right:.75in`, `bottom:.42in`; 1px hairline top border.
- **Section title block:** small `.lead-num` kicker (e.g., `01 / METHOD`) directly above a large `h2.sect`.
- Standard paragraph spacing `margin:0 0 10px`. Headings reset to `margin:0`.

---

## 3. Typography

Load exactly these three families (Google Fonts):

```html
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
```

| Family | Weights | Role |
|---|---|---|
| **Oswald** | 300, 400, 500, 600, 700 | All display: cover H1, section titles, rifle names, table headers, eyebrows, brand runhead, axis titles. Always `text-transform:uppercase` with positive letter-spacing. |
| **Inter** | 400, 500, 600, 700 | Body copy, intro paragraphs, callout text. Base `body` font. |
| **JetBrains Mono** | 400, 500, 700 | All numerics & data: scores, MSRP, weights, tick labels, footer, `.note`, `.disc`, pills, scatter labels. |

Representative sizes (do not deviate): cover H1 **74px** (`.94` line-height) with a **38px 300-weight** brass subline; `h2.sect` **30px**; rifle `.hero .name` **36px**; matrix body **10.5px**; reftable body **9px**; footer **9.5px**. Full sizes are encoded in the CSS (§4) — reproduce verbatim.

---

## 4. Color system

Declared as CSS custom properties on `:root`. Reproduce exactly.

```css
:root{
  --ink:#1A1A1A;      /* near-black: text, rules, runhead underline, cover bg, HZ column header */
  --steel:#444444;    /* secondary text; grey circle marker (v1) */
  --steel-2:#6E6E6E;  /* tertiary text, tick labels, grey circle marker (final) */
  --bone:#EDEDED; --bone-2:#FFFFFF; --bone-3:#F2F2F3; /* paper / panel fills */
  --brass:#E8742C;    /* PRIMARY ORANGE: Horizon marker, accents, top-fill, cover glow */
  --brass-deep:#C25E1C;/* darker orange: winning totals, eyebrows, key numbers */
  --clay:#5A5A5A;     /* "edge"/rival grey accents */
  --green:#C25E1C;    /* alias of brass-deep (winner text) */
  --line:rgba(26,26,26,.12);   /* hairline borders */
  --line-2:rgba(26,26,26,.28); /* stronger hairline (ticks) */
}
```

**Brand meaning of color (invariant):** Orange (`--brass`) = Horizon / the subject / the winner. Greys = competitors. Winning weighted totals render in `--brass-deep`. Never color a competitor orange except the single Horizon diamond/marker.

**0–10 score ramp** (used in the rubric swatches and the result-bar track):

```css
.b0{background:#DCDCDC} .b1{background:#E8C9AE} .b4{background:#F2C091}
.b7{background:#F0A968} .b8{background:#EC8C3F} .b9{background:#E8742C} .b10{background:#BF5A1B}
```

**Scatter brand colors** (marker fills): Horizon `#E8742C` (diamond); Seekins `#2B2D30`; Fierce `#7A7A7A`; Bergara `#B3B3B3`; Christensen `#4F4F4F` (all circles).

---

## 5. Page inventory & order (24 pages)

| # | Section | `tag` (runhead right) | `lead-num` | Notes |
|---|---|---|---|---|
| 1 | **Cover** | — | — | Dark, grid + sun glow + horizon line |
| 2 | **Method & Neutrality** | `METHOD & NEUTRALITY` | `01 / METHOD` | Rubric band + weight table + neutrality disc |
| 3 | **Results Index** | `RESULTS INDEX` | `02 / RESULTS` | 14-row table, "honest winner" per row |
| 4–17 | **14 Model spreads** | `MODEL NN · {FAMILY}` | — | One per rifle, ordered by Horizon weighted score, descending |
| 18 | **Field Map (scatter)** | `FIELD MAP` | `03 / FIELD MAP` | Price (log) vs weighted score |
| 19 | **Appendix A1** | `APPENDIX A · COMPETITOR DATA` | `A1 / REFERENCE` | Seekins reference table |
| 20 | **Appendix A2** | `APPENDIX A · COMPETITOR DATA` | `A2 / REFERENCE` | Fierce reference table |
| 21 | **Appendix A3** | `APPENDIX A · COMPETITOR DATA` | `A3 / REFERENCE` | Bergara reference table |
| 22 | **Appendix A4** | `APPENDIX A · COMPETITOR DATA` | `A4 / REFERENCE` | Christensen reference table |
| 23 | **Appendix B** | `APPENDIX B · SOURCES & METHOD` | `B / SOURCES` | Sources + limitations |
| 24 | **Appendix C** | `APPENDIX C · IMPROVEMENT AREAS` | `C / IMPROVE` | "Where Horizon could do better" |

Rules that keep the count stable:
- **One appendix reference page per competitor brand.** Four brands ⇒ four A-pages. If a brand's table would overflow, split that brand across two pages rather than shrinking type.
- The spread count equals the number of Horizon models (reference = 14). Adding/removing a model changes only the spread count and the total page count.
- Spreads are always ordered by the Horizon model's own weighted total, highest first (`idx`, §6).

---

## 6. Scoring engine (exact logic)

### 6.1 Criteria, weights & display order
Nine criteria. `W` holds weights (sum = 1.00). `ORDER` sets the matrix row order and the weight labels shown.

```python
W = dict(acc=.20, feat=.15, wt=.15, stock=.12, cham=.10, barrel=.09, trig=.09, mag=.05, val=.05)
ORDER = [("acc","Accuracy","20%"),("feat","Accessories","15%"),("wt","Weight / Handling","15%"),
         ("stock","Stock / Chassis","12%"),("cham","Caliber / chambering","10%"),
         ("barrel","Barrel","9%"),("trig","Trigger","9%"),
         ("mag","Magazine","5%"),("val","Value (MSRP)","5%")]
def total(s): return round(sum(s[k]*W[k] for k in W), 2)
```

Every rifle (Horizon and competitor) carries a score dict with these nine keys, each **0–10** in 0.1 steps. Weighted total is the dot product with `W`, rounded to 2 decimals.

### 6.2 The 0–10 rubric (shown on the Method page)
`0` none · `1–3` poor · `4–6` average–good · `7` good · `8` good + value · `9` very good + value · `10` exceptional.

### 6.3 Same-spec normalization (mandatory)
**If two rifles share an identical published spec for a criterion, they must receive the identical score for that criterion.** Applied to the two objective specs:

```python
# Accuracy is scored by the published guarantee only:
ACC_SCORE = {0.5:9.0, 0.75:8.5, 1.0:8.0}      # 0.5 MOA→9.0; 0.75→8.5; sub-MOA/1.0→8.0
# Trigger is scored by trigger model:
TRIG_SCORE = {"bixnandy":9.5,"ttdiamond":9.5,"tt":9.0,"timney":8.5,"bergaraperf":8.0}
```

Classification rules used to assign each rifle's guarantee and trigger (brand-driven, override per model where facts differ):
- **Accuracy guarantee:** Horizon = 0.5; Fierce = 0.5; Bergara = 1.0; Christensen = 1.0 (sub-MOA); Seekins = 1.0 (sub-MOA).
- **Trigger:** Fierce Rogue-family = Bix'n Andy (9.5), other Fierce = TriggerTech (9.0); Seekins HIT Pro / NRL / SIC = TriggerTech Diamond (9.5), other Seekins = TriggerTech (9.0); Bergara Premier = TriggerTech (9.0), Bergara B-14 = Performance trigger (8.0); Christensen = TriggerTech (9.0); Horizon = TriggerTech (9.0), except the SBR ("Riff") = Diamond (9.5).

After building the raw score dicts, overwrite `acc` and `trig` for every rifle from these maps so identical specs collapse to identical scores. (See the loop in §7.4.) Extending the rule to other criteria — e.g., identical barrel maker → identical barrel score — is optional but must follow the same "spec→score table" pattern.

### 6.4 Matchup construction (barrel-matched, closest-per-brand)
Each Horizon model is compared with the **closest current model from each competitor brand**, matched on role/class and, where a brand offers it, barrel construction (carbon vs steel). A carbon-only brand (Fierce) supplies its nearest carbon analog even against a steel Horizon. Matchups are declared explicitly (`MATCHUPS`, §7.2); competitor count per spread is typically 4 but may be 2–5. Order within a matchup is the display order in the matrix.

### 6.5 Ranking & derived fields
```python
for m in M:
    m["h"] = HZ[m["title"]]                       # Horizon score dict
    m["comps"] = [(DISPLAY.get(n,n), MSRP_STR[n], CS[n]) for n in MATCHUPS[m["title"]]]
    m["total"] = total(m["h"])
idx = sorted(range(len(M)), key=lambda i: M[i]["total"], reverse=True)  # spread order
```
- **`ranked(m)`** = all rifles in a matchup (Horizon + comps) sorted by weighted total, desc. `ranked(m)[0]` is the honest winner.
- **`crit_leader(m,key)`** = the rifle with the highest score for one criterion.
- **`DISPLAY`** maps an internal name to a shown label (e.g., append ` *` for a footnoted rifle, or rename `MgLite`→`MG Lite`).
- **`NOTES`** maps a model title to a footnote appended to that spread's `.note` line.

---

## 7. Data schemas (swap these to change the document)

### 7.1 Horizon scores `HZ` and competitor scores `CS`
Dicts keyed by rifle name → nine-key score dict. Example rows:

```python
HZ = {
 "Venatic Carbon 2": dict(acc=9.0,barrel=9.0,trig=9.0,stock=8.8,wt=8.9,cham=9.2,feat=8.8,mag=8.6,val=7.2),
 # ... one row per Horizon model ...
}
CS = {
 "Seekins Havak PH3": dict(acc=8.4,barrel=8.3,trig=8.5,stock=8.4,wt=8.0,cham=8.6,feat=8.6,mag=8.4,val=8.0),
 # ... one row per competitor model referenced by any matchup ...
}
```
Note: `acc` and `trig` values here are placeholders; they are overwritten by the §6.3 normalization.

### 7.2 Prices, matchups, display aliases, footnotes
```python
MSRP_STR = { "Seekins Havak PH3":"$1,895.00", "Fierce CT Rival XP":"≈$2,650", ... }  # shown string; "≈" = estimate
MATCHUPS = { "Venatic Carbon 2":["Seekins Element M3","Fierce Carbon Rogue","Bergara Premier Cima Pro","Christensen Ridgeline FFT Ti"], ... }
DISPLAY  = { "Christensen Ridgeline Scout":"Christensen Ridgeline Scout *", "Bergara Premier MgLite":"Bergara Premier MG Lite" }
NOTES    = { "Venatic Riff":"* The Christensen Ridgeline Scout is not an SBR but is included because it is the closest production rifle in this category." }
PRICE    = { "Vandal 2":2299, "Seekins Havak PH3":1895, ... }  # NUMERIC, for the scatter (all rifles)
```

### 7.3 Per-model presentation record `M`
List, one dict per Horizon model, in any order (sorted later by `idx`). Fields consumed by the spread template:

| Field | Meaning | Used in |
|---|---|---|
| `img` | filename stem of the official Horizon photo (JPG) | hero image |
| `title` | model name (matches `HZ` key) | everywhere |
| `fam` | family label, uppercase (e.g., `VENATIC FAMILY`) | runhead tag |
| `msrp` | Horizon MSRP string (e.g., `$3,999`) | hero, index |
| `role` | short role line (eyebrow) | hero eyebrow |
| `spec` | one-line spec sentence | hero `.role` |
| `cham` | chambering list, ` · `-separated | `.chamber` panel |
| `barrel` | barrel maker/material | `.chamber` panel |
| `bl` | barrel length string (set from `BL`) | `.chamber` panel |
| (derived) `h`,`comps`,`total`,`src` | injected by the engine (§6.5, §7.4) | matrix, resultbar |

`BL` is a separate dict `title → barrel-length string` (e.g., `'lengths vary by chambering — 18", 22"'`).

### 7.4 Assembly order of the engine
```python
1. define W, ORDER, total()
2. define M (presentation records, with img/title/fam/msrp/role/spec/cham/barrel)
3. define HZ, CS (raw scores)
4. define MSRP_STR, MATCHUPS, DISPLAY
5. run SAME-SPEC NORMALIZATION over HZ and CS (overwrite acc, trig)   # §6.3
6. (optional) per-model value overrides (e.g., Seekins real-MSRP value bump)
7. for each m in M: attach h, comps, total ; compute idx
8. attach m["src"]=data-URI(img), m["bl"]=BL[title]
9. define PRICE, REF ; build pages[] ; wrap in HTML shell ; render PDF
```

### 7.5 Appendix reference data `REF`
Dict `brand → list of 8-tuples`, one per competitor model:
`(model, msrp, "Action / Barrel", trigger, guarantee, magazine, weight, "Chamberings (representative)")`. Rendered by `reftable()` (§9.5). Every model referenced in any matchup should appear here under its brand.

---

## 8. HTML shell & global assembly

```python
html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Horizon Firearms — Comparative Analysis 2026 (Unbiased)</title>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
{''.join(pages)}
</body></html>"""
# Replace the brand text runhead with the logo image span everywhere:
html = html.replace('<span class="brand">Horizon Firearms · Comparative Catalog</span>',
                    '<span class="logo" role="img" aria-label="Horizon Firearms"></span>')
```

**Logo:** the horizontal Horizon wordmark (`horizon_logo2.png`, ~738×210) is base64-embedded once into the CSS `.logo`, `.coverlogo` background `url(...)`. All page runheads show it via `.logo` (24×84px). The cover shows it larger in a white badge (`.coverbadge`+`.coverlogo`, 30×106px). Substitute the client's horizontal logo as a data URI.

**Images:** each Horizon photo is base64-embedded (`data:image/jpeg;base64,...`). Competitors are **spec-only (no photos)** by design.

---

## 9. Complete stylesheet (authoritative)

Paste this entire block as the document `<style>` (concatenation order matters; later duplicate selectors intentionally override earlier ones — e.g., the result-bar block). `{LOGO_H}` = the logo data URI.

```css
:root{--ink:#1A1A1A;--steel:#444444;--steel-2:#6E6E6E;--bone:#EDEDED;--bone-2:#FFFFFF;--bone-3:#F2F2F3;
--brass:#E8742C;--brass-deep:#C25E1C;--clay:#5A5A5A;--green:#C25E1C;--line:rgba(26,26,26,.12);--line-2:rgba(26,26,26,.28);}
@page{size:8.5in 11in;margin:0}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:#2B2D30;color:var(--ink);font-family:"Inter",system-ui,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased}
.page{width:8.5in;min-height:11in;margin:24px auto;background:var(--bone-2);position:relative;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.45);padding:.5in .7in .4in}
@media print{body{background:#fff}.page{margin:0;box-shadow:none;width:8.5in;height:11in;overflow:hidden;page-break-inside:avoid;break-inside:avoid}}
.display{font-family:"Oswald",sans-serif;font-weight:600;letter-spacing:.01em;line-height:1.02;text-transform:uppercase}
.mono{font-family:"JetBrains Mono",monospace}
.eyebrow{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.22em;font-weight:600;font-size:11px;color:var(--brass-deep)}
h1,h2,h3{margin:0}p{margin:0 0 10px}
.runhead{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid var(--ink);padding-bottom:7px;margin-bottom:20px}
.runhead .brand{font-family:"Oswald",sans-serif;font-weight:700;text-transform:uppercase;letter-spacing:.16em;font-size:13px}
.runhead .tag{font-family:"JetBrains Mono",monospace;font-size:10px;color:var(--steel-2);letter-spacing:.04em}
.foot{position:absolute;left:.75in;right:.75in;bottom:.42in;display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:7px;font-family:"JetBrains Mono",monospace;font-size:9.5px;color:var(--steel-2);letter-spacing:.03em}
.cover{padding:0;background:var(--ink);color:var(--bone-2)}
.cover .grid{position:absolute;inset:0;background-image:linear-gradient(rgba(232,116,44,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(232,116,44,.10) 1px,transparent 1px);background-size:38px 38px;opacity:.55}
.cover .horizonline{position:absolute;left:0;right:0;top:44%;height:1px;background:linear-gradient(90deg,transparent,var(--brass),transparent)}
.cover .sun{position:absolute;left:50%;top:44%;width:240px;height:240px;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle at 50% 60%,rgba(232,116,44,.38),rgba(232,116,44,0) 65%)}
.cover-inner{position:relative;z-index:2;padding:.9in .8in;display:flex;flex-direction:column;height:11in}
.cover .kicker{font-family:"JetBrains Mono",monospace;font-size:11px;letter-spacing:.18em;color:var(--brass)}
.cover h1{font-family:"Oswald",sans-serif;text-transform:uppercase;font-weight:700;font-size:74px;line-height:.94;margin:18px 0 0}
.cover h1 .thin{display:block;font-weight:300;color:var(--brass);font-size:38px}
.cover .sub{max-width:5in;margin-top:auto;color:#d2d2d2;font-size:14px}
.cover .meta{margin-top:24px;display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid rgba(236,230,218,.25);padding-top:16px}
.cover .meta div{font-family:"JetBrains Mono",monospace;font-size:10.5px;color:#9a9a9a}
.cover .meta b{display:block;font-family:"Oswald",sans-serif;font-weight:600;font-size:15px;color:var(--bone-2);letter-spacing:.04em;margin-bottom:3px;text-transform:uppercase}
.lead-num{font-family:"Oswald",sans-serif;font-weight:300;font-size:15px;color:var(--brass-deep);letter-spacing:.1em}
h2.sect{font-family:"Oswald",sans-serif;text-transform:uppercase;font-weight:600;font-size:30px;line-height:1;margin:4px 0 14px}
.intro{max-width:6.4in;color:var(--steel);font-size:13px}
.rubric{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin:18px 0 8px}
.rcell{border:1px solid var(--line);padding:10px 8px;background:#fff}
.rcell .band{font-family:"JetBrains Mono",monospace;font-weight:700;font-size:15px}
.rcell .lab{font-size:10px;color:var(--steel);margin-top:3px;line-height:1.25}
.rcell .swatch{height:6px;margin-bottom:8px}
.b0{background:#DCDCDC}.b1{background:#E8C9AE}.b4{background:#F2C091}.b7{background:#F0A968}.b8{background:#EC8C3F}.b9{background:#E8742C}.b10{background:#BF5A1B}
table.spec{width:100%;border-collapse:collapse;margin:12px 0;font-size:12px}
table.spec th,table.spec td{text-align:left;padding:8px 9px;border-bottom:1px solid var(--line);vertical-align:top}
table.spec thead th{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.06em;font-size:11px;border-bottom:1.5px solid var(--ink)}
table.spec td.crit{font-weight:600;white-space:nowrap}table.spec .w{font-family:"JetBrains Mono",monospace;color:var(--steel-2);font-size:11px}
table.index{width:100%;border-collapse:collapse;font-size:11.5px;margin-top:10px}
table.index th,table.index td{padding:7px 8px;border-bottom:1px solid var(--line);text-align:left}
table.index thead th{font-family:"Oswald",sans-serif;text-transform:uppercase;font-size:10.5px;letter-spacing:.06em;border-bottom:1.5px solid var(--ink)}
table.index td.num,table.index td.msrp,table.index td.score{font-family:"JetBrains Mono",monospace;text-align:right;white-space:nowrap}
table.index td.model{font-weight:600}
.pill{font-family:"JetBrains Mono",monospace;font-size:9.5px;letter-spacing:.04em;padding:2px 7px;border-radius:2px;white-space:nowrap}
.pill.win{background:rgba(232,116,44,.14);color:var(--green);border:1px solid rgba(232,116,44,.45)}
.pill.edge{background:rgba(90,90,90,.10);color:var(--clay);border:1px solid rgba(90,90,90,.40)}
.hero{display:grid;grid-template-columns:1.05fr 1fr;gap:22px;align-items:start;margin-bottom:4px}
.hero .name{font-family:"Oswald",sans-serif;text-transform:uppercase;font-weight:700;font-size:36px;line-height:.96;margin-top:2px}
.hero .role{color:var(--steel);font-size:11.5px;margin-top:6px;max-width:3.6in}
.hero .price{font-family:"JetBrains Mono",monospace;font-size:12px;margin-top:11px}.hero .price b{font-size:21px}
.shot{width:100%;border:1px solid var(--line);background:#fff;padding:6px;display:block}
.shot img{width:100%;height:auto;max-height:1.95in;object-fit:contain;display:block}
.specline{font-family:"Inter";font-size:11px;color:var(--steel);margin-top:6px}
.chamber{font-family:"JetBrains Mono",monospace;font-size:10.5px;color:var(--ink);background:var(--bone-3);border:1px solid var(--line);padding:7px 10px;margin-top:6px;line-height:1.45}
.chamber b{color:var(--brass-deep)}
table.matrix{width:100%;border-collapse:collapse;font-size:10.5px;margin-top:8px}
table.matrix th,table.matrix td{padding:3px 6px;border-bottom:1px solid var(--line);text-align:center}
table.matrix thead th{font-family:"Oswald",sans-serif;text-transform:uppercase;font-size:9.5px;letter-spacing:.03em;border-bottom:1.5px solid var(--ink);vertical-align:bottom}
table.matrix td.c1,table.matrix th.c1{text-align:left;font-weight:600;white-space:nowrap}
table.matrix .w{font-family:"JetBrains Mono",monospace;color:var(--steel-2);font-size:9.5px;font-weight:400}
table.matrix td.num{font-family:"JetBrains Mono",monospace}
table.matrix td.hz,table.matrix col.hz{background:rgba(232,116,44,.12)}
table.matrix th.hz{background:var(--ink);color:var(--bone-2)}
table.matrix tr.total td{border-top:1.5px solid var(--ink);font-weight:700;border-bottom:none}
table.matrix tr.total td.num{font-size:12px}
.best{color:var(--green);font-weight:700}
.callouts{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px}
.callout{border-left:3px solid var(--green);padding:7px 11px;background:#fff;border-top:1px solid var(--line);border-right:1px solid var(--line);border-bottom:1px solid var(--line)}
.callout.edge{border-left-color:var(--clay)}
.callout h4{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.07em;font-size:11px;margin:0 0 5px}
.callout p{font-size:11px;color:var(--steel);margin:0}
.note{font-family:"JetBrains Mono",monospace;font-size:9.5px;color:var(--steel-2);background:var(--bone-3);border:1px solid var(--line);padding:7px 10px;margin-top:8px;line-height:1.45}
/* logo (base64) */
.logo{display:inline-block;height:24px;width:84px;background:url('DATA_URI_LOGO') left center/contain no-repeat;background-color:#fff;vertical-align:middle}
.coverbadge{display:inline-block;background:#fff;border-radius:7px;padding:9px 14px;margin-bottom:20px}
.coverlogo{display:block;height:30px;width:106px;background:url('DATA_URI_LOGO') left center/contain no-repeat}
/* index/leaders/reference helpers */
.leadlist{margin:0;padding-left:15px}
.leadlist li{font-size:11px;color:var(--steel);margin:3px 0}
table.matrix td.best{color:var(--ink);font-weight:700}
table.matrix td.win{color:var(--brass-deep);font-weight:700}
table.reftable{width:100%;border-collapse:collapse;font-size:9px;margin-top:6px}
table.reftable th,table.reftable td{border-bottom:1px solid var(--line);padding:4px 6px;text-align:left;vertical-align:top}
table.reftable thead th{font-family:"Oswald",sans-serif;text-transform:uppercase;font-size:8.5px;letter-spacing:.03em;border-bottom:1.5px solid var(--ink)}
table.reftable td.mono{font-family:"JetBrains Mono",monospace;font-size:8.5px;white-space:nowrap}
table.reftable td.model{font-weight:700;font-size:9.5px}
.brandhead{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.06em;font-size:13px;margin:13px 0 0;color:var(--brass-deep)}
ul.imp{font-size:11.5px;color:var(--ink);margin:6px 0 0;padding-left:16px}
ul.imp li{margin:8px 0;line-height:1.45}
ul.imp b{font-family:"Oswald",sans-serif;text-transform:uppercase;font-size:11px;letter-spacing:.03em}
.disc{font-family:"JetBrains Mono",monospace;font-size:10px;color:var(--steel);background:var(--bone-3);border-left:3px solid var(--brass);padding:9px 12px;margin:10px 0;line-height:1.5}
/* ---- RESULT BAR (final, two-marker; overrides any earlier .rail rules) ---- */
.railwrap{margin:10px 0 2px;border:1px solid var(--line);background:#fff;padding:10px 14px}
.railwrap .rtitle{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4px}
.railwrap .rtitle .t{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.07em;font-size:11.5px}
.railwrap .rtitle .v{font-family:"JetBrains Mono",monospace;font-weight:700;font-size:18px;color:var(--brass-deep)}
.rail{position:relative;height:64px;margin:8px 2px 2px}
.rail .track{position:absolute;left:0;right:0;top:27px;height:8px;display:flex;border-radius:2px;overflow:hidden}
.rail .track i{display:block}
.rail .s0{flex:1}.rail .s13{flex:3}.rail .s46{flex:3}.rail .s7{flex:1}.rail .s8{flex:1}.rail .s9{flex:1}.rail .s10{flex:1}
.rail .tick{position:absolute;top:23px;width:1px;height:16px;background:var(--line-2)}
.rail .ticklab{position:absolute;top:52px;transform:translateX(-50%);font-family:"JetBrains Mono",monospace;font-size:8.5px;color:var(--steel-2)}
.hmark,.cmark{position:absolute;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;white-space:nowrap;z-index:2}
.hmark{top:10px}.cmark{top:24px}
.hmark .dot,.cmark .dot{width:13px;height:13px;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.35)}
.hmark .dot{background:var(--brass);transform:rotate(45deg);margin-top:3px}
.cmark .dot{background:var(--steel-2);border-radius:50%}
.hmark .ml{font-family:"JetBrains Mono",monospace;font-size:8.5px;color:var(--brass-deep);font-weight:700}
.cmark .ml{font-family:"JetBrains Mono",monospace;font-size:8.5px;color:var(--steel);margin-top:3px}
.legend-line{display:flex;gap:18px;align-items:center;font-family:"JetBrains Mono",monospace;font-size:9px;color:var(--steel-2);margin-top:4px}
.legend-line b{display:inline-block;width:11px;height:11px;vertical-align:-1px;margin-right:5px}
.legend-line .h b{background:var(--brass);transform:rotate(45deg)}
.legend-line .c b{background:var(--steel-2);border-radius:50%}
/* ---- SCATTER ---- */
.scatleg{display:flex;gap:16px;flex-wrap:wrap;margin:10px 0 4px;font-family:"JetBrains Mono",monospace;font-size:10px;color:var(--steel)}
.scatleg .lg{display:flex;align-items:center;gap:6px}
.scatleg .lg i{width:11px;height:11px;border-radius:50%;display:inline-block}
.scatkeywrap{margin-top:10px}
.scatkeyhead{font-family:"Oswald",sans-serif;text-transform:uppercase;letter-spacing:.06em;font-size:11px;color:var(--brass-deep);margin-bottom:4px}
ol.scatkey{margin:0;padding:0;list-style:none;columns:2;column-gap:26px;font-size:10.5px}
ol.scatkey li{margin:2px 0;color:var(--ink)}
ol.scatkey li b{font-family:"JetBrains Mono",monospace;color:var(--brass-deep);display:inline-block;width:18px}
```

---

## 9b. Page templates (exact HTML)

All non-cover pages begin with the runhead and (spreads/appendix) end with the footer. `·` = U+00B7, `—` = U+2014, `≈` = U+2248, `″` = U+2033. Placeholders in `{ }`.

### 9.1 Cover (page 1)
```html
<section class="page cover"><div class="grid"></div><div class="sun"></div><div class="horizonline"></div>
<div class="cover-inner">
  <div class="coverbadge"><span class="coverlogo"></span></div>
  <div class="kicker">COMPARATIVE ANALYSIS · BOLT-ACTION RIFLES · 2026</div>
  <h1>Benchmark<span class="thin">scored without a thumb on the scale</span></h1>
  <div class="sub">
    <p>A like-for-like comparison of every Horizon Core Series rifle against its nearest current-production rivals from Fierce, Seekins, Christensen Arms, and Bergara. Every rifle — Horizon included — is scored on the same nine 0–10 criteria with no brand weighting, on published manufacturer specifications and MSRP.</p>
    <p>Where a competitor wins, it is named and ranked first.</p>
  </div>
  <div class="meta">
    <div><b>23 Rivals</b>current production, role-matched</div>
    <div><b>9 Criteria</b>identical for every brand</div>
    <div><b>MSRP</b>like-for-like basis</div>
  </div>
</div></section>
```
The cover has **no runhead and no footer**. The three background layers (`.grid` dotted orange grid, `.sun` radial glow, `.horizonline` gradient rule) sit behind `.cover-inner`.

### 9.2 Method & Neutrality (page 2)
```html
<section class="page">
  <div class="runhead"><span class="brand">Horizon Firearms · Comparative Catalog</span><span class="tag">METHOD &amp; NEUTRALITY</span></div>
  <div class="lead-num">01 / METHOD</div><h2 class="sect">How every rifle is scored</h2>
  <p class="intro">{one paragraph explaining the weights and matchup rule}</p>
  <div class="rubric">
    <div class="rcell"><div class="swatch b0"></div><div class="band">0</div><div class="lab">No relevant offering</div></div>
    <div class="rcell"><div class="swatch b1"></div><div class="band">1–3</div><div class="lab">Poor — clear shortfall</div></div>
    <div class="rcell"><div class="swatch b4"></div><div class="band">4–6</div><div class="lab">Average to good</div></div>
    <div class="rcell"><div class="swatch b7"></div><div class="band">7</div><div class="lab">Good — no real caveat</div></div>
    <div class="rcell"><div class="swatch b8"></div><div class="band">8</div><div class="lab">Good, with added value</div></div>
    <div class="rcell"><div class="swatch b9"></div><div class="band">9</div><div class="lab">Very good — significant value</div></div>
    <div class="rcell"><div class="swatch b10"></div><div class="band">10</div><div class="lab">Excellent &amp; exceptional</div></div>
  </div>
  <table class="spec"><thead><tr><th style="width:24%">Criterion</th><th class="w" style="width:9%">Weight</th><th>What it rewards (applied identically to all brands)</th></tr></thead>
  <tbody>
    <tr><td class="crit">Accuracy</td><td class="w">20%</td><td>…</td></tr>
    <!-- one row per criterion, in ORDER, with matching weight -->
    <tr><td class="crit">Value</td><td class="w">5%</td><td>…</td></tr>
  </tbody></table>
  <div class="disc">NEUTRALITY — {neutrality statement incl. the same-spec rule and barrel-match rule}</div>
</section>
```
The rubric is a **7-column grid**; the spec table lists the nine criteria in `ORDER` with weights matching `W`.

### 9.3 Results Index (page 3)
```html
<section class="page">
  <div class="runhead"><span class="brand">Horizon Firearms · Comparative Catalog</span><span class="tag">RESULTS INDEX</span></div>
  <div class="lead-num">02 / RESULTS</div><h2 class="sect">Every matchup, honest winner</h2>
  <p class="intro">… Horizon takes the top score in {hz_wins} of {N} …</p>
  <table class="index"><thead><tr><th>#</th><th>Horizon model</th><th class="msrp">MSRP</th><th class="score">Horizon</th><th>Top-scoring rifle in matchup</th><th>Result</th></tr></thead>
  <tbody>
    <!-- one row per model in idx order: -->
    <tr><td class="num">{rank}</td><td class="model">{title}</td><td class="msrp">{msrp}</td><td class="score">{horizon_total}</td>
        <td>{winner_name} ({winner_total})</td>
        <td>{pill}</td></tr>
  </tbody></table>
  <div class="note">Ranked by the Horizon model's own weighted score. …</div>
</section>
```
`pill` = `<span class="pill win">Horizon tops</span>` when the Horizon model wins its matchup, else `<span class="pill edge">{Winner} tops</span>`.

### 9.4 Model spread (pages 4…, one per model in `idx` order)
```html
<section class="page">
  <div class="runhead"><span class="brand">Horizon Firearms · Comparative Catalog</span><span class="tag">MODEL {rank:02d} · {FAMILY}</span></div>
  <div class="hero">
    <div>
      <div class="eyebrow">{role}</div>
      <div class="name">{title}</div>
      <div class="role">{spec}</div>
      <div class="price">MSRP <b>{msrp}</b></div>
      <div class="chamber"><b>Chamberings:</b> {cham}<br><b>Barrel:</b> {barrel} · {bl}</div>
    </div>
    <div>
      <span class="shot"><img alt="{title}" src="{data-uri jpg}"></span>
      <div class="specline">Horizon image (official). Competitors shown spec-only. <b>Top weighted score: {winner} ({winner_total}).</b></div>
    </div>
  </div>
  {RESULT_BAR}      <!-- §9.6 -->
  {MATRIX}          <!-- §9.7 -->
  <div class="callouts">
    <div class="callout"><h4>Category leaders</h4>{LEADERS_LIST}</div>
    <div class="callout edge"><h4>Analyst note</h4><p>{ANALYST_NOTE}</p></div>
  </div>
  <div class="note">COMPETITOR MSRP (MSRP vs MSRP): {name msrp · name msrp · …}. Current-production models only. {optional footnote from NOTES}</div>
  <div class="foot"><span>COMPARATIVE ANALYSIS — PUBLISHED-SPEC BASIS</span><span>{TITLE UPPER} · P.{page:02d}</span></div>
</section>
```
- **Hero grid** is two columns `1.05fr 1fr`: left = text, right = photo + caption.
- **Category leaders** list: five `<li><b>{Label}:</b> {leader} ({score})</li>` for Accuracy, Chamberings, Weight, Trigger, Value (from `crit_leader`).
- **Analyst note** text pattern: if Horizon wins → *"The {title} posts the top weighted score here ({t} of 10), ahead of {2nd} ({t2})."*; else → *"{winner} posts the top weighted score ({t}); the {title} ranks #{rank} of {n} at {ht}."* — followed by *"The Horizon model rates highest on {top-2 criteria} and lowest on {bottom-2 criteria}. Scores reflect published specifications, not measured performance."*

### 9.5 Appendix reference pages (A1–A4, one per brand)
```html
<section class="page">
  <div class="runhead"><span class="brand">Horizon Firearms · Comparative Catalog</span><span class="tag">APPENDIX A · COMPETITOR DATA</span></div>
  <div class="lead-num">A1 / REFERENCE</div><h2 class="sect">Competitor reference — {Brand}</h2>
  <!-- A1 only: a <p class="intro"> preface sentence -->
  <div class="brandhead">{Brand}</div>
  <table class="reftable"><thead><tr>
    <th>Model</th><th>MSRP</th><th>Action / Barrel</th><th>Trigger</th><th>Guarantee</th><th>Magazine</th><th>Weight</th><th>Chamberings (representative)</th>
  </tr></thead><tbody>
    <tr><td class="model">{model}</td><td class="mono">{msrp}</td><td>{build}</td><td>{trig}</td><td class="mono">{guar}</td><td>{mag}</td><td class="mono">{wt}</td><td>{cham}</td></tr>
    <!-- one row per model from REF[brand] -->
  </tbody></table>
  <div class="foot"><span>COMPARATIVE ANALYSIS — PUBLISHED-SPEC BASIS</span><span>APPENDIX · P.{page:02d}</span></div>
</section>
```

### 9.5b Appendix B (Sources) & C (Improvement)
Both use the same shell as §9.5 with `tag` = `APPENDIX B · SOURCES & METHOD` / `APPENDIX C · IMPROVEMENT AREAS` and `lead-num` = `B / SOURCES` / `C / IMPROVE`. Body uses `<p class="intro">`, `<div class="brandhead">` sub-heads, `<ul class="imp">` bulleted lists (each `<li>` begins `<b>UPPERCASE LEAD</b> — …`), and a closing `<div class="disc">` for limitations.

---

## 9.6 Component: two-marker result bar (`RESULT_BAR`)

A single 0–10 track showing **one orange diamond (Horizon)** above the line and **one grey circle (leading rival)** below it. The grey circle is the highest-scoring competitor in the matchup (i.e., the leader if Horizon loses, or the runner-up if Horizon wins).

```html
<div class="railwrap">
  <div class="rtitle"><span class="t">Weighted result — Horizon vs. leading competitor</span><span class="v">{horizon_total:.2f}</span></div>
  <div class="rail">
    <div class="track"><i class="s0 b0"></i><i class="s13 b1"></i><i class="s46 b4"></i><i class="s7 b7"></i><i class="s8 b8"></i><i class="s9 b9"></i><i class="s10 b10"></i></div>
    <!-- ticks at 0,3,6,7,8,9,10 -->
    <div class="tick" style="left:0%"></div><div class="ticklab" style="left:0%">0</div>
    <div class="tick" style="left:30%"></div><div class="ticklab" style="left:30%">3</div>
    <div class="tick" style="left:60%"></div><div class="ticklab" style="left:60%">6</div>
    <div class="tick" style="left:70%"></div><div class="ticklab" style="left:70%">7</div>
    <div class="tick" style="left:80%"></div><div class="ticklab" style="left:80%">8</div>
    <div class="tick" style="left:90%"></div><div class="ticklab" style="left:90%">9</div>
    <div class="tick" style="left:100%"></div><div class="ticklab" style="left:100%">10</div>
    <div class="cmark" style="left:{rival_total*10:.1f}%"><span class="dot"></span><span class="ml">{rival} {rival_total:.2f}</span></div>
    <div class="hmark" style="left:{horizon_total*10:.1f}%"><span class="ml">{title} {horizon_total:.2f}</span><span class="dot"></span></div>
  </div>
  <div class="legend-line"><span class="h"><b></b>{title} (Horizon)</span><span class="c"><b></b>{rival} (best rival)</span></div>
</div>
```
**Geometry (invariant):** track spans 0–100% = score 0–10 (`left = score*10%`). The track is a 7-segment flex ramp (weights 1:3:3:1:1:1:1) colored with the b0…b10 ramp. Horizon marker (`.hmark`, label-over-diamond) sits above the line; rival marker (`.cmark`, circle-over-label) below — vertical offsets prevent overlap even when scores are close. Diamond = brass; circle = steel-grey.

## 9.7 Component: criterion matrix (`MATRIX`)

```html
<table class="matrix"><thead><tr>
  <th class="c1">Criterion <span class="w">/ weight</span></th>
  <th>{HorizonTitle split on first space to two lines}</th>
  <th>{Comp1 split}</th> … <th>{CompN split}</th>
</tr></thead><tbody>
  <!-- one row per criterion in ORDER -->
  <tr><td class="c1">{Label} <span class="w">{weight%}</span></td>
      <td class="num{ best?}">{hz_val:.1f}</td>
      <td class="num{ best?}">{comp_val:.1f}</td> … </tr>
  <tr class="total"><td class="c1">Weighted total</td>
      <td class="num{ win?}">{hz_total}</td>
      <td class="num{ win?}">{comp_total}</td> … </tr>
</tbody></table>
```
Rules: header cells break the model name after the first space into two lines. In each criterion row, the **highest** value in the row gets class `best` (renders `--green`/bold). In the total row, the **highest** weighted total gets class `win` (renders `--brass-deep`/bold). Column count = 1 (criterion) + 1 (Horizon) + N (competitors); typical N=4, allow 2–5. All value cells are `num` (mono).

## 9.8 Component: Field-Map scatter (page 18)

Inline **SVG**, `viewBox="0 0 724 412"`, `width:100%`, 1px `--line` border, white fill. Plots every rifle (Horizon + all competitors) once.

- **Plot rect:** x0=60, y0=26, x1=704, y1=384.
- **X axis = MSRP on a log10 scale.** `X(price) = x0 + (log10(price) − 3) × (x1 − x0)` (i.e., $1,000→x0, $10,000→x1). X gridlines/labels at 1000,1500,2000,3000,5000,10000 → `$1k,$1.5k,$2k,$3k,$5k,$10k`. Axis title `MSRP — log scale` centered below.
- **Y axis = weighted score (linear).** Range `ylo = min(7.0, min_total−0.1)` to `yhi = max(9.0, max_total+0.1)`. `Y(t) = y0 + (1 − (t−ylo)/(yhi−ylo)) × (y1−y0)`. Horizontal gridlines + labels every 0.5 from `ceil(ylo×2)/2`. Rotated axis title `Weighted score` at left.
- **Markers:** competitors = `circle r=4.2` filled by brand color (Seekins `#2B2D30`, Fierce `#7A7A7A`, Bergara `#B3B3B3`, Christensen `#4F4F4F`), white 0.8 stroke. Horizon = **12×12 square rotated 45°** (diamond) fill `#E8742C`, white stroke, with the model's **overall rank number** centered in white 7.5px mono. Draw competitors first, Horizon diamonds on top.
- **Legend (`.scatleg`):** five entries; Horizon swatch is a rotated square, others are circles.
- **Numbered key (`.scatkeywrap` + `ol.scatkey`, 2 columns):** `#rank Model` for every Horizon model in `idx` order, matching the diamond numbers.
- Intro line: *"All {count} current-production rifles plotted by MSRP (log scale) against their weighted score… Horizon models are orange diamonds, numbered by overall rank; competitors are grey by brand."* Footer identical to spreads with right label `FIELD MAP · P.{page:02d}`.

---

## 10. Invariant rules (do not violate when re-skinning with new data)

1. **Neutral framing.** No brand weighting; Horizon competes on the same nine criteria. Every spread and the index name the *actual* winner, orange-highlighted, even when it is a competitor.
2. **Color semantics.** Orange = Horizon/winner only. Competitors are grey. Winning totals are `--brass-deep`.
3. **One section = one Letter page.** Content must fit; tighten spacing, never the type scale.
4. **Same-spec → same-score** for accuracy (by guarantee) and trigger (by model), via the tables in §6.3.
5. **Barrel-matched, closest-per-brand matchups** (§6.4), declared in `MATCHUPS`.
6. **Spread order = Horizon weighted total, descending** (`idx`).
7. **Runhead** on every non-cover page (logo left, mono tag right, 2px ink underline). **Footer** on spreads/appendix (left constant label, right `{context} · P.NN`).
8. **Photos for Horizon only;** competitors are spec-only.
9. Estimated prices are prefixed `≈`; footnoted rifles get ` *` via `DISPLAY` plus a `NOTES` sentence in that spread's `.note`.
10. Fonts: Oswald (display/upper), Inter (body), JetBrains Mono (all numerics). Never substitute.

---

## 11. How to produce a new edition (checklist)

1. Replace **`M`** (presentation records) and **`BL`** with the new Horizon lineup; drop new JPGs where the generator can read them and set each `img` stem.
2. Replace **`HZ`** and **`CS`** score dicts (nine keys, 0–10). Set raw `acc`/`trig` to anything — they are normalized.
3. Set **guarantee/trigger classification** (§6.3) so identical specs collapse; adjust the brand rules if the new brands differ.
4. Declare **`MATCHUPS`** (barrel-matched, closest per brand), plus **`MSRP_STR`**, **`PRICE`** (numeric, every rifle), **`DISPLAY`**, **`NOTES`**.
5. Rebuild **`REF`** so every competitor in any matchup appears under its brand; keep one A-page per brand.
6. Update the Method intro/weight table if `W`/`ORDER` change; keep the rubric band unchanged.
7. Update cover meta counts, the index intro (`{hz_wins} of {N}`), and Appendix B/C prose.
8. Run the engine (§7.4) → emit HTML (§8) → render with WeasyPrint to Letter PDF.
9. **QA:** confirm page count matches §5; every `.page` fits 11in (no clipped matrices, esp. 5-competitor spreads); winners/orange highlighting correct; scatter numbers match the key; fonts embedded in the PDF.

*End of specification.*
