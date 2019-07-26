p,q = map(int,input().split())

A = []
for _ in range(p):
        A.append(list(map(int, input().split())))


x,y = map(int,input().split())
B = []
for _ in range(x):
        B.append(list(map(int, input().split())))

result = [[sum(a * b for a, b in zip(A_row, B_col))  
                        for B_col in zip(*B)] 
                                for A_row in A] 
  
res = [sum(e) for e in result]

col = [sum([row[i] for row in result]) for i in range(0,len(result[0]))]

g = max(res)
h = max(col)

print(max(g,h))
