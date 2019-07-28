n,k = map(int,input().split())
a=list()
b=list()
c=list()
for i in range(0,n):
    if(i==0):
        a = list(map(int,input().split()))
    elif(i==1):
        b = list(map(int,input().split()))
    else:
        c = list(map(int,input().split()))


if(n==3):
        
    fin = 999999
    for t in range(0,k):
        x=list()
        y=list()
        z=list()
        for i in range(0,n):    
            x.append((a[i]+t) %k)
            y.append((b[i]+t) %k)
            z.append((c[i]+t) %k)    
        val = max(sum(x),sum(y),sum(z))
        fin = min(val,fin)

elif(n==2):

    fin = 999999
    for t in range(0,k):
        x=list()
        y=list()
        for i in range(0,n):    
            x.append((a[i]+t) %k)
            y.append((b[i]+t) %k)  
        val = max(sum(x),sum(y))
        fin = min(val,fin)

else:

    fin = 999999
    for t in range(0,k):
        x=list()
        for i in range(0,n):    
            x.append((a[i]+t) %k)
        val = sum(x)
        fin = min(val,fin)

print(fin)
