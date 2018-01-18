from collections import Counter
from itertools import groupby
t = int(input())
for z in range(t):
    n,m = map(int,input().split())
    a = input()
    b = input()
    s = a[0]
    i=1
    j=0
    while(i < n and j < m):
        if(i<j):
           s=s+a[i]
           i+=1
        elif(i>j):
           s=s+b[j]
           j+=1
        else:
            s=s+a[i]
            s=s+b[j]
            i+=1
            j+=1
            

    while(i<n):
         s+=s+a[i]
         i+=1
    while(j<m):
         s=s+b[j]
         j+=1

    print(s)     
    c = [''.join(g) for _, g in groupby(s)]
    print(c)
    print(len(c))
