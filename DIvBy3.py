def canConstruct(a):
    results= ''
    for element in a:
        results += str(element)
    num = int(results)
    s = 0
    #print(num)
    while(num):
        s += num%10
        num //=10
    if(s%3==0):
        return("Yes")
    else:
        return("No")


a = list(map(int, input().rstrip().split()))
sy = canConstruct(a)
print(sy)
