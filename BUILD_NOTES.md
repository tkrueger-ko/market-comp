# Corrected Edition — Build Notes & Methodology

**Artifact:** `Horizon_Comparative_Analysis_UNBIASED_2026_CORRECTED.html` (+ `.pdf`)
**Generator:** `build_edition.py` (deterministic; re-run to regenerate)
**Built:** 2026-07-01 · 25 pages · US Letter

This edition mirrors the original `Horizon_Comparative_Analysis_UNBIASED_2026.html`
per `Comparative_Analysis_DESIGN_SPEC.md` — **same page templates, CSS, fonts, logo,
and the 14 Horizon photos, reused byte-for-byte** — but is fed the corrected data
from the multi-agent audit. Only the *inputs* changed, never the scoring machinery.

## What the generator does

1. **Parses the original HTML** as the ground-truth baseline: every rifle's nine
   criterion scores, matchups, hero copy, and the embedded CSS/logo/photos.
2. **Applies a correction layer** (below), then **recomputes** every weighted total,
   re-ranks the spreads by Horizon total, and regenerates all matrices, result bars,
   the results index, the scatter, and the analyst notes from the corrected numbers.
3. **Refreshes every MSRP** to the live 2026-07-01 figures in `sales/PRICE_REFERENCE.md`.
4. **Adds one new section** — `04 / DELIVERY` — the customer-sentiment / promise-vs-
   delivery lens from `audits/CONSOLIDATED_ASSESSMENT.md §7`, on the same visual system.

Every printed number is therefore either (a) reproducible from a stated rule, (b) the
original analyst's cell value left untouched, or (c) an anchored factual override listed
below. **Nothing is invented.**

## Correction layer

### A. Same-spec normalization applied *consistently* (the headline fix)
The original report defines this rule in its own method (`DESIGN_SPEC §6.3`) but did not
apply it evenly — Horizon's 0.5 MOA guarantee scored 9.0–9.2 while Fierce's identical
0.5 MOA guarantee was capped ~8.3–8.6. This edition enforces it in both directions:

- **Accuracy — scored by guarantee tier:** 0.5 MOA → 9.0 · 0.75 → 8.5 · 1.0/sub-MOA claim → 8.0.
  - Horizon (all): 0.5 MOA → **9.0** (was 9.0–9.2; the small inflation is removed).
  - Fierce: Carbon Rogue 0.75 → 8.5; **CT Rival XP, Carbon Rage LR, MTN Reaper 2.0,
    Reaper H-TAC 2.0 all 0.5 → 9.0** (equal to Horizon).
  - Seekins (all): 1.0 claim **+ per-rifle fired test target = demonstrated proof → 8.5**
    (credited one tier above an unverified claim, per the report's own Appendix C).
  - Bergara / Christensen (all): 1.0 / sub-MOA claim → **8.0**.
- **Trigger — scored by trigger model:** TT Diamond / Bix'n Andy 9.5 · TriggerTech 9.0 ·
  Bergara Performance 8.0.
  - Horizon 9.0, except **Venatic Riff SBR (TriggerTech Diamond) 9.5**.
  - Seekins **HIT Pro M3 (Diamond) 9.5**; PH3 / Element M3 / **NRL (Primary — corrected
    from "Diamond") 9.0**.
  - Fierce 9.0 (TriggerTech; Bix'n Andy on Rogue-family was *not* verified in our audit,
    so kept conservative at 9.0 rather than 9.5).
  - Bergara Premier 9.0 / B-14 Performance 8.0; Christensen 9.0.

### B. Verified factual spec overrides (anchored, one-directional-to-truth)
Each is tied to a cited live-2026 spec and set to a target anchored to an
already-in-document comparably-specced rifle. Applied once, propagates to every matchup.

| Competitor | Cell(s) | From → To | Basis |
|---|---|---|---|
| Fierce CT Rival XP | barrel, wt, cham | 8.5→**8.7**, 8.4→**8.9**, 8.0→**8.2** | Ti action, full C3 carbon barrel, 0.5 MOA, ~6 lb, 7 chamberings (prior sheet described a *different*, steel rifle) |
| Christensen MPR | wt, cham | 6.9→**8.6**, 7.8→**8.8** | real ≈6.9 lb (not "8–10 lb"); anchored below Bergara Cima 5.5 lb=9.3. 12 chamberings |
| Seekins Element M3 | cham | 8.6→**9.0** | verified 10 chamberings |
| Bergara Premier Cima Pro | cham | 8.0→**8.8** | verified 9, incl. 22/25 Creedmoor |
| Fierce Reaper H-TAC 2.0 | cham | 8.0→**8.6** | verified 10 chamberings |
| Fierce MTN Reaper 2.0 | cham | 8.0→**8.6** | verified 10 chamberings |
| Seekins HIT Pro M3 | val | 7.6→**8.2** | real $2,400 (report est ~$2,800) |
| Seekins Havak PH3 NRL | val | 7.8→**8.0** | real $2,295 published |

Horizon cells are **not** bumped anywhere (the single-caliber low chambering scores are
genuine and left as-is). Value cells beyond the two Seekins fixes were left at the
original analyst values — no new value formula was invented.

### C. Live pricing (all rifles)
Every Horizon and competitor MSRP refreshed to 2026-07-01 (`PRICE_REFERENCE.md`), incl.
Christensen's cuts (Mesa FFT $1,499.99, Ridgeline FFT Ti $2,549.99 — was ~$3,399.99) and
Bergara's discontinuations. Discontinued **Bergara Premier LRP** is retained only as a
legacy analog, marked **†** with a footnote.

## Result

**Horizon tops 3 of 14** (was "4 of 14"): clear wins at **Venatic Carbon 2** and
**Venatic 2** (now a 0.03 near-tie over Fierce CT Rival XP) plus the uncontested-niche
**Vandal Bloodline**. **Vandal Prime 2 flips to Fierce CT Rival XP** (8.68 vs 8.65).
This matches the reconciled **Scenario B** in `CONSOLIDATED_ASSESSMENT.md §3` exactly.

## Known cosmetic note
On a few dense model spreads the competitor-MSRP note runs close to the page footer —
this is **inherited from the original design** (the original overlaps identically) and is
within the `overflow:hidden` page box; no content spills to an extra page (PDF = 25 pp).

## Judgment calls (documented, per the "decide and move on" instruction)
- **Scope = the same 14 models.** The 3 new/pre-release SKUs (Rabble Core Pistol, dealer
  Bandit, pre-release XLR-Atom Mg SBR) are **not** scored here: full phase-1 scoring is
  paused per your instruction, and there are no official photos for them (the design is
  photo-per-Horizon-model). They are called out in Appendix C / QUESTIONS instead.
- **Seekins accuracy = 8.5, not 8.0.** Pure guarantee-tier would put Seekins at 8.0, but
  Seekins ships demonstrated proof (fired test target); the report's own Appendix C says
  that outranks a claim, so it gets +1 tier. Documented here so it's not mistaken for a
  thumb on the scale in Seekins' favor.
- **Fierce triggers kept at 9.0** (not the spec's illustrative "Rogue-family = Bix'n Andy
  9.5") because our audit did not verify Bix'n Andy on the specific models in these
  matchups. Conservative; would only move further against Horizon if confirmed.
