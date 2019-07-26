import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

n,r = map(int,input().split())

print(ncr(n,r))


11
2 2 2 1
2 2 1 2
2 2 2 2
4 2 1 2
4 2 1 1
4 2 1 3
4 2 2 2
4 2 2 3
3 5 1 3
3 5 2 3
3 5 2 1

