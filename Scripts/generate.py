with open("ttt.txt","w",encoding='utf-8') as f:
    for i in range(1,17):
        f.write("SWAP%s = functools.partial(SWAPXXX, idx=%s)\n"%(i,i))