n,m,g = map(int,input().split())
t = list(map(int,input().split()))
a = list(map(int,input().split()))


diff = []
diff.append(t[0])

g = 0
count  = 0
for i in range(0,len(t)-1):
    diff.append(t[i+1]-t[i])


for j in range(0,len(diff)):
    if(a[j]<=diff[j]):
        g+=1
        count+=1


print(count)
        

        
            
