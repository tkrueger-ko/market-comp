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

### Highest priority (affects whether reps can make our strongest claim)
1. **What is Horizon's *actual* warranty/accuracy-guarantee policy — is there a fee to invoke it, and what's the real turnaround?** Our biggest wedge against Fierce is their $200 fee + slow CS. Reps must be able to state our own terms as the clean contrast. Research only found a generic "contact us if not grouping after 40 shots" FAQ line. **Please confirm the official policy** so the playbook can state it as fact.
2. **Do we ship (or will we ship) a per-rifle fired test target?** The consolidated assessment's #1 recommendation. It's referenced as an aspiration, not a current practice — confirm current state so reps don't imply something we don't do.
3. **Sub-6 lb / titanium mountain SKU — is it real and on a timeline?** Both the Fierce and Christensen battlecards tell reps to concede weight and "offer to follow up when our titanium option ships." Is there one in development, and can reps reference it? If not, remove that line.

### Medium priority (accuracy / freshness)
4. **Current Horizon MSRP master sheet.** Our audits cite a $2,299–$9,999 range but no per-model price list; reps need exact deltas vs specific competitor models. Where's the current price sheet?
5. **Point-of-sale pricing + promotions** for all brands were not refreshed. Confirm before quoting exact price gaps, especially around seasonal promos.
6. **Horizon's own delivery confidence is thin (~17 sources, Low–Medium).** Every battlecard instructs reps to say "no comparable pattern found," not "proven better." As our volume/owner data grows this should be re-audited — and the QC-lottery risk that sank rivals tends to appear *as* volume scales, so locking QC process now matters (assessment §8).

### Lower priority (watch items)
7. **Christensen moves:** new president (Shane Meisel, Jan 2026) and a sub-$1,000 **Evoke** line surfaced but weren't assessed — both could shift the "value 5.0 / improving CS" picture. Worth a follow-up if they come up in the field.
8. **Fierce's 4 newest SKUs** (CT Rival XP, Carbon Rage LR, MTN Reaper 2.0, Reaper H-TAC 2.0) have almost no owner data — genuine gap on both sides; revisit when data accumulates.
9. **Seekins spec corrections** (PH3 NRL = TriggerTech Diamond; Element M3 = 10 chamberings) are our corrections against a third-party report, not Seekins' own copy — spot-check seekinsprecision.com before a deal where these are decisive.
10. **Stiller-action historical QC thread** (in `audits/horizon.md`) is dated/unclear vintage — not used as a claim; if a prospect raises Stiller's reputation, route to product/engineering rather than improvising.

## Phase 3 (MDT × Lone Peak) note
The Phase-3 agent hit a session limit on the first run and was re-launched after reset. See `MDT_LonePeak_threat_assessment.md` for its own "Open questions / assumptions log" (verification gaps on the acquisition timing, the MDT trigger's specs/reception, and whether MDT has signaled any intent to sell complete rifles vs. staying components-only).
