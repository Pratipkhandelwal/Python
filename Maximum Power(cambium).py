t = int(input())
for _ in range(t):
    arr = []
    q = int(input())
    for _ in range(q):
        x,y = map(str,input().split())
        if(x=='A'):
            arr.append(int(y))
        if(x=='I'):
            arr = [z+int(y) for z in arr]
        if(x=='D'):
            arr = [z-int(y) for z in arr]
        if(x=='P' and len(arr)<=int(y)):
            arr.sort(reverse=True)
            print(arr[int(y)-1])
        else:
            print(-1)

        
        
