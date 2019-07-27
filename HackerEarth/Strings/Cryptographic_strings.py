from itertools import cycle
z=range
y=input
x=int
w=len
 
def de(i, u):
    r = list(z(u))
    print(r)
    p = cycle(r + r[-2:0:-1])
    print(p)
    f = sorted(z(w(i)), key=lambda i: next(p))
    print(f)
    e = [''] * w(i)
    print(e)
    for i, c in zip(f, i):
        e[i] = c
    print(''.join(e))
 
for _ in z(x(y())):
    a,b=y().split()
    a=x(a)
    de(b,a)
