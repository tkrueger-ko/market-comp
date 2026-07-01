# Bergara — Audit

## Summary

- **Bergara's published accuracy guarantee is being reported accurately, not fabricated.** Bergara's own current site (bergara.online/us) states "1.0 MOA or less" / "sub-MOA Guarantee" across the B-14 and Premier lines. The report's "1.0 MOA (sub-MOA)" label is a fair paraphrase, not a fabrication — but it is applied *inconsistently* next to Christensen Arms' "Sub-MOA," even though Christensen's own published guarantee uses the identical technical definition (3 shots within 1 MOA at 100 yds). This is a labeling-consistency issue, not a factual error, and the actual Accuracy *scores* given to Bergara are not severely or uniformly depressed by it (Bergara ties or beats Christensen on Accuracy in several matchups, and trails by only 0.1–0.2 in others involving the cheaper steel-barrel B-14 line).
- **One verifiable, material spec error found:** the report's appendix lists only ~3–4 representative chamberings for the **Premier Cima Pro** ("6.5 CM, 6.5/7 PRC, .300 Win"), but Bergara's current product page lists **nine** chamberings, including 22 Creedmoor and 25 Creedmoor — the exact proprietary-feel cartridges central to Horizon's own "broad chambering" pitch. This undercounts the single criterion (Caliber, 10% weight) that the report explicitly designed to reward breadth, and it is the one finding here that moves a weighted total by a non-trivial amount (+0.08).
- **Several Bergara MSRPs in the report are stale relative to bergara.online/us today (2026-06-30).** B-14 Squared Crest is currently $1,879 (not $1,699.99 used in 5 matchups) — a correction that, if anything, *reduces* Bergara's apparent value edge. Conversely, B-14 Wilderness Ridge ($1,099) and B-14 Ridge / 450 BM ($999) are *cheaper* than the $1,199–1,299 the report cites — corrections that would *increase* Bergara's value edge. Net effect on weighted totals from price corrections alone: under ±0.03 points per matchup, because Value is only 5% weighted.
- **Arithmetic check: clean.** Every Bergara weighted total in the report (7.36–8.49 range) recomputes correctly to within rounding from its own published criterion scores and stated weights. No hidden arithmetic bias found.
- **Methodology critique (not a rule violation):** Bergara is the cheapest rifle in every single matchup it appears in, often by $500–$2,300, yet Value is weighted at only 5% — a quarter of Accuracy's weight. A sensitivity test (below) shows that even doubling Value's weight (5%→10%, taken from Accuracy) only narrows the Horizon–Bergara gap by ~0.1 pt per matchup and never flips a winner. The 5% weight is a legitimate, disclosed methodological choice — but it does structurally mute Bergara's single biggest, most verifiable competitive advantage in a report commissioned by a premium-priced rival.
- **No matchup winner changes** under any of the corrections proposed below. The corrections improve accuracy and modestly narrow gaps (mostly in Bergara's favor), but Horizon's "tops 4 of 14" framing is numerically unaffected.

## Spec verification table

| Model | Field | Report says | Verified value | Source URL | Match? |
|---|---|---|---|---|---|
| B-14 Wilderness/Ridge | MSRP | $1,199–1,299 | Wilderness Ridge: $1,099 starting; base Ridge: $999 starting | bergara.online/us/rifles/b14wilderness/wilderness-ridge-rifle/ ; bergara.online/us/rifles/b14/ridge-rifle/ | ✗ overstated by report |
| B-14 Wilderness/Ridge | Accuracy guarantee | 1.0 MOA (sub-MOA) | "sub-MOA Guarantee" (Bergara's general policy = 3-shot groups ≤1.0 MOA at 100 yds) | bergara.online/us/rifles/b14wilderness/wilderness-ridge-rifle/ | ✓ accurate |
| B-14 Wilderness/Ridge | Chamberings | "6.5 CM, .308, 6.5/7 PRC, .300 Win, .22-250, .450 BM (Ridge)" (≈7) | Wilderness Ridge: .308, 6.5 CM, 6.5 PRC, 7 PRC, 28 Nosler, 7mm Rem Mag, 300 PRC, 300 Win Mag (8); base Ridge separately: 14 chamberings incl. .243, .270, .30-06, 7mm-08, .22-250, .450 BM | bergara.online/us/rifles/b14wilderness/wilderness-ridge-rifle/ ; bergara.online/us/rifles/b14/ridge-rifle/ | ~ close, conservative |
| B-14 Squared Crest | MSRP | $1,699.99 | $1,879 (std calibers); $1,929 (6.5 PRC/7 PRC) | bergara.online/us/rifles/b-14squared/crest/ (fetched live) | ✗ understated by report |
| B-14 Squared Crest | Chamberings | "6.5 CM, 6.5/7 PRC, .308, .300 Win" (4) | 6.5 CM, .22-250 Rem, .308 Win, 6.5 PRC, 7 PRC, .300 Win Mag (6) | bergara.online/us/rifles/b-14squared/crest/ | ~ close, missing .22-250 |
| B-14 Squared Crest | Trigger | "Bergara Performance" | Confirmed: adjustable Bergara Performance Trigger (not TriggerTech) | bergara.online/us/rifles/b-14squared/crest/ | ✓ accurate |
| B-14 Squared Crest | Weight | 6.9 lb | 6.8–7.2 lb, 6.9 lb starting | bergara.online/us/rifles/b-14squared/crest/ | ✓ accurate |
| B-14 Squared Cima CF | MSRP | $1,849 | $1,849.99 | NRA/Gun Digest coverage, corroborated by Bergara press materials | ✓ accurate |
| B-14 Squared Cima CF | Weight | 5.8 lb | 5.8 lb (range 5.8–6.2 lb by caliber) | NRA Family / Gun Digest first-look coverage | ✓ accurate |
| B-14 Ridge (450 BM) | MSRP | $1,199 | $999 (all B-14 Ridge configs) | bergara.online/us/rifles/b14/ridge-rifle/ | ✗ overstated by report |
| B-14 Ridge (450 BM) | Magazine | "2-rd box" | 3-rd capacity (.450 Bushmaster row) | bergara.online/us/rifles/b14/ridge-rifle/ | ✗ understated by report |
| B-14 Ridge (450 BM) | Weight | ~7.5 lb | 7.4 lb | bergara.online/us/rifles/b14/ridge-rifle/ | ✓ accurate |
| Premier MgLite | MSRP | $3,149 | $3,099 starting | bergara.online/us/rifles/premier/mglite-rifle/ | ✗ minor overstatement |
| Premier MgLite | Weight | 6.6–6.8 lb | 6.6 lb starting | bergara.online/us/rifles/premier/mglite-rifle/ | ✓ accurate |
| Premier MgLite | Chamberings | "6.5/7 PRC, .300 Win/PRC, 28 Nos" | .308 Win, 6.5 CM, 6.5 PRC, 300 Win Mag, 7 PRC, 300 PRC (6; no 28 Nosler found) | bergara.online/us/rifles/premier/mglite-rifle/ | ~ close, 28 Nos not confirmed |
| Premier Cima Pro | MSRP | $3,099 | $3,099 | bergara.online/us/rifles/premier/cima-pro/ | ✓ accurate |
| Premier Cima Pro | Weight | 5.5 lb | 5.5–5.7 lb | bergara.online/us/rifles/premier/cima-pro/ | ✓ accurate |
| Premier Cima Pro | Accuracy guarantee | 1.0 MOA (sub-MOA) | "sub-MOA Guarantee" on official page | bergara.online/us/rifles/premier/cima-pro/ | ✓ accurate |
| **Premier Cima Pro** | **Chamberings** | **"6.5 CM, 6.5/7 PRC, .300 Win" (≈4)** | **22 Creedmoor, 25 Creedmoor, .308 Win, 6.5 CM, 6.5 PRC, 300 Win Mag, 7mm Rem Mag, 7mm PRC, 300 PRC (9, incl. 22/25 Creedmoor)** | bergara.online/us/rifles/premier/cima-pro/ (live config table, model codes BPR38-22CM, BPR38-25CM, etc.) | **✗ materially understated** |
| Premier LRP/Ridgeback | MSRP | ≈$2,150 | LRP: $2,000; Ridgeback: $2,100 | bergara.online/us/rifles/premier/lrp-rifle/ ; snipercentral.com review | ~ close (high end of range) |
| Premier LRP/Ridgeback | Accuracy guarantee | 1.0 MOA | "guaranteed to produce groups of 1.0 MOA or less at 100 yards with quality factory match grade ammunition" | bergara.online/us/rifles/premier/lrp-rifle/ | ✓ exact match — Bergara's own wording |
| Premier LRP/Ridgeback | Weight | ~9–10 lb | LRP: 9.3–9.7 lb; Ridgeback (heavier variant): 10.75–11.05 lb | bergara.online/us/rifles/premier/lrp-rifle/ ; snipercentral.com | ✓ accurate (LRP variant) |
| Premier LRP/Ridgeback | Trigger | TriggerTech FRT | Confirmed: TriggerTech, Frictionless Release Technology | bergara.online/us/rifles/premier/lrp-rifle/ | ✓ accurate |

## Findings

### 1. Premier Cima Pro chambering breadth materially understated
**Severity:** High
**Type:** spec-error
**Location:** Appendix A2 (Bergara reference table) and Model 01 · Venatic Carbon 2 matchup (table, Caliber/chambering row), report text lines 32–35, 199.
**Report claims:** Bergara Premier Cima Pro chamberings = "6.5 CM, 6.5/7 PRC, .300 Win" — implying roughly 3–4 options. Scored Caliber/chambering = **8.0**, the lowest of all five rifles in that matchup (Horizon 9.2, Seekins 8.6, Fierce 8.4, Christensen 9.0).
**Correct/verified:** Bergara's live product configurator (https://www.bergara.online/us/rifles/premier/cima-pro/) lists nine current chamberings: 22 Creedmoor, 25 Creedmoor, .308 Win, 6.5 Creedmoor, 6.5 PRC, 300 Win Mag, 7mm Rem Mag, 7mm PRC, 300 PRC — each with its own SKU (BPR38-22CM, BPR38-25CM, BPR38-308, BPR38-65CM, BPR38-65PRC, BPR38-300WM, BPR38-7PRC, BPR38-7REM, BPR38-300PRC), all at the same $3,099 MSRP. Notably this includes 22 Creedmoor and 25 Creedmoor — the same niche, performance-oriented cartridges the report uses to justify Horizon's own high Caliber scores (9.0–9.2) elsewhere in the document.
**Fairness impact:** The report's own rubric states Caliber "rewards breadth of chamberings orderable today." On the verified count (9 chamberings, including the two cartridges Horizon is built around), Cima Pro's breadth is closer to Christensen Ridgeline FFT Ti's (9.0, "broad… ~20 options" per Appendix) than to a narrow single-caliber rifle. Scoring it at 8.0 — tied for lowest in the matchup — is not supported by current published specs.
**Proposed score correction:** Caliber/chambering 8.0 → **8.8** (still conservative relative to Christensen's broader ~20-option lineup, but reflecting verified 9-option breadth including 22/25 Creedmoor).
Recomputed weighted total for Bergara Premier Cima Pro (Venatic Carbon 2 matchup):
`Accuracy 8.4×0.20=1.68 + Accessories 8.4×0.15=1.26 + Weight 9.3×0.15=1.395 + Stock 8.5×0.12=1.02 + Caliber 8.8×0.10=0.88 (was 0.80) + Barrel 8.4×0.09=0.756 + Trigger 8.2×0.09=0.738 + Magazine 8.0×0.05=0.40 + Value 8.0×0.05=0.40 = 8.53` (was 8.45; +0.08).
Result: still below Horizon Venatic Carbon 2 (8.84) and Christensen Ridgeline FFT Ti (8.63) and Seekins Element M3 (8.66), but pulls clearly ahead of Fierce Carbon Rogue (8.44) instead of trailing it. Matchup winner (Horizon, 8.84) is unaffected.

### 2. B-14 Squared Crest MSRP is stale (used in 5 matchups)
**Severity:** Medium
**Type:** spec-error
**Location:** Competitor-MSRP footnotes and Value criterion, Models 02/04/10/11/12 (Venatic 2, Vandal Prime 2, Vandal X, Vandal Dark II, Villain) — report text lines 47, 71, 143, 155, 167.
**Report claims:** "Bergara B-14 Sq. Crest $1,699.99," used identically in all five matchups; Value score 8.8 in each.
**Correct/verified:** bergara.online/us currently prices the B-14 Squared Crest at **$1,879** for standard calibers (6.5 CM, .22-250, .308 Win, .300 Win Mag) and **$1,929** for 6.5 PRC/7 PRC — a $179–$229 increase over the figure used in the report (fetched live 2026-06-30, https://www.bergara.online/us/rifles/b-14squared/crest/).
**Fairness impact:** This cuts against Bergara, not for it — the report currently overstates Bergara's value edge in these five matchups by using a lower, outdated price. Flagged here in the interest of accuracy (this audit's mandate is correctness, not advocacy), and because it is a useful illustration of how little the Value criterion actually moves totals (see point 3 below and Methodology note).
**Proposed score correction:** Value (MSRP) 8.8 → **8.6** (modest reduction; Bergara remains the cheapest rifle in every one of these five matchups even at $1,879–$1,929, vs. Christensen Mesa FFT $1,699.99, Fierce CT Rival XP ≈$2,650, Seekins Havak PH3 ≈$2,500, and Horizon at $3,799–$2,999).
Recomputed weighted total (e.g., Venatic 2 matchup): Value delta = (8.6−8.8)×0.05 = −0.01 → weighted total 8.12 → **8.11**. (Same arithmetic applies to the other four matchups using this column.)

### 3. B-14 Wilderness/Ridge and B-14 Ridge (450 BM) MSRPs are overstated
**Severity:** Medium
**Type:** spec-error
**Location:** Appendix A2; Model 09 Vandal 2 matchup (line 131) and Model 13 Vandal Bloodline matchup (line 179).
**Report claims:** "B-14 Wilderness $1,299.00" (Vandal 2 matchup) and "B-14 Ridge (450 BM) $1,199" (Vandal Bloodline matchup).
**Correct/verified:** Live bergara.online/us pages show B-14 Wilderness Ridge starting at **$1,099** (https://www.bergara.online/us/rifles/b14wilderness/wilderness-ridge-rifle/) and B-14 Ridge (all configs, including .450 Bushmaster) at a flat **$999** (https://www.bergara.online/us/rifles/b14/ridge-rifle/).
**Fairness impact:** Unlike Finding 2, this corrects in Bergara's favor — its actual price advantage over Horizon and Christensen in these two matchups is larger than the report credits.
**Proposed score correction:**
- Vandal 2 matchup: Value 9.2 → **9.4** (B-14 Wilderness already category leader at $1,299 vs. Horizon Vandal 2's $2,299; the gap is even larger at the verified $1,099). Recomputed total: (9.4−9.2)×0.05=+0.01 → 7.93 → **7.94**.
- Vandal Bloodline matchup: Value 9.0 → **9.5** (B-14 Ridge 450 BM already category leader at $1,199 vs. Horizon's $2,799; gap is larger at verified $999). Magazine capacity also corrected (Finding 4) in the same matchup; combined recompute below.

### 4. B-14 Ridge (450 BM) magazine capacity understated
**Severity:** Low
**Type:** spec-error
**Location:** Appendix A2; Model 13 Vandal Bloodline matchup, Magazine row (line 176).
**Report claims:** Magazine "2-rd box" for Bergara B-14 Ridge (450 BM); Magazine score 7.2 (lowest of the three rifles in this matchup).
**Correct/verified:** bergara.online/us lists the .450 Bushmaster B-14 Ridge configuration at **3-round capacity**, not 2 (https://www.bergara.online/us/rifles/b14/ridge-rifle/).
**Fairness impact:** Minor, but the report's own Magazine criterion explicitly rewards "capacity" — understating capacity understates the score.
**Proposed score correction:** Magazine 7.2 → **7.5**.
Combined with Finding 3's Value correction, recomputed Vandal Bloodline total for Bergara B-14 Ridge (450 BM):
`Accuracy 7.9×0.20=1.58 + Accessories 7.3×0.15=1.095 + Weight 8.0×0.15=1.20 + Stock 7.5×0.12=0.90 + Caliber 4.0×0.10=0.40 + Barrel 7.8×0.09=0.702 + Trigger 7.5×0.09=0.675 + Magazine 7.5×0.05=0.375 (was 0.36) + Value 9.5×0.05=0.475 (was 0.45) = 7.40` (was 7.36; +0.04). Still trails Christensen Mesa FFT 450 BM (7.65) and Horizon Vandal Bloodline (8.01, unaffected); winner unchanged.

### 5. Accuracy-guarantee labeling is inconsistent across brands, though scoring impact is limited
**Severity:** Low-Medium
**Type:** scoring-inconsistency
**Location:** Appendix A2/A3 and every matchup's Accuracy row.
**Report claims:** Bergara is labeled "1.0 MOA (sub-MOA)" throughout; Christensen Arms is labeled plain "Sub-MOA."
**Correct/verified:** Both manufacturers' own current guarantee policies use the identical technical definition. Bergara: "guaranteed to produce groups of 1.0 MOA or less at 100 yards" (bergara.online/us/rifles/premier/lrp-rifle/). Christensen Arms: "Any firearm under our Sub-MOA Guarantee is guaranteed to shoot 3 shots within 1 MOA at 100 yards" (christensenarmshelp.zendesk.com/hc/en-us/articles/360055265093-What-is-your-accuracy-guarantee). These are the same standard (1 MOA, 3-shot groups, 100 yds, factory match ammo) described in different marketing language by each company.
**Fairness impact:** A reader skimming the Appendix sees a specific number ("1.0 MOA") next to Bergara and a vaguer, more impressive-sounding "Sub-MOA" next to Christensen and Seekins, which risks implying Bergara's standard is looser when it is not. However, checking the actual Accuracy *scores* across all 14 matchups shows this is not systematically punishing: Bergara ties Christensen in 1 matchup, **beats** Christensen in 4 matchups (Premier MgLite/LRP vs. Christensen Ridgeline/MPR), and trails by only 0.1–0.2 in 6 matchups (entry/mid-tier B-14 Squared Crest, Wilderness, and Ridge 450 BM vs. Christensen Mesa FFT) — a gap plausibly justified by 4140 CrMo steel barrels (B-14 economy line) vs. 416 stainless on the compared Christensen models, which is a legitimate "precision construction" distinction under the report's own Accuracy criterion definition ("guarantee and precision construction").
**Proposed score correction:** None proposed — the underlying scores are largely defensible once construction tier is accounted for. Recommend the report standardize its labeling (either show the numeric MOA figure for all five brands, or show "sub-MOA" uniformly) so the presentation doesn't imply a gap that the manufacturers' own guarantees don't support.

### 6. Premier LRP used as the analog across four very different Horizon roles
**Severity:** Low
**Type:** unfair-role-match (observation, not a scored deficiency)
**Location:** Models 06, 07, 08, 14 (Vandal DM, Venatic Riff [13" SBR], Venatic Max [WOOX wood/aluminum], Vena-Bull [ELR .375/.408 CheyTac]) — all paired against "Bergara Premier LRP."
**Report claims/observation:** The same Premier LRP column (identical scores: Accuracy 8.5, Accessories 8.6, Weight 6.8, Stock 8.7, Caliber 7.8, Barrel 8.4, Trigger 8.5, Magazine 8.8, Value 8.4, total 8.21 in all four) is reused verbatim across a heavy precision chassis rifle, a 13" SBR truck gun, a wood/aluminum hybrid hunter, and an extreme-long-range CheyTac rifle.
**Fairness impact:** Bergara does not currently manufacture a true SBR/compact rifle or a CheyTac-chambered ELR rifle, so there is no closer in-catalog analog — the report's own narrative acknowledges this for Vena-Bull ("limited direct rivals in this group"). Because the report's own rubric defines "0 — No relevant offering" as a valid score band, reusing one rifle's identical scorecard across four dissimilar roles is a methodological shortcut. Critically, this does **not** numerically disadvantage Bergara — its reused score (8.21) is competitive in all four matchups — so this is flagged as a transparency/methodology observation, not a finding that warrants a score change.
**Proposed score correction:** None — flagged for disclosure purposes only.

## Methodology note

Two of the report's own design choices interact in a way that is legitimate-but-disclosure-worthy when read against Bergara specifically:

**Value at 5% weight structurally caps Bergara's biggest, most verifiable advantage.** Bergara is the cheapest rifle in literally every matchup it appears in — by $500 to over $2,800 against Horizon, and usually cheaper than Seekins, Fierce, and Christensen too (even after the price corrections above, which work in both directions). Bergara wins the Value criterion outright in most of its matchups (category leader in Vandal 2, Venatic Riff, Venatic Max, Vena-Bull, Vandal Bloodline). But at 5% weight, a full 1.0-point Value advantage only moves a 10-point weighted total by 0.05 — smaller than normal score noise in any other single criterion.

To test whether this is decisive, I reweighted one matchup (Vandal 2: Horizon $2,299 vs. Bergara B-14 Wilderness $1,299) by moving 5 points from Accuracy (20%→15%) into Value (5%→10%), holding every criterion *score* fixed:
- Horizon Vandal 2 recomputes to 8.15 (from 8.18)
- Bergara B-14 Wilderness recomputes to 7.99 (from 7.93)
- Gap narrows from 0.25 to 0.16 — Horizon still wins.

So doubling Value's weight at Accuracy's expense is real but modest in effect; it does not flip outcomes on its own. This is offered as a methodology critique, not a rule violation: the report discloses its weights up front and applies them identically to every brand, which is the report's own definition of fairness. But "identical weights" is not the same as "weights that fairly represent what differentiates these rifles" — and a report commissioned by the most expensive brand in the comparison, in which the cheapest brand never wins a single matchup despite winning Value almost every time, is exactly the scenario where a 5% Value weight deserves scrutiny. A reasonable, still-conservative alternative (Value 10%, Accuracy 15%) would not change any winner but would better reflect Bergara's actual market position as the value leader.

**Accuracy at 20% is the single most influential criterion, and it rests entirely on a manufacturer claim the report itself says is "not measured results."** Given that Bergara's and Christensen's guarantees are textually identical in substance (Finding 5), and that Accuracy is weighted 4x Value, even the small, mostly-defensible 0.1–0.2 gaps on entry-tier B-14 models carry more total-score weight than Bergara's entire price advantage. This compounds the Value-weight issue rather than independently distorting it.

## Net effect on rankings

None of the corrections proposed in this audit change a single matchup winner. Applying every correction above:

| Matchup | Bergara model | Original total | Corrected total | Δ | Winner change? |
|---|---|---|---|---|---|
| Venatic Carbon 2 | Premier Cima Pro | 8.45 | 8.53 | +0.08 | No (Horizon 8.84 still wins; Bergara moves from 4th to ahead of Fierce) |
| Venatic 2 / Vandal Prime 2 / Vandal X / Vandal Dark II / Villain | B-14 Squared Crest | 8.12 | 8.11 | −0.01 | No |
| Vandal 2 | B-14 Wilderness | 7.93 | 7.94 | +0.01 | No |
| Vandal Bloodline | B-14 Ridge (450 BM) | 7.36 | 7.40 | +0.04 | No |

Bergara's overall standing in this report (last- or second-to-last-place finisher in nearly every matchup) is **not** primarily explained by factual errors — most of the report's Bergara specs check out against bergara.online/us. It is explained by (a) one real, fixable chambering-breadth undercount on the Premier Cima Pro, and (b) the structural effect of a 5% Value weight that prevents Bergara's consistent, large, and — after these corrections — slightly *larger* price advantage from ever meaningfully closing a gap, even when Bergara is the outright Value leader in a matchup. The report is accurate to call itself unweighted by brand; it is fair to call it, by its own admission, a comparison that rewards premium construction breadth far more than price — a defensible editorial choice for a "comparative analysis," but one a budget-focused buyer reading this report should be told plainly, given who commissioned it.

## Sources

- https://www.bergara.online/us/rifles/b14wilderness/wilderness-ridge-rifle/
- https://www.bergara.online/us/rifles/b14/ridge-rifle/
- https://www.bergara.online/us/rifles/b-14squared/crest/
- https://www.bergara.online/us/rifles/b-14squared/
- https://www.bergara.online/us/rifles/premier/cima-pro/
- https://www.bergara.online/us/rifles/premier/mglite-rifle/
- https://www.bergara.online/us/rifles/premier/lrp-rifle/
- https://www.bergara.online/us/rifles/premier/ridgeback-rifle/
- https://snipercentral.com/bergara-premier-lrp-full-review/
- https://www.americanhunter.org/content/sundaygunday-bergara-b14-squared-cima-cf/
- https://www.nrafamily.org/content/first-impressions-bergara-b-14-squared-cima-cf-rifle/
- https://gundigest.com/rifles/hunting-rifles/bergara-b-14-squared-cima-cf
- https://gunsamerica.com/digest/bergara-cima-pro-shot-show-2026/
- https://www.theoutdoorwire.com/releases/2026/01/bergara-introduces-the-premier-series-cima-pro/
- https://www.americanhunter.org/content/new-for-2026-bergara-premier-series-cima-pro/
- https://christensenarmshelp.zendesk.com/hc/en-us/articles/360055265093-What-is-your-accuracy-guarantee
- https://christensenarms.com/product/ridgeline/
- https://christensenarms.com/product/ridgeline-fft/
- /home/ko-tk/market-comp/audits/_source_extracted_text.txt (report extracted text used for all "Report claims" citations)
