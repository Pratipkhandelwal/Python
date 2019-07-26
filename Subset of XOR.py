import math 

def subsetXOR(arr, n, k): 
	
 
	max_ele = arr[0] 
	for i in range(1, n): 
		if arr[i] > max_ele : 
			max_ele = arr[i] 
			
	m = (1 << (int)(math.log2(max_ele) + 1)) - 1
	
	 
	dp = [[0 for i in range(m + 1)] 
			for i in range(n + 1)] 
	
	dp[0][0] = 1

	for i in range(1, n + 1): 
		for j in range(m + 1): 
			dp[i][j] = (dp[i - 1][j] +
						dp[i - 1][j ^ arr[i - 1]]) 

	
	return dp[n][k] 

T = int(input())
for _ in range(T):
    N = int(input())
    k = int(input())
    A = list(map(int, input().split(' ')))
    cnt1 = []
    cnt2 = []
    cnt3 = []
    n = len(A)
    for i in range(0,k+1):
        val = subsetXOR(A, n, i)
        if(val < k):
            cnt1.append(val)
        elif(val == k):
            cnt2.append(val)
        else:
            cnt3.append(val)
            
    a = sum(cnt1)
    b = sum(cnt2)
    c = sum(cnt3)
    print(a,b,c)
    final = ((a+b) * (a+b)) + ((b+c) * (b+c)) + ((c+a) * (c+a)) - (a*a + b*b + c*c)
    print(final)
    
