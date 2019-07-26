def palindromeNumbers(list_a): 

            c = 0
            p = list()
            for i in list_a:			 

                    # Find reverse of current number 
                    t = i 
                    rev = 0
                    while t > 0: 
                            rev = rev * 10 + t % 10
                            t = t / 10

                    # compare rev with the current number 
                    if rev == i: 
                            p.append(i), 
                            c = c + 1

            
            return len(p)
	
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))
    brr = []
    for i in arr:
        if(int(i) > 1 ):
            if(int(i)<10):
                brr.append(i)
            if(len(list(set(i))>1)):
                brr.append(i)
    print(brr)    
    print(palindromeNumbers(brr))
	
