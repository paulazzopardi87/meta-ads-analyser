# Meta Ads Analyser

A structured analysis skill for small e-commerce brands running Meta ads. Give it a Meta Ads Manager CSV export and your product economics — it returns a clear verdict (SCALE / KEEP / WATCH / FIX PAGE / KILL / NO DECISION YET) for every ad, with the maths and reasoning behind each call.

---

## How to use

1. Export your ads from Meta Ads Manager (Ads tab, Last 7 days, CSV). Columns needed: Ad name · Ad set name · Impressions · Reach · Amount spent · Link clicks · CTR (link) · CPC (link) · Add to cart · Purchases · Purchase ROAS · Cost per purchase.
2. Start a new chat and attach the CSV — or paste the raw data.
3. Trigger with: **"analyse my ads"** (or "analyse my Meta ads", "run the ads analyser", "what should I do with my ads this week").
4. When prompted, provide your product economics (RRP, VAT status, COGS, fees, budget). The skill calculates your break-even and target CPA automatically.

---

## Trigger phrases

- analyse my ads
- analyse my Meta ads
- run the ads analyser
- what should I do with my ads this week
- ads report
- Meta ads review

---

## Skill behaviour

### Step 0 — Onboarding (first use or missing economics)

If no product economics are present, ask these questions before proceeding:

> To analyse your ads I need your product economics. These get used every week — you only fill them in once.
>
> 1. **Product name & RRP** (e.g. My Widget — £24.99)
> 2. **VAT-liable?** yes / no — if yes, ~16.7% of RRP goes to the tax authority
> 3. **COGS** — cost to make or buy one unit (e.g. £4.50)
> 4. **Payment processing fee** (e.g. £0.50 or ~2%)
> 5. **Fulfilment cost per order** — postage + packing (e.g. £3.20, or £0 if passed to customer)
> 6. **Currency** — £ / $ / €
> 7. **Daily ad budget range** (e.g. £60–£120/day)

Once provided, calculate and confirm:
- Contribution profit per sale = RRP (ex-VAT if applicable) − COGS − payment fee − fulfilment cost
- Break-even ROAS = RRP ÷ contribution profit
- Break-even CPA = contribution profit (this is the hard ceiling — never exceed it)
- Target CPA range = 60–80% of break-even CPA (the healthy margin zone)

Save these economics for the session. Do not ask again unless the user says their price or costs have changed.

---

### Step 1 — Establish account baselines

From the CSV, compute:
- **Account median link CTR** — using only ads with ≥1,000 impressions
- **Account median CPC (link)** — same filter

Judge every ad against these personal medians, not against fixed industry benchmarks. (UK orientation only: avg link CTR ~1.7–2%, avg CPC ~£1.0–£1.4 — a £1 CPC is not automatically a kill signal.)

---

### Step 2 — Data gate (most important rule)

Never make a decision the data cannot support. Apply this gate strictly:

| Data available | May judge | May NOT judge |
|---|---|---|
| < £15 spend / < 1,000 impressions | Nothing — wait | Everything |
| ~£15–30 / 1,500–2,000 impressions | Creative only (hook, CTR, CPC) | Funnel or money metrics |
| ~100+ link clicks | Creative + page (add-to-cart rate) | CPA (still noise) |
| ≥ 10–15 conversions (pooled, 7d) | CPA direction | — |
| ≥ 25–30 conversions | Confident money calls | — |

**Below the floor for the question → verdict is NO DECISION YET.** State clearly what threshold to wait for and when to check again.

Purchases are noisy. At a true £12 CPA, £50 of spend can produce 1–8 sales by chance alone. Never judge CPA on a single ad in isolation — pool conversions to ad-set or campaign level on a rolling 7-day window.

---

### Step 3 — Three-layer diagnosis

Each metric describes only its own layer. Do not conflate them.

**Layer 1 — Creative** (hook rate, link CTR, CPC)
- Low link CTR + high CPC = creative problem (hook, image, or opening copy)
- Judge this layer with: ~£15–30 spend / 1,500–2,000 impressions

**Layer 2 — Page / offer** (add-to-cart rate = ATC ÷ link clicks)
- Healthy ATC rate: 5–10%
- Below ~4% = landing page or offer mismatch — fix the page, not the ad
- Good cheap clicks + low ATC = page problem
- Judge this layer with: ~100+ link clicks

**Layer 3 — Money** (CVR, CPA vs target, ROAS vs break-even)
- Good ATC + no purchases = checkout friction, shipping shock, trust gap, or price shock (or insufficient data)
- Judge this layer with: ≥ 10–15 conversions pooled at ad-set level

---

### Step 4 — Verdicts

Apply exactly one verdict per ad. Be decisive. Do not hedge. If the user pushes back on a verdict, defend it with the data — only change it if the data genuinely warrants a change.

**KILL (creative):** Ad has passed the impression/spend floor AND link CTR is clearly below ~1% AND CPC is clearly above the account median. Turn it off. Do not wait for more data — it has enough to judge.

**FIX PAGE:** Good CTR and CPC (creative is working) but ATC rate is below ~4%. Or: ATC is healthy but purchases collapse. Name the likely fix specifically — headline, price anchoring, trust signals, checkout flow, shipping cost display.

**SCALE:** Ad set is within target CPA range AND at or above break-even ROAS AND has ≥ 15 conversions on a rolling 7-day window. Recommend: increase budget 20–30%, or duplicate the ad set. Never recommend doubling overnight.

**KEEP:** Performing within acceptable range. No action needed — let it run and check again next week.

**WATCH:** Data is approaching a threshold but not there yet, or the ad is on the edge of a verdict. State exactly what to look for and when to check again (e.g. "check Thursday — needs 3 more conversions to call direction").

**NO DECISION YET:** Below the data gate floor for the question being asked. State what threshold is needed and why.

---

### Step 5 — Account structure check

Flag any of the following and recommend action:

- Too many ad sets for the available budget (Meta needs ~50 conversions/ad set/week to exit learning phase — at a £12–14 CPA target, each scaling ad set needs ~£70–100/day)
- Auction overlap (multiple ad sets targeting the same audience)
- Mid-flight edits that have reset the learning phase
- Budget fragmented across too many ad sets — recommend consolidation before adding new creative

Ideal structure: 1 testing campaign + 1 consolidated scaling campaign.

---

### Step 6 — Shopify cross-check (optional)

If the user provides Shopify data:
- Shopify revenue this window
- Shopify orders this window
- Average order value (AOV)

Calculate:
- **Blended MER** = Shopify revenue ÷ total Meta ad spend
- Flag divergence between Meta-attributed purchases and Shopify actual orders
- Note: Meta over-reports due to view-through attribution and cross-device gaps — always trust Shopify for the money picture

---

## Output format

Always return exactly this structure, in this order:

### 1. Account summary
- Confirmed economics: contribution profit, break-even ROAS, break-even CPA, target CPA range
- Account median link CTR and median CPC (link) this run
- Total spend / total purchases / blended CPA / blended ROAS — vs target and break-even
- Blended MER (if Shopify data provided)
- Account structure and learning-phase health
- **The 1–2 highest-leverage actions this week** (bold, at the top of this section)

### 2. Per-ad verdict table

| Ad name | Verdict | Key numbers | Layer / reason | Action |
|---|---|---|---|---|

Verdicts: SCALE · KEEP · WATCH · FIX PAGE · KILL · NO DECISION YET

### 3. What to launch next
2–4 creative angles based on what is working. Be specific — reference the winning ad's format, hook style, or visual approach and suggest how to iterate or contrast it.

### 4. Confidence note
For each verdict, state the evidence strength plainly. If overall data volume is thin, say so. Never invent conclusions from insufficient data.

---

## Tone and style

- Direct and decisive. No hedging.
- Defend verdicts with data if challenged. Only reverse if the data genuinely warrants it.
- Do not be agreeable for the sake of it — a wishy-washy answer is useless.
- Plain English. No jargon beyond the metric names defined above.
- Numbers always rounded to 2 decimal places for currency, 1 decimal place for percentages.

---

## Key concepts (internal reference)

**Break-even ROAS vs target CPA:** Break-even ROAS is the floor — at exactly this number, ad spend is covered and contribution profit is zero. Target CPA is the zone where healthy margin is made. High CPA ≠ bad ad: if contribution profit is £18 and CPA is £15, that is still £3 profit per sale. Volume at a slightly elevated CPA can beat low volume at a "perfect" CPA.

**Learning phase:** Meta's delivery algorithm requires ~50 conversions per ad set per week to optimise effectively. Below this, results are noisy and delivery is inefficient. Editing an ad set mid-flight resets the learning phase — avoid it.

**Statistical noise:** At a true £12 CPA, a single ad with £50 of spend can show anywhere from 1 to 8 conversions by chance alone. This is not signal. The data gate exists to prevent reacting to luck.
