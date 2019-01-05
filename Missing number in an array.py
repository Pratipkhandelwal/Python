t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = [i for i in range(1,n+1)]
    print(b)
    diff = list(set(b)-set(a))
    print(*diff)
