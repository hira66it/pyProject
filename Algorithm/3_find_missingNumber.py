def missingNumber(arr):
    tmp_1=0
    tmp_2=0
    length = len(arr)
    print(length)
    for i in range(length):
        tmp_1 += arr[i]
        tmp_2 += i
    tmp_2 += (length)
    return tmp_2 - tmp_1
print(missingNumber([0,1,2,3,5]))