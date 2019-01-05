from itertools import accumulate
n = int(input())
a = [0] + list(accumulate(map(int, input().split())))
s = [0]
i = 1
r = -10 ** 15
print(a)
while s[-1] < n:
    s.append(s[-1] + i)
    i += 1
    print(s)
for i in range(n):
    while i + s[-1] > n:
        s.pop()
    print("after s",s)
    r = max(r, a[i + s[-1]] - a[i])
print(r)
