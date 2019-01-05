from itertools import combinations_with_replacement 
import itertools

# Get all combinations of [1, 2, 3] and length 2 
comb = combinations_with_replacement([2,4,3], 3) 
  
for i in list(comb): 
    print(i,',',end="") 

pro = list(itertools.product([2,3,4], repeat=3))
print(pro)
