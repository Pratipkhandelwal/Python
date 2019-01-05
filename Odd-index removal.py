# just pass the case if len list is null to print zero 

n = int(input())
a = list(map(int,input().split()))
l = n
while(l!=1):
    del a[0::2]
    l = len(a)
print(*a)
    
