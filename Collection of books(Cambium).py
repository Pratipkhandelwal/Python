t = int(input()) #Total Testcases
for _ in range(t):
            temp = [int(x) for x in input().split()]
            N, I, Q = temp[0], temp[1], temp[2]
            nArr = [int(x) for x in input().split()]
            for _ in range(Q):
                M = int(input())
                k = 0
                value = 0
                for i in range(I-1,N):
                    value+=nArr[i]
                    if(value <= M):
                        k+=1
                    else:
                        break
                if(k==0):
                    print(-1)
                else:
                    print(k+(N-I-1),value)


