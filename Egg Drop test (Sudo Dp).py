t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    
def eggDrop(n,k):
    if(k==1 or k==0):
        return k
    
    if(n==1):
        return k
    
    min = 9999
    
    for x in range(1,k+1):
        res = max(eggDrop(n-1, x-1) ,eggDrop(n, k-x))
        if(res < min):
            min = res
            
        
    return min+1


t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    print(eggDrop(n,k))
