def commonCharacterCount(s1, s2):
    a = dict()
    b = dict()
    tmp=0
    for x in s1:
        if not x in a:
            a[x]=1
        else:a[x]+=1
    for x in s2:
        if not x in b:
            b[x]=1
        else:b[x]+=1
    print 
    for key in a.keys():
        if key in b:
            tmp+=min(a[key],b[key])
    return tmp
print(commonCharacterCount('abcc','abd'))