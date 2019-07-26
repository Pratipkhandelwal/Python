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


something = [3,4,2]

l = []
for n, p in enumerate(partition(something), 1):
    k = 0
    for i in range(0,len(p)):
        if(sum(p[i])>=3 and sum(p[i])<=12):
            k+=1
        if(k==len(p)):
            l.append(sorted(p))


print(l)
        
        
