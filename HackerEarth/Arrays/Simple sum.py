n = int(input())
a = list(map(int,input().split()))
val = 0
for i in range(0,n):
    for j in range(i,n):
        m = max(a[i:j+1])
        mul = (a[i]|a[j])
        val = val + m * mul
 
print(val)        
