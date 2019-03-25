from bisect import bisect_left
    
def getBeauty(n):
    beauty = 0
    while(n>0):
        beauty+=(n&1)
        n = n//2

    return beauty

def binarysearch(arr,x):
    j = bisect_left(arr,x)
    if j:
        return(j)
    else:
        return -1

t = int(input())
for z in range(t):
    x = int(input())
    s = 0
    k = 0
    arr = []
    for i in range(0,40):
        p = getBeauty(i)
        s+=p
        arr.append(s)
        print(i,p,s)
    res = binarysearch(arr,x)
    #print(res)
    
