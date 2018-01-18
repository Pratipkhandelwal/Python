t=int(input())
for i in range(t):
    x,y=input().split()
    x = int(str(x)[::-1])
    y = int(str(y)[::-1])
    z=int(x)+int(y)
    k = int(str(z)[::-1])
    print(k)
