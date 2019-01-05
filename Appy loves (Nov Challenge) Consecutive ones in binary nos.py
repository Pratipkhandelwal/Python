def getMaxLength(z):
        ans = 0    
        while z>0 :
            z &= (z<<1)
            ans += 1
            
        return ans  


n, q, k =  map(int,input().split())
arr = list(map(int,input().split()))
s = input()
for i in range(0,len(s)):
    if(s[i]=='?'):
        res = map(str,arr)
        rest = ''.join(res)
        print(rest)
        val = getMaxLength(int(rest))
        if(val > k):
            print(k)
        else:
            print(val)
    else:
        b = list()
        b.append(arr[-1])
        b.extend(arr[0:-1])
        arr = b
        #print(b)
        
        
