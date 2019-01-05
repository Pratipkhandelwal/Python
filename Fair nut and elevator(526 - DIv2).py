n = int(input())
a = list(map(int,input().split()))

x = a.index(max(a))
s = 0
for i in range(0,len(a)):
    if(x>i):
        s += a[i] * abs(x-i)*2
    elif(x==i):
        s += a[i] * (abs(x)*2 *2)
    elif(x<i):
        s += a[i] * (abs(x-i)*2 + abs(x)*2)*2
print(s)
