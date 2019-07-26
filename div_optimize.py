t = int(input())
for z in range(t):
    n = int(input())
    if(n==2):
        print("NO")
    elif(n==3):
        print("YES")
    else:
        if((n+1)%2!=0):
            print("NO")
        else:
            print("YES")
