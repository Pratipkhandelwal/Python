import math

def SubArraySum(arr, n): 
    result = 0
    sub = []
    prev=0
    for i in range(0, n): 
            result = sum(arr[i:])
            sub.append(result)
    print(sub)
    y = [x for x in sub if math.sqrt(x).is_integer()]        
    return len(y)  
  
# driver program
n = int(input())
arr = list(map(int,input().split())) 
print (SubArraySum(arr, n)) 
