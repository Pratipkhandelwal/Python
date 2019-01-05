import collections

t = int(input())
for zz in range(t):        
    n,k = map(int,input().split())
    my_list = list(map(int,input().split()))
    freq = {} 
    for items in my_list: 
            freq[items] = my_list.count(items) 
    d = dict(sorted(freq.items(),reverse=True))
    a = list(d.values())
    print(sum(a[:k]))
