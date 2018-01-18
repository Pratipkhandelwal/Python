n = int(input())
for p in range(n):
    a = input().strip().split()
    b = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fin = 0
    for j in a:
        c = len(j)
        pro=0
        for i in range(0,c):
            val = i+b.index(j[i])
            pro = pro+val
        fin = fin+pro    
    end = len(a)*fin
    print(end)
