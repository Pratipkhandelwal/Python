n,m=map(int,input().split())
l=list()
k=list()
z=list()
num=list((input().split()))
for i in range(m):
      u,v=map(int,input().split())
      l.append(u)
      l.append(v)

for j in set(l):
      k.append(int(num[int(j-1)]))
      
from fractions import gcd
res=gcd(*k[:2])
for x in k[:2]:
      res = gcd(res,x)

print(res)      


    
           
