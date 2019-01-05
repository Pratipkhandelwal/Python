from itertools import combinations_with_replacement 

n = int(input())
a = list(map(int,input().split()))
m = int(input())
c = 0
for _ in range(m):
    l,r,x = map(int,input().split())
    gap = [y for y in range(l,r+1)]
    c = 0
    comb = combinations_with_replacement(gap, 3)
    combo = [(2, 2, 2),(2, 2, 3),(2, 2, 4),(2, 3, 3),(2, 3, 4),(2, 4, 4),(3, 3, 3),(3, 3, 2),(3, 3, 4),(3, 2, 2),(3, 2, 4),(3, 4, 4),(4, 4, 4) ,(4, 4, 2) ,(4, 4, 3) ,(4, 2, 2) ,(4, 2, 3) ,(4, 3, 3)]
    for i in list(combo):
        arr = i
        z = a[(arr[0]-1)]&a[(arr[1]-1)]&a[(arr[2]-1)]
        print(a[(arr[0]-1)],a[(arr[1]-1)],a[(arr[2]-1)],'',z)
        if(z==x):
            c+=1

    print(c)  
