import itertools

n = int(input())
a = list(map(int,input().split()))
m = int(input())
c = 0
for _ in range(m):
    l,r,x = map(int,input().split())
    f = 1
    for i in range(l-1,r):
        f = f*(a[i]+1)
    print(f)
