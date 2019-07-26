t = int(input())
s = [0]
for _ in range(t):
    a = list(map(int,input().split()))
    if(len(a)==1):
        print(min(s), s)
    if(len(a)==2):
        if(a[0]==1):
            s.append(a[1])
            print(s)
        else:
            print(s)
            for i in range(0,len(s)):
                s[i] = s[i]^a[1]
                
    
