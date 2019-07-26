n, m = map(int, input().split(' '))
A = []
for _ in range(n):
    A.append(input().split(' '))

s = ''
s = A[0][0]
ptr = A[0][0]
for i in range(0,len(A)):
    for j in range(i,len(A)):
        if((i+1)<= n-1 and (j+1)<= n-1):
            if(ord(A[i][j+1]) < ord(A[i+1][j])):
                ptr = A[i][j+1]
                s+=A[i][j+1]
            else:
                s+=A[i+1][j]

s = s+A[n-1][n-1]
print(''.join(sorted(s)))
