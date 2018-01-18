s = input()
a = list()
for i in range(0,len(s)):
      for j in range(i+1,len(s)+1):
        a.append(s[i:j])

print(a)
print(sorted(a))

my = ''.join(map(str, sorted(a)))
print(my)   
for z in range(q):
    p,m = map(int,input().split())
     
