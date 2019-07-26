import sys 
def findNumberOfTimes(str1, str2): 	
	freq = [0] * 26
	l1 = len(str1) 
	
	for i in range(l1): 
		freq[ord(str1[i]) - ord("a")] += 1
	l2 = len(str2) 
	count = sys.maxsize 
	
	for i in range(l2): 
		count = min(count, freq[ord(str2[i]) - ord('a')])
								 
	return count 
	
t = int(input())
for z in range(t):
    n = int(input())
    str1=''
    for z in range(n):
        z = input()
        str1 = str1 + ''.join(z) 
        str2 = "codechef"
    print(str1)
    print(findNumberOfTimes(str1, str2)) 
