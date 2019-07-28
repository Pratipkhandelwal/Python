for T in xrange(input()):
	x, n = map(int, raw_input().strip().split())
	if n < 4: print 'impossible'
	elif x == 2 and n >= 7 and ((n-7) % 4 == 0):
		data = ['2']*n
		data[1-1], data[3-1], data[4-1], data[5-1] = '0', '0', '0', '0'
		data[6-1], data[7-1] = '1', '1'
		a, b = 0, 0
		for i in xrange(n, 7, -1):
			if a <= b:
				data[i-1] = '0'
				a += i
			else:
				data[i-1] = '1'
				b += i
		print 'impossible' if a != b else ''.join(data)
	else:
		s = n*(n+1) / 2 - x
		if s % 2 != 0: print 'impossible'
		else:
			if x != 1:
				arr, data = list(xrange(1, n+1)), ['2']*n
				arr.remove(x)
				a, b = 0, 0
				for i in reversed(arr):
					if a <= b:
						data[i-1] = '0'
						a += i
					else:
						data[i-1] = '1'
						b += i
				print 'impossible' if a != b else ''.join(data)
			else:
				if (n-1) % 2 == 0:
					arr, data = list(xrange(1, n+1)), ['2']*n
					arr.remove(x)
					a, b = 0, 0
					for i in reversed(arr):
						if a <= b:
							data[i-1] = '0'
							a += i
						else:
							data[i-1] = '1'
							b += i
					print 'impossible' if a != b else ''.join(data)
				else:
					data = ['2']*n
					data[2-1], data[3-1], data[5-1] = '0', '0', '0'
					data[4-1], data[6-1] = '1', '1'
					a, b = 0, 0
					for i in xrange(n, 6, -1):
						if a <= b:
							data[i-1] = '0'
							a += i
						else:
							data[i-1] = '1'
							b += i
					print 'impossible' if a != b else ''.join(data) 
