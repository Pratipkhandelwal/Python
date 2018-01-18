def dec_to_bin(y):
    return int(bin(y)[2:])

def equality(m):
    v = str(m)
    d=list()
    for i in range(len(v)):
        if(v[i]=='1'):
            d.append(i)
    return d

def sec_equal(r):
    v = str(r)
    e=list()
    for i in range(len(v)):
        if(v[i]=='1'):
            e.append(i)
    return e

n = int(input())
h = list(map(int,input().split()))
q = int(input())
for z in range(q):
    x,y = map(int,input().split())
    z = dec_to_bin(x)
    b = list()
    inx = list()
    print("bin is:",z)
    inx = equality(z)
    print("inx :",inx)
    for k in range(0,n):
        c = dec_to_bin(k)
        inxy=list()
        if(k==0):
            inxy.append(0)
        else:
            inxy = sec_equal(c)
        print("inxy :",inxy)
        if(inx == inxy):
            h[k] = h[k]-y
            b.append(h[k])
        else:
            b.append(h[k])      
    val = sum(j> 0 for j in b)
    for p in range(0,n):
        h[p] = b[p]
    print(val)
            
            
               
