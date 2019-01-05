def countEvenSum(arr, n):

# A temporary array of size 2. temp[0] is
# going to store count of even subarrays
# and temp[1] count of odd.
# temp[0] is initialized as 1 because there
# a single even element is also counted as
# a subarray
    temp = [1, 0]
    
    # Initialize count. sum is sum of elements
    # under modulo 2 and ending with arr[i].
    result = 0
    sum = 0
    
    # i’th iteration computes sum of arr[0..i]
    # under modulo 2 and increments even/odd
    # count according to sum’s value
    for i in range( n):
    
    # 2 is added to handle negative numbers
        sum = ( (sum + arr[i]) % 2 + 2) % 2
        temp[sum]+= 1
    
    result = result + (temp[0] * (temp[0] – 1)//2)
    result = result + (temp[1] * (temp[1] – 1)//2)
    
    return (result)
    
    
# driver code 
n = int(input())
l1 = list(map(int,input().split()))
print(countEvenSum(l1,len(l1)))
