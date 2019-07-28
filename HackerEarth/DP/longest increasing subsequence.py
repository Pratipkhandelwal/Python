def lis(arr):
	n = len(arr)

	lis = [1]*n
	val = []

	for i in range (1 , n):
		for j in range(0 , i):
			if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
				lis[i] = lis[j]+1
				val.append(arr[j])
				print(val)
                

	maximum = 0
        
	for i in range(n):
		maximum = max(maximum , lis[i])

	return maximum



arr = [50, 3, 10, 7, 40, 80]
print("Length of lis is", lis(arr))
print(lis)
