import collections

t = int(input())
for i in range(t):
    s = input()
    lcounts = sorted([(i, s.count(i)) for i in set(s)], key=lambda x: x[1])
    print(lcounts)
    count = max(lcounts, key=lambda x: x[1])[1]
    print(counts)
    val = dict(filter(lambda x: x[1] == count, lcounts))
    for key in sorted(val):
        print(key)
        
