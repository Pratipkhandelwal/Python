def cnt (A, X, R, L):
    # Write your code here
    gap = A[L-1:R]
    c=0
    print(gap)
    for i in gap:
        if(X%i==0):
            c+=1
    print(c)

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = list(map(int, input().split()))
R = list(map(int, input().split()))
X = list(map(int, input().split()))

for j in range(0,Q):
    out_ = cnt(A, X[j], R[j], L[j])
#print (' '.join(map(str, out_)))
