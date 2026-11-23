# Meta Ads Manager: column preset

Set this up once and save it as a preset. After that, a weekly export takes about 15 seconds. Desktop only.

## Required columns

| Search for | Why the analyser needs it |
|---|---|
| Ad name | Identifies the creative |
| Ad set name | Money metrics are pooled at ad-set level |
| Impressions | Creative data gate (≥ 2,000) |
| Amount spent | Spend gates, CPA |
| Link clicks | Page data gate (≥ 100), ATC rate |
| CTR (link click-through rate) | Creative layer. Use the **link** version, not "CTR (all)" |
| CPC (cost per link click) | Creative layer. Use the **link** version |
| Adds to cart | Page / offer layer |
| Purchases | Money layer |
| Purchase ROAS (return on ad spend) | Compared against your break-even ROAS |
| Cost per purchase | CPA |

## Strongly recommended

These let the analyser use the full diagnosis (fatigue, hook, page speed, checkout):

| Search for | Unlocks |
|---|---|
| Campaign name | Pooling for CBO / Advantage+ campaigns |
| Delivery / Ad delivery | Spots learning / learning-limited |
| Reach, Frequency | Fatigue detection |
| Landing page views | Page-speed / bounce diagnosis (LPV ÷ link clicks) |
| Checkouts initiated | Splits page problems from checkout problems |
| Purchases conversion value | More precise ROAS / AOV |
| 3-second video plays | Hook rate (video ads) |
| ThruPlays | Hold rate (video ads) |

Reporting starts/ends are included in exports automatically.

## Save as preset

Columns → Customise columns → add the above → tick **Save as preset** → name it `Ads Analyser` → Apply.

## Date range

| Purpose | Range |
|---|---|
| Weekly review | **Last 7 days, ending yesterday** (custom range, or "Last 7 days" which excludes today) |
| Fatigue check | Also export the **previous 7 days**, or add Breakdown → By time → Day |
| New creative test | Lifetime, but no calls before 72 h and the data gates |

## Attribution

The analyser assumes Meta's default **7-day click / 1-day view**. If you use something else, tell it. That changes how much lag the recent days have.

## Exporting

Ads tab (not Campaigns / Ad sets) → Reports → **Export table data** → CSV.
