n = int(input())
a = list(map(int,input().split()))
k = 0
for i in range(n):
    first = [0:i]
    second = [i:]
    if(sum(first)/len(first) > sum(second)/len(second)):
        k+=1
    print(k)
