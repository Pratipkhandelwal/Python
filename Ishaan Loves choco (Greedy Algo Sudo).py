t = int(input())
for z in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    while(len(arr)!=1):
        if(arr[0] < arr[-1]):
            arr.pop(-1)
        else:
            arr.pop(0)
    print(*arr)
