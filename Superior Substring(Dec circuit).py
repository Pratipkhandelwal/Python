import collections
import math
 
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l1=  0
    for i in range(0,n):
        z = i
        for j in range(n,i,-1):
            sub = s[z:j]
            word = sub.count(s[z])
            if(word >= math.floor(len(sub)/2) and len(sub) > l1):
                l1 = len(sub)
                break
            else:
                continue
            
    print(l1)
