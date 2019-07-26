t = int(input())
for j in range(0,t):
    n,m = map(int,input().split())
    small = min(n,m)
    big = max(n,m)
    if(big%small == 0):
        print("Ari")
    else:
        k = 0
        while(small!=0 and big!=0):
            div = big % small
            big = small
            small = div
            k+=1
        if(k%2==0):
            print("Rich")
        else:
            print("Ari")
            
            
