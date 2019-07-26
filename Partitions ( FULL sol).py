n, l, r = (int(x) for x in input().split())
A = [int(x) for x in input().split()]
 
mod = 1000000007
count = [0] * (n+1)
 
count[n] = 1
 
for start in range(n-1,-1,-1):
    current_sum = 0
    total = 0
    for end in range(start,n):
        current_sum += A[end]
        print(current_sum)
        if current_sum > r:
            break
        if current_sum >= l:
            total = (total + count[end+1]) % mod
            print("total is",total)
    count[start] = total
print(count[0])
