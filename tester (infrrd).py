n,m,k = map(int, input().split())
A = []
for _ in range(n):
    A.append(input().split())

arr = []
brr = []
for i in range(0,n):
    count = A[i].count('0')
    if(k - count >=0):
        arr.append(A[i])

for i in range(0,len(arr)):
    val = arr.count(arr[i])
    brr.append(val)
print(max(brr))
