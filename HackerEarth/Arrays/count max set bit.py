def dec_to_bin(n):
    return int(bin(n)[2:])

t = int(input())
for z in range(t):
     n = int(input())
     s = [ int(input()) for i in range(n)]
     print(s)
     bit = "00000000000000000000000000000000"
     for i in range(0,n):
             z = dec_to_bin(s[i])
             print(z)
             v = str(z).index('1')
             bit  = bit.replace(bit[v], bit[v] + 1)
             print(z)

     print(bit)        
     
