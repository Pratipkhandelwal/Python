def func(n):
    r = 1
    mod = 1000000007
    for i in range(1, n + 1):
        r *= i % mod
    return r % mod

t = int(input())
for j in range(0,t):
    n = int(input())
    val = func(n+1)
    print(val-1)
