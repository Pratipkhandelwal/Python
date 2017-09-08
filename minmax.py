n=int(input())
numbers = [int(n) for n in input().split()]
min=0
max=0
z=sorted(numbers)
print(z)
for i in z:
    max=sum(z[1:n])
    min=sum(z[:n-1])
print(min,max)    
