# Meta Ads Analyser

**A free weekly Meta ads review that thinks like a performance marketing manager.**

Export your Meta Ads Manager CSV, add your margins once, and get one verdict per ad: what to **scale**, **keep**, **iterate**, **fix** or **kill**. Each verdict is backed by your break-even maths and refuses to make calls the data can't support yet.

Works as a **Claude skill**, or as a **copy-paste prompt** in any AI chat. No code, no API keys, no account access.

![License: MIT](https://img.shields.io/badge/license-MIT-green) ![Works with Claude](https://img.shields.io/badge/works%20with-Claude%20%7C%20ChatGPT%20%7C%20Gemini-blue)

---

## Why this exists

Most ad "analysis" fails in one of three ways:

1. **It reacts to noise.** An ad with 3 sales at £8 CPA looks like a winner, but the true CPA could be anywhere from £3 to £39. This tool has a [data gate](#the-data-gate) and won't judge a layer until there's enough data for it.
2. **It uses someone else's benchmarks.** "Good ROAS is 3" means nothing. Your break-even comes from *your* price, VAT, COGS and fulfilment, and that's what every verdict is measured against.
3. **It caves when you push back.** Ask a chatbot "are you sure?" and it flips. This one separates *new data* (re-run) from *context* (adjust the action, state the cost) from *preference* ("your call, but here's what I'd do, and here's what would change my mind").

---

## What you get

A one-line summary, **max 3 actions ranked by £ impact**, then a table like this ([full sample report →](examples/sample-report.md)):

| Ad | Verdict | Key numbers | Reason |
|---|---|---|---|
| Carousel - Full range | **KILL (creative)** | 6.4k impr · CTR 0.7% · CPC £1.00 | CTR half the account median; enough data to call it |
| Static - 15% off | **KILL (money)** | £48 · 0 purchases | 0 sales at 4× target CPA, about a 2% chance that's bad luck |
| Video - Founder story | **FIX PAGE** | CTR 2.1% · ATC 2.1% · LPV 63% | Best hook in the account; the page loses them |
| UGC - Unboxing | **SCALE** | 26 purchases · CPA £9.23 | Ad set clears every scale gate: +25% budget |
| Video - New hook test | **NO DECISION YET** | 880 impr | Needs 2,000 impressions. Check again at that point |

---

## Get started

### Option 1: Claude skill (recommended)

**Claude.ai (web, desktop or mobile):**
1. Make sure code execution is on: Settings → Capabilities → **Code execution and file creation** (called "Create and edit files" in newer layouts). Skills need it.
2. Download [`dist/meta-ads-analyser.zip`](dist/meta-ads-analyser.zip). Don't unzip it.
3. Go to [Customize → Skills](https://claude.ai/customize/skills) → **+** → **Create skill** → **Upload a skill** → choose the zip.
4. Check the skill's toggle is on.

Works on Free, Pro, Max, Team and Enterprise plans. On Team/Enterprise, an admin may need to allow user-created skills.

**Claude Code:**

```bash
git clone https://github.com/paulazzopardi87/meta-ads-analyser.git
```

```bash
cp -r meta-ads-analyser/meta-ads-analyser ~/.claude/skills/
```

Then attach your CSV and say **"analyse my ads"** (or, to force it, *"use the meta-ads-analyser skill"*). First time, it asks for your economics.

### Option 2: Copy-paste prompt (any AI chat)

Open [`docs/magic-prompt.md`](docs/magic-prompt.md), fill in your economics once, paste it into Claude / ChatGPT / Gemini with your CSV. Works on free tiers.

### Export your data

Ads Manager → **Ads** tab → **Last 7 days** → columns from [`docs/column-preset.md`](docs/column-preset.md) → Reports → Export table data (CSV). Save the column preset once and the weekly export takes 15 seconds. Full walkthrough: [`docs/quick-start.md`](docs/quick-start.md).

---

## How decisions are made

### 1. Your economics set the bar

```
Contribution per order = AOV − VAT − COGS − payment fees − fulfilment
Break-even CPA         = contribution per order        (above this, every sale loses money)
Target CPA             = 60–80% of break-even CPA      (where profit lives)
Break-even ROAS        = AOV ÷ contribution per order
```

### 2. The data gate

Each layer of the funnel needs a different amount of data before it can be judged. Below the gate, the verdict is **NO DECISION YET**, with a date to check back.

| Judging | Needs at least | Why |
|---|---|---|
| Anything | **72 h live**, and 72 h since the last significant edit | Delivery is erratic early on and after edits |
| Creative (CTR, CPC, hook) | **2,000 impressions** | CTR is then accurate to ±0.5 pts |
| Landing page (add-to-cart rate) | **100 link clicks** | Fewer clicks = a handful of add-to-carts = noise |
| "It's not converting" | **3× target CPA spent, 0 sales** (or 5× with 1) | ~5% chance a decent ad looks that bad by luck |
| CPA direction | **10 purchases**, pooled at ad-set level, 7+ days | True CPA is still −46% / +109% of what you see |
| Confident budget moves | **25 purchases** pooled | Range tightens to −32% / +55% |

### 3. Diagnose by layer, so you fix the right thing

```
Impression → Click → Page load → Add to cart → Checkout → Purchase
 CREATIVE           │  PAGE / OFFER                       │  MONEY
 hook, CTR, CPC     │  LPV ÷ clicks, ATC rate             │  CPA, ROAS vs break-even
```

Great CTR with terrible add-to-cart is a **page** problem. Killing the ad would throw away a working hook.

### 4. The verdicts (first match wins)

| Verdict | When | Do |
|---|---|---|
| **NO DECISION YET** | Below the data gate | Wait. Report says until when |
| **KILL (creative)** | CTR clearly below your median, CPC above it | Turn it off |
| **FIX PAGE** | Ad is fine, page/offer is losing people | Fix the named page issue |
| **KILL (money)** | 0 sales at 3× target CPA, or 1 sale at 5× | Turn it off |
| **ITERATE** | One part works, one doesn't, or fatigue is setting in | 1–2 variants, change one thing |
| **SCALE** | Ad set has 15+ purchases, CPA ≤ target, ROAS ≥ break-even, and this ad is carrying it | +20–30% budget, then hands off for 3–4 days |
| **KEEP** | Profitable, between target and break-even | Leave it alone |
| **WATCH** | Borderline | Exact trigger, e.g. "kill if CPA > £14 after £40 more" |

Ad sets get their own call: **SCALE** (raise budget 20–30%) or **CUT** (pause a failing prospecting ad set; for a testing ad set, turn off the losers and cap its budget instead).

The maths behind every threshold: [`methodology.md`](meta-ads-analyser/references/methodology.md).

---

## How long should I leave ads alone?

- **72 hours** after launch or any significant edit before judging anything
- **7 days** (ending yesterday) for any money decision. The last 1–2 days always under-report sales
- **3–4 days** between budget changes
- **One change per ad set per week**, so you can tell what worked

---

## Repo layout

```
meta-ads-analyser/
├── meta-ads-analyser/            # The Claude skill (install this folder)
│   ├── SKILL.md                  #   Rules, verdict logic, output format
│   └── references/methodology.md #   The maths and reasoning behind each threshold
├── dist/meta-ads-analyser.zip    # Same skill, zipped for upload to Claude.ai
├── docs/
│   ├── magic-prompt.md           # Copy-paste version for any AI chat
│   ├── quick-start.md            # 10-minute setup + weekly routine
│   └── column-preset.md          # Exact Ads Manager columns to export
├── examples/
│   ├── sample-export.csv         # Example Meta export (fictional brand)
│   └── sample-report.md          # The report it produces
└── tests/
    ├── check_rules.py            # Applies the verdict rules to fixed datasets; must all pass
    ├── fixtures/                 # Edge-case and campaign-level test exports
    └── README.md                 # How the skill was QA'd, and what was found
```

Rebuild the zip after editing the skill:

```bash
rm -f dist/meta-ads-analyser.zip && zip -qr dist/meta-ads-analyser.zip meta-ads-analyser && python3 tests/check_rules.py
```

---

## How it's tested

- **Rules as code:** [`tests/check_rules.py`](tests/check_rules.py) applies the verdict rules literally to two datasets: the sample and an edge-case file built to sit right on the thresholds. Every verdict must match. Currently 25/25.
- **Blind runs:** fresh Claude agents, given *only* the skill (or only the copy-paste prompt) and a CSV, reproduced every expected verdict on both datasets: 7/7, 12/12 and 12/12.
- **Behaviour:** separately tested for asking for economics before judging, refusing to scale when margins are negative, handling campaign-level exports, ignoring instructions hidden in ad names, holding a verdict under pushback, and changing it when given real new data.

Details and what each run found: [`tests/README.md`](tests/README.md).

## Limits (read before trusting it with real money)

- It's a decision framework run by an LLM, not a calculator. Check the maths it shows you, especially on large accounts.
- Built for small e-commerce brands spending roughly £20–£500/day on purchase-optimised campaigns. Lead gen, app installs and very large accounts need different gates.
- Meta's attribution is a model. Add your Shopify/backend revenue for an MER check. When the two disagree, trust the backend.
- First-order economics by default. If you have strong repeat purchase, you can tell it to use LTV, but go in knowing that.

## Licence

[MIT](LICENSE). Free to use, adapt and share.
