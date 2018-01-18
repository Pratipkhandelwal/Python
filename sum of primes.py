n=int(input())
import math
for  p in range(n):
    l,r = map(int,input().split())
    k=[]
    for num in range(l,r+1):
        if num >1:
            if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
               k.append(num)

               
    print(sum(k))
