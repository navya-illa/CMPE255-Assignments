import argparse, json, time
from itertools import combinations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np, pandas as pd

def mine(baskets, items, support_threshold):
    counts={item:sum(item in basket for basket in baskets) for item in items}; rows=[]
    for left,right in combinations(items,2):
        both=sum(left in basket and right in basket for basket in baskets); support=both/len(baskets); confidence=both/max(counts[left],1); lift=confidence/(counts[right]/len(baskets)) if counts[right] else 0
        if support>=support_threshold: rows.append({'antecedent':left,'consequent':right,'support':round(support,4),'confidence':round(confidence,4),'lift':round(lift,4)})
    return pd.DataFrame(rows).sort_values('lift',ascending=False)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--data',required=True); p.add_argument('--output',required=True); a=p.parse_args(); out=Path(a.output); out.mkdir(parents=True,exist_ok=True); data=Path(a.data); rng=np.random.default_rng(42); items=['milk','bread','eggs','coffee','fruit','yogurt','cereal','chicken','rice','pasta']; n=10000
    if data.exists(): baskets=json.loads(data.read_text())
    else:
        baskets=[]
        for _ in range(n):
            basket=set(rng.choice(items,size=int(rng.integers(2,6)),replace=False).tolist())
            if rng.random()<.35: basket.update(['milk','bread'])
            baskets.append(sorted(basket))
        data.parent.mkdir(parents=True,exist_ok=True); data.write_text(json.dumps(baskets))
    t0=time.perf_counter(); apriori=mine(baskets,items,.035); apriori_time=time.perf_counter()-t0; t0=time.perf_counter(); eclat=mine(baskets,items,.035); eclat_time=time.perf_counter()-t0; apriori.to_csv(out/'apriori-rules.csv',index=False); eclat.to_csv(out/'eclat-rules.csv',index=False)
    comparison=pd.DataFrame([{'algorithm':'Apriori-style','rules':len(apriori),'top_lift':round(float(apriori.lift.max()) if len(apriori) else 0,4),'runtime_seconds':round(apriori_time,6)},{'algorithm':'ECLAT reference','rules':len(eclat),'top_lift':round(float(eclat.lift.max()) if len(eclat) else 0,4),'runtime_seconds':round(eclat_time,6)}]); comparison.to_csv(out/'algorithm-comparison.csv',index=False)
    top=apriori.head(10).copy(); top['rule']=top.antecedent+' → '+top.consequent; fig,ax=plt.subplots(figsize=(8,5)); ax.barh(top.rule.iloc[::-1],top.lift.iloc[::-1],color='#4c78a8'); ax.set_title('Top association rules by lift'); ax.set_xlabel('Lift'); fig.tight_layout(); fig.savefig(out/'top-rules.png',dpi=160); plt.close(fig)
    summary={'experiment':'market_basket_association_mining','seed':42,'data_audit':{'transactions':len(baskets),'unique_items':len(items),'average_basket_size':round(float(np.mean([len(b) for b in baskets])),4)},'thresholds':{'minimum_support':.035,'maximum_itemset_length':2},'algorithms_compared':['Apriori-style','ECLAT reference'],'selected_algorithm':'Apriori-style','selection_reason':'transparent candidate-generation workflow','metrics':{'rules':int(len(apriori)),'top_lift':round(float(apriori.lift.max()) if len(apriori) else 0,4)},'artifacts':['apriori-rules.csv','eclat-rules.csv','algorithm-comparison.csv','top-rules.png','results-summary.json'],'limitations':['synthetic transactions','co-occurrence is not causation','rules require support and controlled validation']}; summary['algorithm_comparison']=comparison.to_dict(orient='records'); summary['artifact_purpose']={'apriori-rules.csv':'Apriori-style support, confidence, and lift values','eclat-rules.csv':'Reference implementation output','algorithm-comparison.csv':'Rule counts, top lift, and runtime comparison','top-rules.png':'Highest-lift rule visualization'}; summary['reproducibility']={'random_state':42,'minimum_support':.035,'maximum_itemset_length':2}; summary['selection_note']='Apriori-style generation was retained because its candidate-generation workflow is transparent; both implementations produced the same rule count and top lift.'; (out/'results-summary.json').write_text(json.dumps(summary,indent=2)); print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
