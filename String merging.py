def clean(s):
	ans = [s[0]]
	for i in xrange(1, len(s)):
		if s[i] != ans[-1]:
			ans.append(s[i])
	return ans
 
def lcsq(a, b, n, m):
	dp = [[0]*(m+1) for N in xrange(n+1)]
	for i in xrange(1, n+1):
		for j in xrange(1, m+1):
			if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1] + 1
			else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return dp[n][m]
 
for T in xrange(input()):
	n, m = map(int, raw_input().strip().split())
	a, b = clean(raw_input().strip()), clean(raw_input().strip())
	n, m = len(a), len(b)
	print n + m - lcsq(a, b, n, m)
