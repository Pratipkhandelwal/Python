d = int(input())
a = list(map(int,input().split()))
max_occur = {}
val = 0
for i in range(0,len(a)):
    value = str(a[i]).count(str(d))
    max_occur[i] = value
    if(val < value):
        val = value
        idx = i
print(a[idx])
