t = int(input())
for _ in range(t):
    n = int(input())
    x = []
    if(n==1):
        print(0)
    else:         
        for i in range(2,n+1,2):
            if(i%4!=0):
                x.append(i)
        print(len(x))
