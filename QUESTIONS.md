# Open Questions & Decisions Log — for review

Items I decided on my own to keep moving (per your "make a decision and move on, document it" instruction), plus open questions the agents surfaced that need a human/business answer. Nothing here blocked delivery; all are worth a look before this material is used externally.

## Decisions I made (so you can override if wrong)

1. **Battlecards are partisan but truth-bound.** You said "take the unbiased hat off," so the sales material is pro-Horizon. I drew the line at *factual accuracy*: every competitor weakness cited is sourced to our own audits, and each battlecard has a "Landmines" section banning claims that would get a rep caught (including repeating our own report's false "Seekins doesn't publish pricing" error). Rationale: a caught exaggeration loses the deal and the reputation. If you want a more aggressive tone that trades some defensibility for punch, say so and I'll re-cut.
2. **File layout.** Phase 2 lives in `/sales/` (`SALES_PLAYBOOK.md` + four `battlecard_*.md`). Phase 3 is a single top-level `MDT_LonePeak_threat_assessment.md`, kept fully separate per your instruction and linked (not merged) from the exec summary.
3. **Playbook structure = overall + per-brand,** exactly as asked: a universal "things to lean into" list and guardrails, then a per-brand quick reference, with the full objection/proof tables pushed down into each battlecard so reps aren't drowning.
4. **Christensen analog** stays the current-production **Ridgeline FFT** (your call from earlier), carried through the sales material.
5. **No new pricing/promo research in Phase 2.** Agents synthesized the existing (2026-06-30) audits and did only spot web checks (e.g., a live Trustpilot pull for Christensen). Point-of-sale pricing must be re-verified — see below.
6. **Everything pushed to the existing PR #1** on branch `competitive-audit-2026`, not a new branch.

## Open questions for you (business/policy — I couldn't answer these)

### ✅ RESOLVED (answered by Horizon 2026-07-01 — baked into playbook + battlecards)
1. **Warranty/accuracy-guarantee policy — RESOLVED: no fee for accuracy testing + a no-questions commitment to make it right** (premium buyer → we take care of them). This is now an *affirmative lead claim* vs Fierce's $200 fee, updated across the playbook and the Seekins/Fierce/Christensen cards. *Still to confirm: exact RMA turnaround (days) before reps quote a specific number.*
2. **Per-rifle test target — RESOLVED: we do NOT ship test targets on all production rifles**, but the no-questions make-it-right commitment stands. Fixed a real error (the Seekins card had implied we ship one); added a guardrail forbidding that claim. Our accuracy proof = *independent third-party* testing + the no-fee guarantee. (Shipping targets remains a recommended future addition, not a current practice.)
3. **Sub-6 lb option — RESOLVED: sub-6 lb options are launching now.** Updated the Fierce/Christensen "walk-away on weight" lines from a flat concession to "available/imminent — check current availability." *Still to confirm for reps: exact model name, weight, chambering, price, and whether orders can be taken today (see Open #4b).*

### Medium priority (accuracy / freshness)
4. **Current Horizon MSRP master sheet — IN PROGRESS.** Per Horizon's go-ahead to pull MSRPs from company websites, a Sonnet agent is building `sales/PRICE_REFERENCE.md` (full Horizon lineup + competitor MSRPs + head-to-head deltas). Replaces the $2,299–$9,999 range with per-model figures.
4b. **Sub-6 lb SKU — RESOLVED: it's the XLR Atom magnesium-chassis SBR (~$3,999, Stiller Hyrax, standard Riff/DM chamberings)** — the same new SKU flagged in 5b. **Role nuance baked into the cards:** it's a short-barreled/compact rifle, so it's the sub-6 lb answer for a weight-/compactness-driven or suppressor-oriented buyer — *not* a like-for-like full-length ultralight mountain hunter (so it doesn't fully answer a Christensen Ridgeline FFT Ti mountain buyer). *Still nice-to-have: exact weight figure and whether orders can be taken today.*
4c. **RMA turnaround — RESOLVED:** ~2 weeks, and the rifle comes back with **a handwritten note from a senior leader and a box of ammo.** This is now the signature CS proof point across the playbook and all four battlecards — a tangible, hard-to-copy "we take care of you" moment.

### Product scope & pricing (from `sales/PRICE_REFERENCE.md`, pulled 2026-07-01)
5b. **The report's 14-model Horizon lineup is incomplete — now captured.** Current site shows **15 Core models**; the report missed the **Rabble Core Pistol ($3,399, Stiller Predator, 13", 22 Creed)**, plus an off-catalog dealer-exclusive **"Bandit" (~$2,199–$2,499)**. *Decision for you: re-run phase-1 scoring against the full lineup, or is the pricing/sales capture enough? (You said don't re-run yet — holding.)*
5c. **XLR Atom MG SBR — confirmed pre-release, not yet public.** The web pull couldn't find it on horizonfirearms.com (consistent with pre-launch). I reframed the price-reference entry from "unconfirmed/possible mix-up" to "confirmed by Horizon, pre-release." **Please confirm at launch:** final model name (site uses "XLR Element 4.0 Mg" for the *existing* Venatic DM chassis; your new one is the *XLR Atom* — different chassis, so the name is plausible), exact weight (to substantiate "sub-6 lb"), and MSRP. Until it's public, reps are told not to send prospects to a product page.
5d. **CORRECTION — Seekins PH3 NRL trigger:** live site shows **TriggerTech Primary @2.5 lb, not Diamond** (Diamond is the HIT Pro M3 only). Our earlier `audits/seekins.md` **F3** proposed an NRL score bump *based on the Diamond claim* — that correction is likely invalid and should be dropped if/when phase-1 is revisited. Sales battlecard already fixed. *(Two of our agents read the same Seekins page oppositely — worth a 30-sec human spot-check.)*
5e. **Christensen appears to have CUT MSRPs** since our audit: live site shows **Mesa FFT $1,499.99** (was $1,699.99) and **Ridgeline FFT Titanium ~$2,549–$2,599** (was ~$3,300–$3,399). This makes Christensen materially *more* price-competitive than the battlecard's price-objection framing assumes — the Christensen card's "$3,300 Ti" reference is now stale. Refresh before heavy use. Also: **Christensen Evoke** sub-$1,000 value line confirmed (~$999).
5f. **Bergara Premier LRP & Ridgeback are DISCONTINUED** (last MSRP ~$2,000 / ~$2,329). They were the named rival in 4 phase-1 matchups (Vandal DM, Venatic Riff, Venatic Max, Vena-Bull) — i.e., those used a legacy analog. Phase-1 note only; not re-running.
5g. **Fierce CT Rival XP price conflict on Fierce's own page:** price widget $2,999 vs body copy $2,699. Price reference uses $2,999; verify at point of sale if a Rival XP matchup is decisive.
5. **Point-of-sale pricing + promotions** for all brands were not refreshed. Confirm before quoting exact price gaps, especially around seasonal promos.
6. **Horizon's own delivery confidence is thin (~17 sources, Low–Medium).** Every battlecard instructs reps to say "no comparable pattern found," not "proven better." As our volume/owner data grows this should be re-audited — and the QC-lottery risk that sank rivals tends to appear *as* volume scales, so locking QC process now matters (assessment §8).

### Lower priority (watch items)
7. **Christensen moves:** new president (Shane Meisel, Jan 2026) and a sub-$1,000 **Evoke** line surfaced but weren't assessed — both could shift the "value 5.0 / improving CS" picture. Worth a follow-up if they come up in the field.
8. **Fierce's 4 newest SKUs** (CT Rival XP, Carbon Rage LR, MTN Reaper 2.0, Reaper H-TAC 2.0) have almost no owner data — genuine gap on both sides; revisit when data accumulates.
9. **Seekins spec corrections** (PH3 NRL = TriggerTech Diamond; Element M3 = 10 chamberings) are our corrections against a third-party report, not Seekins' own copy — spot-check seekinsprecision.com before a deal where these are decisive.
10. **Stiller-action historical QC thread** (in `audits/horizon.md`) is dated/unclear vintage — not used as a claim; if a prospect raises Stiller's reputation, route to product/engineering rather than improvising.

## Corrected edition (design-spec rebuild) note
Built `Horizon_Comparative_Analysis_UNBIASED_2026_CORRECTED.html` (+ PDF) from
`Comparative_Analysis_DESIGN_SPEC.md` — same skin as the original, fed the corrected
audit data. Result: **Horizon tops 3 of 14** (matches Scenario B). Full methodology +
every score override is in `BUILD_NOTES.md`; regenerate with `python3 build_edition.py`.
Two decisions to confirm:
- **11a. Scope = the original 14 models only.** The new SKUs (Rabble Core Pistol, dealer
  Bandit, pre-release XLR-Atom Mg SBR) are NOT scored in it — phase-1 scoring is paused
  per your instruction and there are no official photos for them (design is one photo per
  Horizon model). They're noted in Appendix C instead. Add them once scoring is un-paused
  and photos exist.
- **11b. Which edition ships?** The corrected edition applies the same-spec rule to
  Horizon too, so it is *less* flattering (3 wins, not 4) but defensible line-by-line. If
  this is for external/customer use vs. internal truth-telling, confirm which framing you
  want before distribution.

## Phase 3 (MDT × Lone Peak) note
The Phase-3 agent hit a session limit on the first run and was re-launched after reset. See `MDT_LonePeak_threat_assessment.md` for its own "Open questions / assumptions log" (verification gaps on the acquisition timing, the MDT trigger's specs/reception, and whether MDT has signaled any intent to sell complete rifles vs. staying components-only).
