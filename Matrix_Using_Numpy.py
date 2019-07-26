import numpy as np
r=lambda:list(map(int,input().split()))
print(r)
a,b=r()
A=[r()for _ in range(a)]
print(A)
a,b=r()
B=[r()for _ in range(a)]
print(B)
m=np.matmul(A,B)
print(max(max(np.sum(m,0)), max(np.sum(m,1))))
