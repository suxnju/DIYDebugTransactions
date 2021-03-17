import json

def slot2txs(tx2slots:'Dict') -> 'Dict':
    s2t = {}
    for tx in tx2slots:
        for slot in set(tx2slots[tx]['read'] + tx2slots[tx]['write']):
            if slot in s2t:
                s2t[slot].append(tx)
            else:
                s2t[slot] = [tx]

    with open("slot2txs.json","w",encoding="utf-8") as f:
        json.dump(
            {k:v for k,v in s2t.items()},
            f,
            indent='\t'
        )

def freq():
    with open("slot2txs.json","r",encoding="utf-8") as f:
        freq = json.load(f)

    res = {}
    for f in freq:
        if len(freq[f]) in res:
            res[len(freq[f])] += 1
        else:
            res[len(freq[f])] = 1

    res = {a[0]:a[1] for a in sorted(res.items(),key=lambda x: x[1],reverse=True)}

    with open("freq.json","w",encoding="utf-8") as f:
        json.dump(res,f,indent='\t')

if __name__ == "__main__":
    with open("./result.json","r") as f:
        slot2txs(json.load(f))
    freq()