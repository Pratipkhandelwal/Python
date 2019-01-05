n = int(input())
a = list(map(int,input().split()))

mod = 1000000007
val = 1
for i in a:
    val = (i+1)*val
print((val-1)%mod)
