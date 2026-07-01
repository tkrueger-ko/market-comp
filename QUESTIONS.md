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
4b. **Sub-6 lb SKU specifics (follow-on to resolved #3) — STILL OPEN:** model name, actual weight, chambering(s), MSRP, and order/availability status — reps need these to sell it concretely rather than say "something's coming." (Pricing agent may surface some of this from the site.)
4c. **RMA turnaround — RESOLVED:** ~2 weeks, and the rifle comes back with **a handwritten note from a senior leader and a box of ammo.** This is now the signature CS proof point across the playbook and all four battlecards — a tangible, hard-to-copy "we take care of you" moment.

### Product scope
5b. **The report's 14-model Horizon lineup is incomplete.** Horizon confirms at least one SKU the original analysis missed: a **magnesium XLR Atom chassis SBR (~$3,999, Stiller Hyrax action, standard Riff/DM chamberings)** — distinct from the Venatic Riff (13" SBR, Wombat action, ~$3,799). The pricing agent is capturing the full current site lineup and flagging any other missed SKUs. *Decision for you: do you want the phase-1 competitive scoring re-run to include the full current lineup, or is the sales/pricing capture sufficient?*
5. **Point-of-sale pricing + promotions** for all brands were not refreshed. Confirm before quoting exact price gaps, especially around seasonal promos.
6. **Horizon's own delivery confidence is thin (~17 sources, Low–Medium).** Every battlecard instructs reps to say "no comparable pattern found," not "proven better." As our volume/owner data grows this should be re-audited — and the QC-lottery risk that sank rivals tends to appear *as* volume scales, so locking QC process now matters (assessment §8).

### Lower priority (watch items)
7. **Christensen moves:** new president (Shane Meisel, Jan 2026) and a sub-$1,000 **Evoke** line surfaced but weren't assessed — both could shift the "value 5.0 / improving CS" picture. Worth a follow-up if they come up in the field.
8. **Fierce's 4 newest SKUs** (CT Rival XP, Carbon Rage LR, MTN Reaper 2.0, Reaper H-TAC 2.0) have almost no owner data — genuine gap on both sides; revisit when data accumulates.
9. **Seekins spec corrections** (PH3 NRL = TriggerTech Diamond; Element M3 = 10 chamberings) are our corrections against a third-party report, not Seekins' own copy — spot-check seekinsprecision.com before a deal where these are decisive.
10. **Stiller-action historical QC thread** (in `audits/horizon.md`) is dated/unclear vintage — not used as a claim; if a prospect raises Stiller's reputation, route to product/engineering rather than improvising.

## Phase 3 (MDT × Lone Peak) note
The Phase-3 agent hit a session limit on the first run and was re-launched after reset. See `MDT_LonePeak_threat_assessment.md` for its own "Open questions / assumptions log" (verification gaps on the acquisition timing, the MDT trigger's specs/reception, and whether MDT has signaled any intent to sell complete rifles vs. staying components-only).
