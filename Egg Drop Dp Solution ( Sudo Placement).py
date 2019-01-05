INT_MAX = 32767
  
def eggDrop(n, k): 
    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)] 
    print("initial", eggFloor)
    for i in range(1, n+1): 
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

    print("assign", eggFloor)

    for j in range(1, k+1): 
        eggFloor[1][j] = j 
    print("new_assign", eggFloor)

    for i in range(2, n+1): 
        for j in range(2, k+1): 
            eggFloor[i][j] = INT_MAX 
            for x in range(1, j+1): 
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                if res < eggFloor[i][j]: 
                    eggFloor[i][j] = res 
            print("loop", eggFloor)
    return eggFloor[n][k] 

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    print(eggDrop(n,k))
