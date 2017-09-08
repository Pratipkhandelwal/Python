n=int(input())
a = list(map(int,input().split(' ')))
num=0
for i in a[:]:
    jump=num+i
    print(jump)
    if(jump>n):
        break
    num+=1

print(num+1)

    

    
    
