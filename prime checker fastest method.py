from math import sqrt
from itertools import count,islice

def isPrime(n):
    return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

z = int(input())
a = isPrime(z)
if a is True:
    print(1)
else:
    print(0)
    

