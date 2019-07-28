from fractions import gcd
t=int(input())
m=10**9+7
for i in range(t):
    a,b,c=map(int,input().split())
    num = pow(b,c)
    print(num)
    den = gcd(a,pow(b,c))
    print(den)
    print((num//den)% m)
