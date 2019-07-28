x = input()
l = len(x)
k=0
if(l%2==0):
    y = set(x)
    for i in y:
        val = x.count(i)
        if(val%2==0):
            flag=1
            continue
        else:
            print('NO')
            flag=0
            break
    if(flag==1):
        print('YES')

else:
    y = set(x)
    a = list()
    even=0
    odd=0
    for i in y:
        val = x.count(i)
        if(val%2==0):
            even+=1
        else:
            odd+=1
    if(odd==1):
        print('YES')
    else:
        print('NO')
    
