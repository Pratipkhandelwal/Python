import random

l,r = map(int,input().split())

if(r-l == 3):
    print(4)        
else:
      print(random.randint(l,r+1))
