n = int(input())
arr = list(map(int,input().split()))
k = ''
p = []
a = min(arr[0],arr[-1])
b = max(arr[0],arr[-1])
p.append(a)
if(p[-1]==arr[0]):
    k+='L'
else:
    k+='R'
arr.remove(a)
while(len(arr)>1):
    left = arr[0]
    right = arr[-1]
    small = min(left,right)
    big = max(left,right)
    if(small > p[-1]):
        if(small==left):
            k+='L'
        else:
            k+='R'
        p.append(small)
        arr.remove(small)
    else:
        if(big==left):
            k+='L'
        else:
            k+='R'
        p.append(big)
        arr.remove(big)

if(arr[-1] > p[-1]):
    p.append(arr[-1])
    k+='R'
    print(len(p))
    print(k)
else:
    print(len(p))
    print(k)
