t = int(input())
for _ in range(t):
    n = int(input())
    if(n==0):
        print(0)
        continue
    b = str(bin(n))[2:]
    #print(b)
    c = b[::-1]
    #print(c)
    k = 1
    for i in c:
        if(i=='1'):
            print(k)
            break
        k+=1
            
