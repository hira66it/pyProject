def boxBlur(img):
    tmp_t = []
    for j in range(len(img)-2):
        tmp=[]
        for i in range(len(img[0])-2):
            tmp.append(sum([img[j+x][i+y] for y in range(3) for x in range(3)])//9)
        tmp_t.append(tmp)
    return tmp_t
print(boxBlur([[36,0,18,9], 
 [27,54,9,0], 
 [81,63,72,45]]))