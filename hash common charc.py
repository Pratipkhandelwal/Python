from collections import OrderedDict
t = int(input())
for p in range(t):
    n,f = map(int,input().split())
    x = input().strip().split()
    m = "littlejhool"
    s = OrderedDict()
    for i in x:
        i = i.lower()
        y = set(i)
        set_result = set.intersection(set(i), set(m))
        s[i] = len(set_result)
    #min_key = min(s.keys().key=(lambda z: s[z]))
    v=0    
    for key, value in sorted(s.items()):
            if(v!=f):
                v+=1
                print(key,end=" ")
            else:
                break
    
            
            
        

        
                
        
        
        


