t = int(input())
for j in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    max_sum = -999999999
    sum1 = 0
    c_sum = 0
    for i in range(n):
        sum1+=arr[i]
        if sum1>max_sum:
            max_sum = sum1
        if sum1<0:
            sum1 = 0
    print (max_sum)
