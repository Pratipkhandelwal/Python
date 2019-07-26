t = int(input())
for _ in range(t):
    n = int(input())
    villain = list(map(int, input().split()))
    player = list(map(int, input().split()))
    villain.sort()
    player.sort()
    k=0
    print(villain)
    print(player)
    for i in range(0,n):
        if(player[i]>villain[i]):
            k+=1
        else:
            print("LOSE")
            break
    if(k==n):
        print("WIN")
