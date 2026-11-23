"""Regression check: apply SKILL.md's verdict rules literally to the sample
export and confirm they reproduce examples/sample-report.md.

Run: python3 tests/check_sample.py
If you change a threshold in SKILL.md, mirror it here and re-run.
"""
import csv, os, statistics as st, sys
from collections import defaultdict

# Sample brand economics (see examples/sample-report.md)
AOV = 30.0
BE = 15.0          # break-even CPA = contribution per order
T = 0.8 * BE       # target CPA (top of 60-80% range)
BEROAS = AOV / BE

HERE = os.path.dirname(os.path.abspath(__file__))
R = list(csv.DictReader(open(os.path.join(HERE, "..", "examples", "sample-export.csv"))))
f=lambda r,k: float(r[k] or 0)
for r in R:
    r['imp']=f(r,'Impressions'); r['sp']=f(r,'Amount spent (GBP)'); r['cl']=f(r,'Link clicks')
    r['p']=f(r,'Purchases'); r['atc']=f(r,'Adds to cart'); r['lpv']=f(r,'Landing page views')
    r['ctr']=r['cl']/r['imp']*100; r['cpc']=r['sp']/r['cl']; r['atcr']=r['atc']/r['cl']*100
    r['freq']=f(r,'Frequency')
big=[r for r in R if r['imp']>=1000]
mctr=st.median(r['ctr'] for r in big); mcpc=st.median(r['cpc'] for r in big); matc=st.median(r['atcr'] for r in big)
AS=defaultdict(lambda:[0,0])
for r in R: AS[r['Ad set name']][0]+=r['sp']; AS[r['Ad set name']][1]+=r['p']
def verdict(r):
    s,p=AS[r['Ad set name']]
    if r['imp']<2000: return 'NO DECISION YET'
    if r['ctr']<=0.6*mctr and r['cpc']>mcpc: return 'KILL (creative)'
    if r['ctr']>=mctr and r['cpc']<=mcpc and r['cl']>=100 and (r['atcr']<0.6*matc or r['lpv']/r['cl']<0.7): return 'FIX PAGE'
    if (r['p']==0 and r['sp']>=3*T) or (r['p']==1 and r['sp']>=5*T): return 'KILL (money)'
    own=r['sp']/r['p'] if r['p'] else 1e9
    if p>=15 and s/p<=T and p*AOV/s>=BEROAS and (own<=T or r['p']>=p/2): return 'SCALE'
    if p>=10 and s/p<=BE and own<=BE: return 'KEEP'
    return 'WATCH'
def setcall(s,p):
    if (p==0 and s>=3*T) or (p==1 and s>=5*T) or (p>=10 and s/p>1.25*BE): return 'KILL (money)'
    if p>=15 and s/p<=T and p*AOV/s>=BEROAS: return 'SCALE'
    return '-'

EXPECTED_ADS = {
    "UGC - Unboxing (video)": "SCALE",
    "Static - Benefit headline": "KEEP",
    "Carousel - Full range": "KILL (creative)",
    "Video - Founder story": "FIX PAGE",
    "Static - 15% off": "KILL (money)",
    "Video - New hook test": "NO DECISION YET",
    "Static - Reviews carousel": "WATCH",
}
EXPECTED_SETS = {
    "Broad - Advantage+ audience": "SCALE",
    "Interest - Gift buyers": "KILL (money)",
    "Retargeting - 30d site visitors": "-",
}

fails = 0
for r in R:
    got, want = verdict(r), EXPECTED_ADS[r["Ad name"]]
    ok = got == want; fails += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {r['Ad name']:28} {got}" + ("" if ok else f"  (expected {want})"))
for k, (s, p) in AS.items():
    got, want = setcall(s, p), EXPECTED_SETS[k]
    ok = got == want; fails += not ok
    print(f"{'PASS' if ok else 'FAIL'}  [ad set] {k:28} {got}" + ("" if ok else f"  (expected {want})"))
sys.exit(1 if fails else 0)
