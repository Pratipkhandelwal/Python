def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

s = input()
q = int(input())
for z in range(q):
    x = int(input())
    y = s[0:x]
    a = occurrences(s,y)
    print(a)
    
