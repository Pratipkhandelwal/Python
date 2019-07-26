import math 
  
def primeFactors(n):
    arr = []
      
    while n % 2 == 0: 
        arr.append(2), 
        n = n / 2
          
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            arr.append(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        arr.append(n)

    return arr
          
# Driver Program to test above function 
t = int(input())
for _ in range(t):
    n = int(input())
    z = primeFactors(n) 
    print(int(sum(z)))
