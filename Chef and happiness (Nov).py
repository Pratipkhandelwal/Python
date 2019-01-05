t = int(input())
for z in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(0,len(a)-1):
        for j in range(1,len(a)):
            if(a[a[i]-1] == a[a[j]-1] and a[i]!=a[j]):
                print("match")
                print(a[i],a[j])
                flag = 1
                break
            else:
                flag = 0
                
        if(flag==1):
            print("Truly Happy")
            break
        else:
            continue

    if(flag==0):
        print("Poor Chef")
