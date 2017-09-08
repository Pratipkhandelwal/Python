from collections import OrderedDict
n,k = map(int, input().split())
num = list(map(int, input().split()))
l=OrderedDict()
data=list()
for i in (num):
    mod = i%k
    l[i]=mod
data.append(sorted(l, key=l.__getitem__))
for j in data:
    print(*j)
    
    

