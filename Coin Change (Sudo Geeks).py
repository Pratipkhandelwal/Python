def count(S, m, n): 
    # We need n+1 rows as the table is constructed  
    # in bottom up manner using the base case 0 value 
    # case (n = 0) 
    table = [[0 for x in range(m)] for x in range(n+1)] 
    print(table)  
    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1
    print(table)  

    # Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): 
        for j in range(m): 
  
            # Count of solutions including S[j] 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
  
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
  
            # total count 
            table[i][j] = x + y
            print(table)  
  
    return table[n][m-1] 
  
# Driver program to test above function 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    print(count(arr,n,m)) 