t = int(input())
for z in range(t):
    n = int(input())
    a = list()
    flag=1
    for i in range(n):
        a.append([int(j) for j in input().split()])
    b = min(a[0])    
    for k in range(1,n):
       c = min(a[k])
       if(c <=b):
            print('-1')
            flag = 0
            break
    if(flag==0):
        continue

    if(flag==1):   
            val = max(a[n-1])
            pro = val
            for p in range(n-2, -1 , -1):
                for q in range(0,n):
                    a[p].sort(key = int, reverse = True)
                    diff = val - a[p][q]
                    if(diff > 0):
                        pro =  a[p][q] + pro
                        val = a[p][q]
                        break
                    else:
                        continue                           
    print(pro)
