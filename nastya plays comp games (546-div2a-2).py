n,k = map(int,input().split())
if(k==1):
    print(n*(n+1)//2)
else:
    print(n*(n+1)//2 + k*(k+1)//2)
