import math 

def printSubsequences(arr, n) : 

    opsize = math.pow(2, n)
    summ= 0
    mod = 1000000007  
    for counter in range( 1, (int)(opsize)) :
        r = list()
        for j in range(0, n) : 
			 
            if (counter & (1<<j)) :
                r.append(arr[j])
                
        r.sort(reverse=True)
        if(len(r)==1):
            summ+=1
        elif(len(r)==2):
            even = sum(r) / 2
            if(even in r):
                summ+=1
        elif(len(r)%2==0):
            first = r[(len(r)//2)-1]
            sec = r[(len(r)//2)]
            evens = (first + sec) / 2
            if (evens in r):
                summ+=1
        elif(len(r)%2!=0):
            summ+=1

    return(summ%mod)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(printSubsequences(arr,n))
