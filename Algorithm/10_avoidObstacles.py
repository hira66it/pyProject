def avoidObstacles(inputArray):
    a= sorted(inputArray)
    spot=[]
    
    tmp=0
    for i in range(len(a)-1):
        if a[i+1]-a[i]>1:
            spot.append(a[i]+1)
            spot.append(a[i+1]-1)
    spot.append(a[-1]+1)
    spot.insert(0,0)
    spot = sorted(list(set(spot)))
    for i in range(len(spot)-1):
        if spot[i+1]-spot[i]>tmp:
            tmp = spot[i+1]-spot[i]
    return tmp
print(avoidObstacles([1, 4, 10, 6, 2]))