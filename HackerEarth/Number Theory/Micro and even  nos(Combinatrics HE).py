def fact(no):
    f = 1
    for j in range(1,no+1):
        f = f*j
    return f
    
n,k = map(int,input().split())
arr = list(map(int,input().split()))
even = 0
for i in arr:
    if(i%2==0):
        even+=1

num = fact(even)
den = fact(k)
diff = fact(even-k)
print(num//(den*diff))
