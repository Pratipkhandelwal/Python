n,m = map(int,input().split())
a = list(map(int,input().split()))
for z in range(m):
    x,l,r = map(int,input().split())
    if(x==1):
        b = a[l-1:r]
        p = l-1
        q = r
        for i in b:
            k=0
            for j in range(1,i+1):
                if(i%j==0):
                    k+=1
            a[p] = k
            p+=1
    else:
        print(sum(a[l-1:r]))
