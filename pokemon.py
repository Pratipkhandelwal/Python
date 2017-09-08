t,n=map(int,input().split())
count =0
l=dict()
c=0
for p in range(t):
    k=int(input())
    for x,y in l.items():
        val=l.get(k)
        if y < val:
            c+=1
    print(c)        
        
    
            
            
            
            
            
        
        
     
