def powerset(s):
     x = len(s)
     part = []
     for i in range(1 << x):
         part.append([s[j] for j in range(x) if (i & (1 << j))])
     return part

value = powerset([3,2,1,5,6])
new_val = []
for i in value:
    if(sum(i)>=3 and sum(i)<=12):
        print(i)
        new_val.append(sum(i))

print(set(new_val))




import itertools

def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller


something = [3,5,1,2,6]

l = []
for n, p in enumerate(partition(something), 1):
    for i in sorted(p):
        if(sum(i)>=3 and sum(i)<=12):
            l.append(sorted(p))
                     

l.sort()
#print(list(l for l,_ in itertools.groupby(l)))

