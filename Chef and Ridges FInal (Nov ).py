import math
a = list(map(int,input().split()))
box = a[1:]
b = list()
x = 1
y = 2
count = 2
b.append(x)
b.append(y)
for i in range(2,26):
    next_x = (y-x)
    next_y = int(math.pow(2,count))
    b.append(next_x)
    b.append(next_y)
    x = next_x
    y = next_y
    count+=1
print(*b)
