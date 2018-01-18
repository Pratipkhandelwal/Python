t = int(input())
for z in range(t):
    n = int(input())
    a = list()
    for i in range(n):
        a.append([int(j) for j in input().split()])

    val = max(a[n-1])
    pro = val
    flag=1
    for p in range(n-2, -1 , -1):
            x = [i for i in a[p] if i < val]
            if(len(x)==0):
                flag=0
            else:
                y = max(x)
                pro = pro + y
                val = y

    if(flag==0):
        print('-1')
    else:
        print(pro)
    
