t = int(input())
for _ in range(t):
    x = int(input())
    bit = '{:032b}'.format(x)
    #print(bit)
    rev = bit[::-1]
    #print(rev)
    print(int(rev,2))
