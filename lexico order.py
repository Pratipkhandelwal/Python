from collections import Counter
import re
s = input()
q = int(input())
for z in range(q):
    x = int(input())
    y = s[0:x] 
    print(len(re.findall(y,s)))
              
