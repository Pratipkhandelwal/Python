n = int(input())
page = []
for i in range(n):
    l,r = map(int,input().split())
    page.append([l,r])
k = int(input())
index = 0
flag = 0
for i in page:
    index+=1
    for j in range(i[0],i[-1]+1):
        if(k==j):
            flag=index
            break
            
print(n-flag+1)
