def get_data():
    sum_temp=[]

    T = input()
    for i in range(T):
        tmp=[]
        (N,K) = input().split()
        for j in range(N):
            tmp_j = input()
            for k in range(N):
                tmp[j][k]= tmp_j.split()
def main():
    # get_data()
    (a,b)=input().split()
    print(a,b)

if __name__=="__main__":
    main()