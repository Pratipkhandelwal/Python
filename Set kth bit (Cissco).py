t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    binar = bin(n)[2:]
    binary = binar[::-1]
    if(binary[k]=='0'):
        binary = binary[:k] + '1' + binary[k+1:]
        print(int(binary[::-1],2))
    else:
        print(n)
    
