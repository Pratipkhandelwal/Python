def isSubsetSum (arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
 
    # If last element is greater than sum, then 
    # ignore it
    if arr[n-1] > sum:
        return isSubsetSum (arr, n-1, sum)
 
    ''' else, check if sum can be obtained by any of 
    the following
    (a) including the last element
    (b) excluding the last element'''
     
    return isSubsetSum (arr, n-1, sum) or isSubsetSum (arr, n-1, sum-arr[n-1])
 
def findPartion (arr, n):
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    if sum % 2 != 0:
        return false
 
    return isSubsetSum (arr, n, sum // 2)
 
# Driver program to test above function
arr = [1,2,3,4,5,6,7]
n = len(arr)
if findPartion(arr, n) == True:
    print ("Can be divided into two subsets of equal sum")
else:
    print ("Can not be divided into two subsets of equal sum")
     
