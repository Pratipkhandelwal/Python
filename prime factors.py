def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def list_to_dict(li):  
     dct = {}  
     for item in li:  
             dct[item] = dct.get(item,0) + 1   
     return dct  

import itertools
n=int(input())
a=list()
a=prime_factors(n)
b = list_to_dict(a)
l=list(b.values())
print(len(set(list(itertools.permutations(l)))))


