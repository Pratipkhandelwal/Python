from math import sqrt
 
def check(x):
	s = int(sqrt(x))
	return (x == s*s)
 
def pre():
	sieve, pr = [False]*26000001, []
	for i in xrange(2, 26000001):
		if not sieve[i] and check(i):
			j = i
			while j < 26000001:
				sieve[j] = True
				j += i
	for i in xrange(26000001):
		if sieve[i]: pr.append(i)
	return pr
 
n, ans = input(), pre()
print ans[n-1] 
