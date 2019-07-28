n=int(input())
num=list(map(int,input().split()))
num.sort()
max=num[0]*num[1]
min=num[n-1]*num[n-2]
if(max > min):
   print(max)
else:
    print(min)

s = input()
for i in s:
    print(s,end=" ")
        
