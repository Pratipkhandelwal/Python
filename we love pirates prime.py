import math
from math import sqrt
from itertools import count,islice

def primes(n):
    return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
          

t = int(input())
for z in range(t):
    n = int(input())
    a = list()
    for num in range(2,n+1):
          if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
             a.append(num)
          
    f=0
    b = list()
    for i in range(0,len(a)-1):
            val = 0
            for j in range(i,len(a)-1):
                val = sum(a[i:j+2])
                k = primes(val)
                if k is True:
                    b.append(val)

                
    print(len(set(b)))        
    
    
