import math 

T = int(input())
for _ in range(T):
    N = int(input())
    k = int(input())
    A = list(map(int, input().split(' ')))
    mod = 1000000007
    prod = 1
    p = 2
    for i in range(1,N+1):
        prod = prod * p
    print(prod)
    final = ((prod % mod) * (prod % mod)) % mod
    print(final)
    
