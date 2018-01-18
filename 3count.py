n = int(input())
a = list(map(int,input().split()))

one = a.count(1)
two = a.count(2)

def func(a,b):
    if(a>b):
        count = b
        a = a-b
        count = count + a//3
    elif(b>a):
        count = a
        a  = a-co
    elif(a==b):
        count  = a

    return count    

if(one==0):
    print('0')
else:
    z = func(one,two)
    print(z)

        
            
            
        
    
