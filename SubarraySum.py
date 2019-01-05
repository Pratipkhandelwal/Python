import math

def SubArraySum(arr, n): 
    result = 0
    sub = []
    for i in range(0, n): 
        for j in range(i, n): 
            prev= 0
            for k in range(i, j + 1): 
                result = arr[k]
                prev +=result
            sub.append(prev)
    y = [x for x in sub if math.sqrt(x).is_integer()]        
    return len(y)  
  
# driver program
n = int(input())
arr = list(map(int,input().split())) 
print (SubArraySum(arr, n)) 
