t = int(input())
for p in range(t):
    e=list()
    a,b,c,d = map(int,input().split())
    e.append(a)
    e.append(b)
    e.append(c)
    e.append(d)
    e.sort()
    if(e[0]==e[1] and e[2]==e[3]):
        print("YES")
    else:
        print("NO") 
        
