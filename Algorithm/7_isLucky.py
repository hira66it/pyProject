def sortByHeight(a):
    b = a[:]
    tmp=[]
    i=0
    while -1 in b:
        del b[b.index(-1)]
    b = sorted(b)

    for x in a:
        if not x ==-1:
            tmp.append(b[i])
            i+=1
        else:tmp.append(-1)
    return tmp