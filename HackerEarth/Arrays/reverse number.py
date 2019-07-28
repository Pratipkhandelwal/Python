def rev(n):
    num = n
    m=0
    while(num>0):
        r = num%10
        m = m*10 + r
        num=num//10
    return m


t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    temp = rev(a)+rev(b)
    ans = rev(temp)
    print(ans)
    
