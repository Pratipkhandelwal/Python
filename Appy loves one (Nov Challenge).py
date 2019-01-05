def getMaxLength(arr, n): 

	# intitialize count 
	count = 0
	
	# initialize max 
	result = 0

	for i in range(0, n): 
	
		# Reset count when 0 is found 
		if (arr[i] == 0): 
			count = 0

		# If 1 is found, increment count 
		# and update result if count 
		# becomes more. 
		else: 
			
			# increase count 
			count+= 1
			result = max(result, count) 
		
	return result  


n, q, k =  map(int,input().split())
arr = list(map(int,input().split()))
s = input()
for i in range(0,len(s)):
    if(s[i]=='?'):
        val = getMaxLength(arr, n)
        if(val > k):
            print(k)
        else:
            print(val)
    else:
        b = list()
        b.append(arr[-1])
        b.extend(arr[0:-1])
        arr = b
        #print(b)
        
        
