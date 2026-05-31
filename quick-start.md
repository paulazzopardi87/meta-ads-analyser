# Quick start — 5 minutes to your first verdict

## Before you begin (once only)

Answer these questions. You'll paste the answers into the prompt or skill — you only do this once.

| Question | Your answer |
|---|---|
| Product name & RRP | e.g. My Widget — £24.99 |
| VAT-liable? (yes/no) | If yes, ~16.7% of RRP goes to HMRC |
| COGS (cost to make/buy one unit) | e.g. £4.50 |
| Payment processing fee | e.g. £0.50 or ~2% |
| Fulfilment cost per order | e.g. £3.20 — or £0 if passed to customer |
| Currency | £ / $ / € |
| Daily ad budget range | e.g. £60–£120/day |

The AI calculates your break-even ROAS, break-even CPA, and target CPA from these automatically.

---

## Export your data (90 seconds)

Desktop only — Meta doesn't support column customisation on mobile.

1. Go to [Meta Ads Manager](https://adsmanager.facebook.com)
2. Click the **Ads** tab (not Campaigns or Ad Sets)
3. Set date range: **Last 7 days**
4. Click **Columns → Customise columns** and add these (use the search bar):

   ```
   Ad name
   Ad set name
   Impressions
   Reach
   Amount spent
   Link clicks
   CTR (link click-through rate)
   CPC (cost per link click)
   Add to cart
   Purchases
   Purchase ROAS
   Cost per purchase
   ```

5. Save as a preset — name it `"My Ads OS"` — so next week it's one click
6. Click **Export → Download as CSV**

---

## Run the analysis

### If you have the Cowork skill installed:
1. Start a new chat in the Claude desktop app
2. Attach the CSV (or paste the data)
3. Say: **"analyse my ads"**
4. Answer the economics questions if it's your first run

### If you're using the copy-paste prompt:
1. Open `docs/magic-prompt.md`
2. Fill in your economics at the top (the section marked "fill in once")
3. Paste the whole file into a new Claude or ChatGPT conversation
4. Paste your CSV where indicated
5. Send

---

## Read the output

**Read the Account Summary first.** The 1–2 highest-leverage actions are at the top.

Then the per-ad table. Act on **SCALE** and **KILL** verdicts within 24 hours. Log **WATCH** ads for next week.

---

## Your weekly routine (once set up)

| Step | Action |
|---|---|
| 1 | Meta Ads Manager → Last 7 days → Ads tab → Export CSV |
| 2 | Open Claude or ChatGPT, start a new conversation |
| 3 | Paste the prompt (or trigger the skill) and paste the CSV |
| 4 | Optional: add Shopify revenue/orders for a blended MER check |
| 5 | Read Account Summary, then per-ad table |
| 6 | Act on SCALE and KILL verdicts within 24 hours |

Total time: under 5 minutes.
