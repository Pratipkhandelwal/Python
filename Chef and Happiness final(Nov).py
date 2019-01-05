from collections import defaultdict

t = int(input())
for z in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    a = list()
    b = list()
    for i in range(0,len(s)):
        a.append(s[s[i]-1])
        b.append(i+1)
    print(a)
    print(b)
    for i in range(0,len(a)-1):
        if(a[i]==a[i+1] and b[i]!=b[i+1]):
            flag=1
            break
        else:
            flag=0
            
    if(flag==1):
        print("Truly Happy")
    else:
        print("Poor Chef")
