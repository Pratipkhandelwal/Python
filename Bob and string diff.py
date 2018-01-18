import math
t = int(input())
for k in range(t):
    a = input()
    b = input()
    c1=[0]*26
    for i in range(0,len(a)):
        c1[ord(a[i]) - 97]+=1

    c2=[0]*26    
    for i in range(0,len(b)):
            c2[ord(b[i])- 97]+=1
    ans=0        
    for i in range(0,26):
        if(c1[i]!=c2[i]):
            ans+= abs(c1[i]-c2[i])
    print(ans)        
    
