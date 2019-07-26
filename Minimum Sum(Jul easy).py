import math    

n,x = map(int,input().split())
arr = list(map(int,input().split()))
v = sum(arr)
for i in range(0,len(arr)):
    y = (arr[i]/x)
    if(x==1):
        value = arr[i]
    elif(y>=0):
        value = int(math.ceil(y))- 1
    else:
        value = int(math.floor(y)) - 1
    arr[i-1] = value * x
    print(value)

if(v<0):
    print(max(sum(arr),v))
else:
    print(min(sum(arr),v))
