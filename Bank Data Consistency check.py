l=[]
d = {}

def bank(a,b):
    if(a!=-1 and b!=-1):
        l.append(a)
        l.append(b)
        d[a] = b
    else:
        exit()
    return l

a,b = map(int,input().split())
val = bank(a,b)
print(val)


    
