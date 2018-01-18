n,k = map(int,input().split())
a = list(map(int,input().split()))
c=0
d=0
for i in range(0,n):
    for j in range(1,n):
        if(a[i]>a[j]):
            a[j]=a[-1]
            c+=1
        else:
             a[i]=a[-1]
             d+=1
        if(c==k):
            val = a[j]
            break
        elif(d==k):
            val = a[i]
            

print(val)            
        
