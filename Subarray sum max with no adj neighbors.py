def find_max_sum(arr): 
	incl = 0
	excl = 0
	
	for i in arr: 
		
		# Current max excluding i (No ternary in 
		# Python) 
		new_excl = excl if excl>incl else incl 
		
		# Current max including i 
		incl = excl + i
		print("incl is:",incl)
		excl = new_excl
		print("excl is:",excl)
                
	# return max of incl and excl 
	return (excl if excl>incl else incl) 

# Driver program to test above function 
arr = [4 ,5 ,4 ,3] 
print(find_max_sum(arr))
