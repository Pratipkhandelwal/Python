import math


from itertools import accumulate
from operator import mul

def prod(lst):
    for value in accumulate(lst, mul):
        pass
    return value

k = 0
l = []
l.append(0)
for j in range(1,100):
    x = [i for i in range(1,j+1)]
    add = sum(x)
    mult = prod(x)
    #print(j,add,mult,mult%add)
    if(mult%add!=0):
        l.append(mult%add)
        k+=1
        print(j," ",l[k]-l[k-1])

#print(l)
        
