t = int(input())
for z in range(t):
    n = int(input())
    size = []
    eat = []
    for z in range(n):
        s,e = map(int,input().split())
        size.append(s)
        eat.append(e)
    k = 0
    for i in range(0,len(eat)):
        if(eat[i] < min(size)):
            k+=1
    print(k)    
