from collections import Counter
from itertools import groupby
t = int(input())
for z in range(t):
    n,m = map(int,input().split())
    a = input()
    b = input()
    s = ''.join(sorted(a)+sorted(b))

    c = [''.join(g) for _, g in groupby(s)]
    print(len(c)+1)

    
        
        
