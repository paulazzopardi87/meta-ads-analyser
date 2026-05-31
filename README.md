# Meta Ads Analyser

> Stop guessing. Get a clear verdict on every ad — with the maths to back it up.

A structured toolkit for small e-commerce brands running Meta ads. Paste your Meta Ads Manager CSV export, get a clear weekly verdict for every ad: **SCALE / KEEP / WATCH / FIX PAGE / KILL / NO DECISION YET** — with the reasoning and numbers behind each call.

---

## What's in this repo

```
meta-ads-analyser/
├── skill/
│   └── SKILL.md                  # Cowork skill — install in Claude desktop app
├── docs/
│   ├── magic-prompt.md           # Copy-paste prompt for Claude / ChatGPT (no install)
│   ├── operating-system.md       # The full playbook — the why behind every rule
│   └── quick-start.md            # Get running in 5 minutes
├── assets/
│   └── column-preset.md          # Exact Meta Ads Manager column setup
└── README.md
```

---

## Quick start

### Option A — Cowork skill (Claude desktop app)
1. Open `skill/SKILL.md` in Claude / Cowork
2. Click **Save skill**
3. Attach a Meta Ads Manager CSV and say **"analyse my ads"**

### Option B — Copy-paste prompt (any AI chat)
1. Open `docs/magic-prompt.md`
2. Fill in your product economics at the top (once only)
3. Paste the whole thing into Claude or ChatGPT with your CSV
4. Works on free tiers

---

## The three things that matter most

1. **Most day-to-day swing is noise, not skill** — never judge cost-per-sale on tiny numbers; pool the data and judge weekly
2. **Your real break-even is probably higher than you think** — the toolkit calculates it from your actual margins, not a rule of thumb
3. **Consolidate** — fewer, better-funded ad sets beat many starved ones every time

---

## How to export from Meta Ads Manager

Desktop only. Takes 90 seconds.

1. Go to Meta Ads Manager → **Ads tab** (not Campaigns or Ad Sets)
2. Set date range: **Last 7 days**
3. Click **Columns → Customise columns**, add:
   - Ad name · Ad set name · Impressions · Reach · Amount spent
   - Link clicks · CTR (link click-through rate) · CPC (cost per link click)
   - Add to cart · Purchases · Purchase ROAS · Cost per purchase
4. Save the column set as a preset (e.g. `"My Ads OS"`) — one click next time
5. **Export → Download as CSV**

---

## The verdict system

| Verdict | What it means |
|---|---|
| **SCALE** | Working. Raise budget 20–30% or duplicate. Never double overnight. |
| **KEEP** | Fine. Leave it running. |
| **WATCH** | Too early, or on the edge. Check again in 3–4 days. |
| **FIX PAGE** | Ad is getting clicks but losing people on the landing page. Fix the page. |
| **KILL** | Past the data threshold. CTR and CPC are clearly bad. Turn it off. |
| **NO DECISION YET** | Too little data. Toolkit tells you what to wait for. |

---

## Sold on Etsy

This toolkit is available as a polished digital download on Etsy. If you found it via GitHub, feel free to use it directly — the Etsy listing is for buyers who want a formatted, ready-to-go document.

---

## Licence

MIT — use it, adapt it, share it. Attribution appreciated but not required.
