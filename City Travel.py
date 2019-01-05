import math
 
s, x, n=list(map(int, input().strip().split()))
A={}
for _ in range(n):
    i, value=list(map(int,input().strip().split()))
    A[i]=value
i=0 
last=0
flag=3
for k in sorted(A.keys()):
    normal_days=k-last-1
    if s<=normal_days*x:
        print('less',k, normal_days, s, i)
        i+=math.ceil(s/x)
        s=0
        print('less-1',s,i)
        break
    else:
        print('more',k, normal_days, s, i)
        s-=normal_days*x
        s-=A[k]
        i=k
        last=k
    if s<=0:
        flag=0
        break
        print('more-1',k,s,i)
if s>0:
    flag=1
    print('in',s,i)
    i+=math.ceil(s/x)
print(i,flag)
