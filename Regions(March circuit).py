import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


t = int(input())
for z in range(t):
    n,m,k,l = map(int,input().split())
    total = n*m
    if(k==1):
        print(total)
    elif(l==1):
        value = ncr(total,k)
        print(value)
    else:
        first = ncr(total,k)
        second = l*m*n
        print(abs(first-second))
        


