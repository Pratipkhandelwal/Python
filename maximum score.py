t = int(input())
for q in range(t):
    n = int(input())
    a = list()
    flag = 1
    for i in range(n):
        a.append([int(j) for j in input().split()])
    b = min(a[0])    
    for k in range(1,n):
       c = min(a[k])
       if(c<b):
           print('-1')
           flag = 0
           break
        
    if flag==1:
        val = max(a[n-1])
        pro = val
        for p in range(n-2, -1 , -1):
            d = list()
            for q in range(0,n):
               d.append(val - a[p][q])

            ix = d.index(min(d))
            if(a[p][ix] < val):        
                pro = pro + a[p][ix]
                val = a[p][ix]
            else:
                d.remove(ix)
                continue

    print(pro)
            
                
            
                
                
            
                
           

