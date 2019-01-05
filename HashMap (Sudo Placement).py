t = int(input())
for z in range(t):
    n = int(input())
    s = [x for x in input().split()]
    dict = {}
    for i in set(s):
    	dict[i] = s.count(i)
    maxima = max(dict.values())

    new_list = []
    for k,v in dict.items():
    	if maxima ==v:
    		new_list.append(k)
    new_list.sort()
    print('{} {}'.format(new_list[0],maxima))
