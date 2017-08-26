import math
counts = dict()
print('Enter a line of text :')
line = (input())

words = line.split()

print('Words:',words)

print('Coutning...')
for word in words:
    counts[word] = counts.get(word,0)+1
print('Counts', counts)
sum=0
z=int(input())
for k,v in counts.items():
    sum=sum+int(math.floor(int(k)/z)*v);
print(sum)    
