from itertools import permutations

a = [1,2,3,5]

perms = set()
for perm in permutations(a):
    perms.add(perm)

print(perms)
