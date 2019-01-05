def getMaxLength(input):
        return(max(map(len, input.split('0')))) 

n, q, k =  map(int,input().split())
arr = list(map(int,input().split()))
s = input()
for i in range(0,len(s)):
    if(s[i]=='?'):
        res = map(str,arr)
        rest = ''.join(res)
        #print(rest)
        val = getMaxLength(rest)
        if(val > k):
            print(k)
        else:
            print(val)
    else:
        #c = arr[-1]
        #arr = [c] + arr[0:-1]
        arr.insert(0, arr.pop())

        
        
