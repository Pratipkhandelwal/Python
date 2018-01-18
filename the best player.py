n,t = map(int,input().split())
a = dict()
for p in range(n):
    s,k = map(str,input().split())
    a[s] = int(k)
z=(sorted(a, key=lambda x: (-a[x], x)))
for i in range(0,t):
    print(z[i])
    
