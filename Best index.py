n = int(input())
arr = [0]
arr.extend(map(int, input().strip().split()))
print(arr)
for i in range(n):
    arr[i + 1] += arr[i]
print(arr)
x = 0
y = 1
ans = arr[-1] - arr[-2]
print(ans)
for i in range(n - 1, -1, -1):
    if x + y + i <= n:
        x += y
        y += 1
        print("value of x and y",x,y,i)
    ans = max(arr[i + x] - arr[i], ans)
    print("arr is ",arr[i + x],arr[i])
    
print (ans)

