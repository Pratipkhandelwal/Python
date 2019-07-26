import bisect

t = int(input())
for _ in range(t):
    q = int(input())
    height = list(map(int, input().split()))
    steps = list(map(int, input().split()))
    arr = []
    k = 0
    for j in range(q):
        bisect.insort(arr,height[j])
        #print(arr)
        if((steps[j]-1) <= len(arr)-1):
            print(arr[steps[j]-1],end=" ")
        else:
           print('0',end=" ")
    print("\n")
        
