import math
t = int(input())
for z in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(0,n):
        for j in range(0,n):
            f = a[i]/a[j]
            rem = f - int(f)
            if rem >= 0.5 :
                ans += math.ceil(f)
            else:
                ans += math.floor(f)
                
    print(ans)        
