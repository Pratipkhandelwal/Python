t = int(input())
A = []
for _ in range(3):
        A.append(list(map(int, input().split())))
value = A[0][1] + A[1][0] + A[1][2] + A[2][1] - A[1][1]
print(value)
