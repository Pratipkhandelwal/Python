from math import sqrt
from itertools import count,islice


def isPrime(n):
    return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


l,r = map(int,input().split())
pr = list()
for i in range(l,r+1):
    a = isPrime(i)
    if(a is True):
            pr.append(i)
    else:
        if(i%2==0):
            if(i%3!=0):
                pr.append(i)

    
print(pr)        
