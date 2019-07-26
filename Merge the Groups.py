n = int(input())
data_list = list(map(int,input().split()))
arr = [data_list[i:i+1] for i in range(0, len(data_list), 1)]
#print(arr)
q = int(input())
for z in range(q):
    type = list(map(int,input().split()))
    if(len(type)==3):
        x = type[1]
        y = type[2]
        first = arr[x-1]
        sec  = arr[y-1]
        merge = first+sec
        arr[x-1] = merge
        arr[y-1] = merge
        #print(arr)
    else:
        X = type[1]
        #print("X is",X)
        if(len(arr[X-1])==1):
           print(0)
        else:
            mini = min(arr[X-1])
            maxi = max(arr[X-1])
            print(abs(maxi-mini))
           
    
