t=int(input())
l=list()
for i in range(t):
    e=int(input())
    for j in range(e):
      a,b=input().split()
      x=int(a)
      y=int(b)
      l.append(x)
      l.append(y)
      
print(len(set(l)))    
    
    
