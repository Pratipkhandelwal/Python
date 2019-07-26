from math import sqrt
from itertools import count, islice


def gcd(a,b):
    if(b==0):
        return a
    return gcd(b, a%b)
    

def isPrime(c):
    if c < 2:
        return False

    for number in islice(count(2), int(sqrt(c) - 1)):
        if c % number == 0:
            return False

    return True


t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    for i in range(1,n+1):
        z = gcd(i,n)
        if(z==1):
            c+=1
            
    val = isPrime(c)

    if(val==False):
        print("FALSE")
    else:
        print("TRUE")
