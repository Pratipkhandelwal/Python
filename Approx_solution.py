import random

n = int(input())
for i in range(n):
    x,y,w = map(int,input().split())
    
a = random.randint(1,100000)
b = random.randint(1,100000)
c = random.randint(100000,900000)

print(-a,b,c)
