# LC #260 Single Number III
# Algorithm practicing
# 2019-02-27 Wed

def test(input_arr):
    xor = 0
    for el in input_arr:
        xor^=el
    idx = 0
    print("xor : {0:b}".format(xor))
    for i in range(32):
        if((xor>>i) & 1) ==1:
            idx =i
            print(xor>>i)
            print("idx : ",idx)
            break
    xor1 =0
    xor2 =0
    for el in input_arr:
        if((el>>idx & 1) ==1):
            print("1 : ",el)
            xor1 ^= el
        else:
            print("2 : ",el)
            xor2 ^= el
    return (xor1,xor2)

print(test([1,1,2,2,3,12]))