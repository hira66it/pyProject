def minesweeper(matrix):
    tmp_list_t=[]
    for i in range(len(matrix)):
        tmp_list=[]
        for j in range(len(matrix[0])):
            tmp=0
            for k in range(-1,2):
                for l in range(-1,2):
                    if (k,l)==(0,0) or :continue
                    try:
                        if matrix[i+k][j+l]:tmp+=1
                    except:continue
            tmp_list.append(tmp)
        tmp_list_t.append(tmp_list)
    return tmp_list_t

print(minesweeper([[True,False,False,True], 
 [False,False,True,False], 
 [True,True,False,True]]))