n = int(input())
a = list(map(int,input().split()))
res  = list()
for i in range(0,n):
    for j in range(i,n):
        for k in range(i,j+1):
                res.append(a[k])


print(res)
print(set(res))


    
