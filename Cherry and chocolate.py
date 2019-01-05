t = int(input())
for z in range(t):
    n = int(input())
    arr = [list(map(str, input().split())) for i in range(n)]
    s = 0
    val = []
    print(arr)
    for i in range(0,len(arr)):
        brr = ''.join(arr[i])
        l = list(brr)
        s+=l.count('#')
        val.append(l.count('#'))
    print(val)
    if(s%2!=0):
        print("No")
        continue
    else:
        first = 0
        for i in range(0,len(val)-1):
            first+=val[i]
            sec = sum(val[i+1:])
            third = first
            print(third,sec,first)
            if(first==sec):
                   flag=0
                   print("YES")
                   break
            else:
                flag = 1
                continue
        if(flag==1):
            print("NO")

