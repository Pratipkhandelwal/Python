t = int(input())
for z in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    prev = arr[0]
    flag = 0
    for i in range(1,len(arr)):
        if(arr[i] - prev <= 1 and arr[i] - prev >=0 and arr[i]<=26):
            prev = arr[i]
            continue
        else:
            print('-1')
            flag = 1
            break
    
    if(n==1):
        if(arr[0]==1):
            print("a")
        else:
            print("-1")
            
    if(flag==0 and n>1):    
        str = "abcdefghijklmnopqrstuvwxyz"
        s = "a"
        curr = arr[0]
        for i in range(1,len(arr)):
            if(arr[i] == curr):
                print("yes")
                s+= "a"
                curr = arr[i]
            else:
                s+=str[arr[i]-1]
                curr = arr[i]
        print(s)



#lexicographic order maintain
#length case is 1
        
