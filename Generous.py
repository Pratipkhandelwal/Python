n,k=input().split()
a=input()
d=dict((letter,a.count(letter))
for letter in set(a))
x=0
for value in d.values():
    if(value > int(k)):
          x+=1
    else:
          x=0  
if(x>0):
  print("NO")
else:
  print("YES")
          
          


