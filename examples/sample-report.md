# Sample report

What the analyser returns for [`sample-export.csv`](sample-export.csv), a made-up brand. All numbers are computed from that file.

**Inputs given:** AOV £30.00 incl. 20% VAT · COGS £6.00 · fees £0.80 · fulfilment £3.20 · budget ~£90/day.
**Backend (Shopify), same week:** revenue £1,560.00 · 52 orders.

---

### 1. This week in one line
**Profitable overall, but the gift-buyers ad set is eating the profit. Shut it, put the money into Broad, and fix the founder-story landing page.**

### 2. Do this now

| # | Action | Why | Check |
|---|---|---|---|
| 1 | **Turn off ad set "Interest - Gift buyers"** (CUT). Move *Video - New hook test* into Broad; pause *Founder story* until its page is fixed | £152.00 spent for 1 purchase (5× target CPA is £60.00). Stops ~£137/week of lost contribution, and the freed ~£22/day funds action 2 | n/a |
| 2 | **Raise "Broad - Advantage+ audience" budget ~25%** (≈ £56 → £70/day) | 35 pooled purchases, CPA £11.29 (target ≤ £12.00), ROAS 2.66 (break-even 2.00) | 26 Nov, then +20–30% again if CPA ≤ £12 |
| 3 | **Fix the founder-story landing page, then retest that video in Broad** | Best CTR in the account (2.1%), but only 63% of clicks load the page and ATC is 2.1% | Once page is fixed + 100 new clicks |

### 3. Account summary

- **Economics:** net revenue £25.00 → contribution **£15.00**/order · break-even CPA **£15.00** · target CPA **£9.00–£12.00** · break-even ROAS **2.00**
- **Window:** 15–21 Nov (7 full days, today excluded ✓) · 7-day click / 1-day view
- **Totals:** spend £617.00 · 45 purchases · CPA £13.71 (above target, below break-even) · ROAS 2.19
- **Contribution after ads (Meta-attributed):** 45 × £15.00 − £617.00 = **+£58.00**. Broad +£130.00, Retargeting +£65.00, Gift buyers **−£137.00**
- **Baselines** (prospecting ads ≥ 1k impressions; retargeting excluded): CTR 1.4% · CPC £0.67 · ATC rate 4.4%
- **Assumed:** every ad except *New hook test* (status "Learning") has been live and unedited for 72 h+. Tell me about launches or edits next time
- **Backend:** MER 2.53 vs break-even 2.00 ✓ profitable. Meta reports 45 of 52 orders (87%), so it is slightly *under*-counting. The real picture is a bit better than Meta shows.
- **Structure:** ~£88/day ÷ £12 target CPA ≈ 51 purchases/week of capacity. That's enough for **one** prospecting ad set to exit learning, but there are two plus retargeting. Gift buyers is "Learning limited". Consolidate.

### 4. Per-ad verdicts

| Ad | Ad set | Verdict | Key numbers | Layer & reason | Action | Next check |
|---|---|---|---|---|---|---|
| Carousel - Full range | Broad | **KILL (creative)** | 6.4k impr · CTR 0.7% · CPC £1.00 | Creative: CTR is about half the median, CPC 50% above. Gate met (≥ 2k impr) | Turn off | n/a |
| Static - 15% off | Gift buyers | **KILL (money)** | £48.00 · 0 purchases · CTR 1.4% | Money: 0 sales at 4× target CPA (≈2% chance that's bad luck). Creative is fine, so the discount angle isn't converting | Turn off (goes with the ad set) | n/a |
| Video - Founder story | Gift buyers | **FIX PAGE** | CTR 2.1% · CPC £0.49 · 193 clicks · LPV 63% · ATC 2.1% | Page: hook is strong (best CTR, 25% hook rate), but 37% of clicks never load the page and ATC is under half the median (2.1% vs 4.4%) | Check page speed and message match on its URL; retest in Broad once fixed | After 100 clicks on fixed page |
| UGC - Unboxing (video) | Broad | **SCALE** | £240.00 · 26 purchases · CPA £9.23 · ROAS 3.25 · freq 1.65 | Money: carries 74% of the ad set's sales; ad set clears every scale gate | Part of the +25% ad-set increase; don't edit the ad | 26 Nov |
| Static - Benefit headline | Broad | **KEEP** | £110.00 · 8 purchases · CPA £13.75 · CTR 1.2% | Within break-even; ad-level CPA is a tiebreaker only (8 sales) | Leave running | 30 Nov |
| Static - Reviews carousel | Retargeting | **WATCH (promising)** | £70.00 · 9 purchases · CPA £7.78 · freq 4.2 | Money looks strong, but 9 < 10-purchase gate. Frequency 4.2 is normal for a small retargeting pool | Leave alone. If frequency > 6 and CTR falls 25%, refresh | 30 Nov |
| Video - New hook test | Gift buyers | **NO DECISION YET** | 880 impr · £9.00 | Below 2k-impression creative gate | Move into Broad when you shut Gift buyers | At 2k impressions |

### 5. What to launch next
1. **UGC unboxing, new hook.** Same video body, three new first-3-second openings (problem-first, price reveal, reaction shot). Control: *UGC - Unboxing*.
2. **Founder story, cut to 15 s**, pointing at the fixed page. Control: the current founder video. Tests whether the strong hook survives a shorter edit.
3. **UGC-style static.** Screenshot of a customer review over the unboxing still. Control: *Static - Benefit headline*. Tests whether social proof beats the benefit claim in static.

### 6. Confidence and what would change my mind

| Verdict | Confidence | Would change if… |
|---|---|---|
| SCALE Broad | **Medium** (35 purchases: true CPA plausibly £8–£16) | CPA rises above £13 over the next 7 days after the increase. Then hold budget |
| CUT Gift buyers | **High** (1 sale at ~13× target CPA) | Shopify shows gift-code orders that Meta missed. Send them over |
| KILL Carousel | **High** (6.4k impressions) | n/a. Creative signal is clear |
| FIX PAGE Founder | **Medium** (193 clicks) | Page speed and message match check out fine, then treat it as an audience problem and retest in Broad |
| WATCH Retargeting | **Low** (9 purchases) | One more good week makes this KEEP |
