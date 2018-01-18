x=int(input())
a=[int(r) for r in input().split()]
p=[]
     
for i in a:
    if i not in p:
        p.append(i)
     
p.sort()
r=p[0]
for j in range(len(p)):
        if(a.count(p[j])>a.count(r)):
            r=p[j]
print(r)
