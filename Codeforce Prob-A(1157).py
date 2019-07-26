n = int(input())
s = str(n)
x = n
k = []
k.append(n)
if(n==1):
    print(9)
else:    
    while(int(s)!=0):
        s = str(int(s) + 1)
        while(s[-1]=='0'):
            s = s[:-1]
        else:
            s = s
            if(int(s) in k):
                break
            else:
                k.append(int(s))
    print(len(k))

