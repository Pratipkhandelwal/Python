t = int(input())
for _ in range(t):
    p,q = map(int,input().split())
    val = max(p,q)
    k=0
    if(val==1):
        print("Jeel")
    else:
        while(val!=1):
            val=val//2
            k +=1
        print(k)
        if(k%2==0):
            print("Jeel")
        else:
            print("Ashish")
