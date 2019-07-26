def gcd(a,b):
    if(b==0):
        return a
    return gcd(b, a%b)

a = int(input())
for b in range(a-2,0,-1):
    value = gcd(a,b)
    if(value==1):
       print(b)
       break
