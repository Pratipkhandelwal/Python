t = int(input())
for i in range(t):    
    n = int(input())
    arr = list(map(int,input().split()))
    if(1 in arr):
        arr.sort(reverse=True)
        print(*arr)
    else:
        arr.sort()
        print(*arr)
