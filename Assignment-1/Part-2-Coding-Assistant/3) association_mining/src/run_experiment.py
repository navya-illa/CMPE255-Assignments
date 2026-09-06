import argparse, json
from pathlib import Path
from itertools import combinations
import numpy as np, pandas as pd

def main():
    p=argparse.ArgumentParser(); p.add_argument('--data'); p.add_argument('--output',required=True); a=p.parse_args(); out=Path(a.output); out.mkdir(parents=True,exist_ok=True); data=Path(a.data); rng=np.random.default_rng(42); items=['milk','bread','eggs','coffee','fruit','yogurt','cereal','chicken','rice','pasta']; n=10000
    if data.exists(): baskets=json.loads(data.read_text())
    else:
        baskets=[]
        for _ in range(n): baskets.append(sorted(set(rng.choice(items,size=int(rng.integers(2,6)),replace=False).tolist())))
        data.parent.mkdir(parents=True,exist_ok=True); data.write_text(json.dumps(baskets))
    counts={i:sum(i in b for b in baskets) for i in items}; rows=[]
    for x,y in combinations(items,2):
        both=sum(x in b and y in b for b in baskets); support=both/len(baskets); confidence=both/max(counts[x],1); lift=confidence/(counts[y]/len(baskets)) if counts[y] else 0
        if support>=.035: rows.append({'antecedent':x,'consequent':y,'support':round(support,4),'confidence':round(confidence,4),'lift':round(lift,4)})
    rules=pd.DataFrame(rows).sort_values('lift',ascending=False); rules.to_csv(out/'apriori-rules.csv',index=False); result={'algorithm':'Apriori','rules':int(len(rules)),'top_lift':round(float(rules['lift'].max()) if len(rules) else 0,4),'transactions':len(baskets)}; (out/'results-summary.json').write_text(json.dumps(result,indent=2)); print(result)
if __name__=='__main__': main()
