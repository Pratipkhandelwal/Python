mod = 1000000007

def product(a,k):

    res = 1
    for i in range(0,k):
        res = (res * a[i]) % mod

    return res

n = int(input())
arr = list(map(int,input().split()))

for i in range(0,len(arr)-1):
    l = arr[:i+1]
    r = arr[i+1:]
    prod_l = product(l,len(l))
    prod_r = product(r,len(r))
    if(prod_l == prod_r):
        print(i+1)
        break
    
