import math


from itertools import accumulate
from operator import mul

def prod(lst):
    for value in accumulate(lst, mul):
        pass
    return value


t = int(input())
for z in range(t):
    n = int(input())
    x = [i for i in range(1,n+1)]
    add = sum(x)
    mult = prod(x)
    print(x)
    print(add)
    print(mult)
    if(add%mult == 0):
        print("YES")
    else:
        print("NO")
