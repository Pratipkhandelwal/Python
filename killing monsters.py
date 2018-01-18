n, h = input(), map(int, raw_input().strip().split())
q, data = input(), set(xrange(n))
for Q in xrange(q):
	x, y = map(int, raw_input().strip().split())
	if data:
		dead = []
		for i in data:
			if i & x == i:
				h[i] -= y
				if h[i] <= 0: dead.append(i)
		for i in dead: data.remove(i)
	print len(data) 
