import sys
 
mod = 10**9 + 7
max_n = 10**6
fac = [0] * (max_n + 1)
fac_inv = [0] * (max_n + 1)
 
 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
 
def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m
    
def choose(a,b,c):
    return (fac[a+b+c] * fac_inv[a] * fac_inv[b] * fac_inv[c]) % mod
 
def summation(n, m, k, d):
    sys.stdout.flush()
    rv = 0
    a = 0
    
    m_choose_2 = (m * (m-1) // 2) % mod
    total = 0
    a = -1
    
    multiplier = ( (m-1) * modinv(2*m,mod)) % mod
    term = -1
    
    while True:
        a += 1
        b = k - 2 * a
        if b < 0:
            break
        c = n - (a + b) * d
        if c < 0:
            continue
        
        if term == -1:
            term = (pow(m_choose_2, a, mod) * pow(m,b,mod)) % mod
        else:
            term = (term * multiplier) % mod
        
        temp1 = (choose(a,b,c) * term) % mod
        total = (total + temp1) % mod
    #print(n,m,k,d, "->", total)
    return total
    
def result(n, m, k, d):
    term1 = summation(n, m, k, d)
    term2 = (m * (d-1) * summation(n-d, m, k-1, d)) % mod
    term3 = (m * (m-1) * (d-1) * summation(n-d, m, k-2, d) // 2) % mod
    return (term1 + term2 + term3) % mod
        
fac[0] = 1
fac_inv[0] = 1
for i in range(1,max_n+1):
    fac[i] = (fac[i-1] * i) % mod
    fac_inv[i] = modinv(fac[i], mod)
    
num_probs = int(input())
for _ in range(num_probs):
    n, m, k, d = (int(x) for x in input().split())
    print(result(n,m,k,d))
