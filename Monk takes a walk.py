t=int(input())
for i in range(t):
    s=input()
    sum=0
    for char in s:
       if char in "aeiouAEIOU":
        sum=sum+1
    print(sum)   
