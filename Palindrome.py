t=int(input())
for i in range(0,t):
    s=input()
    x=(str(s)[::-1])
    if s==x:
        print ("YES")
    else:
        print ("NO")
        
