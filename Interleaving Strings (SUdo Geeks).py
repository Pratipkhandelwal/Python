def isLeave(a,b,c):
    if a in c and b in c:
        return True
    else:
        return False
    


if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        arr = input().strip().split()
        if isLeave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)


