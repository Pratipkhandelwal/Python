import itertools

def allSubArrays(xs):
    n = len(xs)
    indices = list(range(n+1))
    for i,j in itertools.combinations(indices,2):
        yield xs[i:j]

value = (list(allSubArrays([3,5,1,2,6])))
for i in value:
    if(sum(i)>=3 and sum(i)<=12):
        print(i)
    
