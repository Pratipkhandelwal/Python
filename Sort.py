t = int(input())
for z in range(t):
    s = input()
    c = []
    d = []
    for i in s:
        if i.isalpha():
            c.append(i)
        else:
            d.append(i)
    d.sort();c.sort()
    ans = ''
    k = j = 0
    for i in s:
        if i.isalpha():ans += c[k];k+=1
        else:ans += d[j];j+=1
    print(ans)
