from itertools import permutations 
  
perm = permutations([1, 2], 2)
v = []
for i in list(perm): 
    v.append(list(i))
print(v)

