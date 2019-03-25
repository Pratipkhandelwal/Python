t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    val = 0
    l = []
    for i in range(0,n-1):
        val+=abs(a[i]-a[i+1])
        l.append(abs(a[i]-a[i+1]))
    a.pop(l.index(max(l))+1)
    val=0
    if(len(a)>2):        
        for j in range(0,len(a)-1):
            val+=abs(a[j]-a[j+1])
        print(val)
    else:
        print(min(a))

    
