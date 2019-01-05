t = int(input())
for z in range(t):
    n,k = map(int,input().split())
    s = 0
    for i in range(1,n+1):
        s+=i

    print("initial sum",s)
    if(s>=k):
        print(s-k)
        continue

    initial = s  
    if(s<k):
        while(s<k):
            s+=initial
            print("s after add",s)
            if(s>=k):
                print(s-k)
                break
            else:
                continue
        
