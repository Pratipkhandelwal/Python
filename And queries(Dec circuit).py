import itertools

n = int(input())
a = list(map(int,input().split()))
m = int(input())
c = 0
for _ in range(m):
    l,r,x = map(int,input().split())
    gap = [y for y in range(l,r+1)]
    c = 0
    comb = itertools.product(gap, repeat=3)
    for i in list(comb):
        arr = i
        z = a[(arr[0]-1)]&a[(arr[1]-1)]&a[(arr[2]-1)]
        if(z==x):
            c+=1

    print(c)  
