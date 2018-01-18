def order(s):
    a = list()
    for i in range(0,len(s)):
      for j in range(i+1,len(s)+1):
        a.append(s[i:j])

    print(a)
    final = ''.join(map(str, sorted(a)))
    return final    

s = input()
q = int(input())
x = order(s)
print(x)
g = 0
for z in range(q):
    p,m = map(int,input().split())
    k = (p*g)% m + 1
    char = x[k-1]
    g = g + ord(char)
    print(char)
   
    
    
