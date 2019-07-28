n = int(input())
x = int(input())
for k in range(0,n):
        v = k & x
        print(v)

def dec_to_bin(y):
    return int(bin(y)[2:])

z = dec_to_bin(x)
v = str(z)
for i in range(len(v)-1 , -1 ,-1):
        if(v[i]=='1'):
           print(i)
