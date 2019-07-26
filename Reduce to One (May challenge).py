t = int(input())
for j in range(0,t):
    n = int(input())
    a = [x for x in range(1,n+1)]
    if(len(a)==1):
        print(a[0])
    else:        
        while(len(a)!=1):
            val = a[0] + a[-1] + a[0]*a[-1]
            del a[0]
            del a[-1]
            a.append(val)            
        print(a[0] % mod)


#3
#10000
#39193487
#100000
#755072380
