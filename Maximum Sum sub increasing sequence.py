def maxsumis(arr,n):

    maxx = 0
    msis = [0 for x in range(n)]
    
    for i in range(n):
        msis[i] = arr[i]

    for i in range(1,n):
        for j in range(i):
            if (arr[i] > arr[j] and msis[i] < msis[j] + arr[i]):
                msis[i] = msis[j] + arr[i]

    l = msis
    print(max(msis))

arr = [1, 101, 2, 3, 100, 4, 5] 
n = len(arr) 
print("Sum of maximum sum increasing " + 
                     "subsequence is " +
                  str(maxsumis(arr, n))) 

    
