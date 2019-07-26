k = int(input())
s = input()
counting = 0
part = 0
for i in range(1,len(s)):
    first = s[0:i]
    second = s[i:]
    freq = list(set(first))
    counting = 0
    
    if(len(freq)>=k):
        for i in freq:
            count1 = first.count(i)
            count2  = second.count(i)
            if(count1==count2):
                counting+=1
        if(counting>=k):
            part+=1
        print(first,second,counting,part)
    else:
        continue

print(part)
    
