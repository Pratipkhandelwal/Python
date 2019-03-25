import math
n=int(input())
arr=list(map(int,input().split()))
minans=999999999999999
print("i","j","ans")
for i in arr:
    ans=0
    for j in arr:
        #ans=ans+min(abs(i-j),j)
        #ans=ans+min(abs(i-j),j)
        ans= ans + min(abs(i-j),j)
        print(i,j,ans)
    if ans<minans:
        minans=ans
        print("minans:",minans)
print(minans)
