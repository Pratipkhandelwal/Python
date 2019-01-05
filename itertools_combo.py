import itertools

a = [1,2,3,4,5,6]
arr = [itertools.combinations(a,i) for i in range(0,len(a)+1)]
l = [list(i) for i in arr]
k = 0
for i in range(0,len(l)):
            k+=len(l[i])
print(k)
    
