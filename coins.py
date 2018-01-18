t = int(input())
for p in range(t):
    s  = input()
    h  = s.count('H')
    t =  s.count('T')
    k=0
    if(h>t):
        for i in s:
            if i=='T':
                k+=1
                continue
            else:
                k = 0

    print(k)       
                    
                
         
            
