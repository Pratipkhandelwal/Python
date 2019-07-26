n,m,g = map(int,input().split())
t = list(map(int,input().split()))
a = list(map(int,input().split()))


diff = []
diff.append(t[0])

g = 0
count  = 0
for i in range(0,len(t)-1):
    diff.append(t[i+1]-t[i])

maxim = max(diff)

print(maxim)

days = [i for i in a if i <= maxim]
print(days)
print(len(days))

#yeah, it all makes sense now. hey y'all "we are now at $t_1$ second and it's raining", this sentence makes a huge difference.




        
            
