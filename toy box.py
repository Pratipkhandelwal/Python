n,m = map(int,input().split())
d = dict()
for i in range(n):
    p,b = map(int,input().split())
    d.setdefault(b, []).append(p)
val = 0
for k,v in d.items():
    val+=max(v)
print(val)
