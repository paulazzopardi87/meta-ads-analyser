# Methodology: why every rule exists

This file explains the reasoning behind each threshold in `SKILL.md`. Use it to explain a verdict, or to check yourself on a borderline call.

---

## 1. Unit economics: the only "benchmark" that matters

A good CPA is not an industry number. It is whatever leaves you profit after the sale.

```
Net revenue per order   = AOV − VAT portion
Contribution per order  = Net revenue − COGS − payment fees − fulfilment
Break-even CPA          = Contribution per order
Break-even ROAS         = AOV (gross) ÷ Contribution per order
Target CPA              = 60–80% of break-even CPA
```

**Worked example (UK, VAT-registered):** AOV £30.00 incl. VAT → VAT £5.00 → net £25.00. COGS £6.00, fees £0.80, fulfilment £3.20 → **contribution £15.00**.
Break-even CPA = **£15.00**. Target CPA = **£9.00–£12.00**. Break-even ROAS = 30 ÷ 15 = **2.00**.

Why use *gross* AOV for ROAS: Meta's purchase value comes from your pixel/CAPI, which normally sends the price the customer paid, including VAT. Comparing Meta ROAS to a break-even worked out on net revenue would flatter every ad. If your store sends ex-VAT values, use net AOV instead.

Why 60–80%: at exactly break-even you make £0 per sale and still carry overheads, returns and refunds. The 20–40% buffer is where actual profit comes from.

---

## 2. Why the data gate exists: purchases are noisy

Conversions follow, roughly, a Poisson distribution. Small counts swing a lot by pure chance.

**Example:** an ad with a true CPA of £12 spends £50. Expected sales = 4.2. The 95% range is **1 to 9 sales**, so the same ad could "show" a CPA of £50 or £5.56 in a given week. Judging it on that week is judging luck.

### How wide is the uncertainty at each purchase count? (95% interval on true CPA)

| Purchases observed | True CPA could be |
|---|---|
| 3 | −66% to +385% of observed |
| 5 | −57% to +208% |
| **10** | **−46% to +109%** |
| 15 | −39% to +79% |
| **25** | **−32% to +55%** |
| 50 | −24% to +35% |

That's why:
- **10 purchases** is enough to call *direction* ("this is probably above break-even"), but not to fine-tune.
- **25 purchases** is enough for confident budget moves.
- Money is judged **pooled at ad-set level**. One ad rarely hits these counts in a week.

### When can you kill with zero sales?

If the true CPA were exactly your target, the chance of seeing **zero** purchases after spending N × target CPA is e^(−N):

| Spend with 0 purchases | Chance it's actually fine (bad luck) |
|---|---|
| 1× target CPA | 37% |
| 2× target CPA | 14% |
| **3× target CPA** | **5%** |

So **3× target CPA with no sales** is the zero-sales kill line. The same logic for exactly one sale: P(≤ 1 purchase) = e^(−N)(1 + N), which drops to ~4% at **5× target CPA**. That's the one-sale kill line. Killing earlier means you'll wrongly kill roughly 1 in 3 to 1 in 7 decent ads.

### Creative metrics need far less data

CTR is a proportion over impressions, which come in thousands, so it settles fast. At a 1.5% CTR, the 95% margin of error is:

| Impressions | ± margin on CTR |
|---|---|
| 1,000 | ±0.75 pts |
| **2,000** | **±0.53 pts** |
| 5,000 | ±0.34 pts |

At 2,000 impressions you can reliably tell a 0.8% ad from a 1.6% ad, which is enough to kill a clearly weak creative. That's why creative can be judged in days, but money takes a week or more.

ATC rate works the same way over link clicks: at 100 clicks, a 5% ATC rate is 5 ± ~4 adds. That's coarse but enough to spot a page that converts at 1% versus 6%.

---

## 3. How long to leave data untouched

| Rule | Reason |
|---|---|
| **No judgement in the first 72 h** of an ad or after a significant edit | Meta's delivery explores in the first days (odd placements, odd audiences). Early CPA/CTR is not representative. |
| **Money decisions use ≥ 7-day windows** | Covers a full weekday/weekend cycle; weekly purchase patterns are real. |
| **Prefer a window that ends yesterday** | Ads Manager attributes conversions to the impression/click date, and with 7-day click attribution late conversions keep arriving. The last 1–2 days always look worse than they'll end up. |
| **After a budget change, wait 3–4 days before the next one** | Big or frequent changes push the ad set back into learning; you also can't attribute the result. |
| **Change one thing per ad set per review** | Otherwise next week's result is uninterpretable. |
| **Review weekly, kill creative any time** | Creative kills (gate: 2k impressions) can happen mid-week. Money calls wait for the weekly review. |

**Learning phase:** Meta says an ad set needs about 50 optimisation events in 7 days to exit learning. If budget × 7 ÷ target CPA is far below 50, the ad set will never exit learning. That's a structure problem (too many ad sets), not a creative one. Meta has changed this guidance before, so treat the "Learning / Learning limited" status in Ads Manager as the source of truth.

---

## 4. Why diagnose by layer

Each metric only tells you about its own stage of the funnel:

```
Impression → (hook) → Link click → Landing page view → Add to cart → Checkout → Purchase
 CREATIVE LAYER         │  PAGE / OFFER LAYER            │  MONEY LAYER
 hook rate, CTR, CPC    │  LPV ÷ clicks, ATC ÷ clicks    │  CVR, CPA, ROAS
```

- Bad CTR, fine ATC → the ad is weak, the page is fine. **KILL/ITERATE the creative.**
- Great CTR, terrible ATC → the ad works, the page/offer doesn't (or the ad over-promises). **FIX PAGE.** Killing the ad would throw away a working hook.
- LPV ÷ link clicks < 70% → people click but leave before the page loads. That's usually page speed.
- Healthy ATC, no purchases → checkout friction, delivery cost shock, trust, or payment options.

Relative thresholds (e.g. "≤ 60% of account median CTR") are used because baselines vary hugely by niche, price point and placement. A £300 product will have a lower CTR than a £15 impulse buy, and both can be healthy.

---

## 5. Fatigue

Prospecting creative wears out as the same people see it repeatedly. Signals, together:
- Frequency rising past ~2.5–3 in a 7-day window (prospecting; retargeting tolerates more)
- CTR falling ≥ 25% vs the previous period
- CPC/CPM rising

One week of data can't show a trend. For fatigue checks, export **two consecutive 7-day windows** (or add a Day breakdown) so the skill can compare.

---

## 6. Attribution and the backend check

Meta's numbers are a model, not a ledger. They can over-count (view-through, modelled conversions, overlapping retargeting) or under-count (iOS tracking opt-outs, ad blockers, cross-device). The defensible top-line check is **MER**:

```
MER            = Total store revenue ÷ Total ad spend
Break-even MER = AOV ÷ Contribution per order   (same formula as break-even ROAS)
```

If MER is under break-even MER, ads are losing money overall, whatever per-ad ROAS says. If you run other channels at the same time, MER covers all of them. Say so when you read it.

---

## 7. Sources and further reading

- Meta Business Help Centre: *About the learning phase*; *About significant edits*; *About attribution settings*
- Poisson confidence intervals for counts (exact/Garwood method), used for the CPA table above
- Normal approximation for a binomial proportion, used for the CTR margin table

Thresholds here are heuristics built on that maths, tuned for small brands spending roughly £20–£500/day. Above that, tighten them: you'll hit the gates quickly, so require more data before each call.
