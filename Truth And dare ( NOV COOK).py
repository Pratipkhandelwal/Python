t = int(input())
for _ in range(t):
    t1 = int(input())
    tr = list(map(int, input().split()))
    s1 = int(input())
    dr = list(map(int, input().split()))
    t2 = int(input())
    ts = list(map(int, input().split()))
    t3 = int(input())
    ds = list(map(int, input().split()))
    result1 =  all(elem in tr  for elem in ts)
    result2 =  all(elem in dr  for elem in ds)
    if(result1 and result2):
        print("yes")
    else:
        print("no")
