t = int(input())
for z in range(t):
    a,b,c,d,k = map(int, input().split())
    for i in range(1,100):
        curr = a*(i**3) + b*(i**2) + c*(i) + d
        print(curr,k)
        if(curr<=k):
            continue
        else:
            print(i-1)
            break
        
