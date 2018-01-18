from collections import defaultdict
from collections import OrderedDict
val = OrderedDict()
val = {3000:6, 600:6, 4:2}
a=sorted(val)
b=defaultdict(list)
for i in a:
    for k,v in val.items():
        if(i==k):
            b[v].append(i)    

print("{",end="")
for k,v in b.items():
    print("%s: %s ," % (k,v), end="")

print("}")
