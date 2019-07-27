L = [3,5,1,2,6]
print([L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)])
