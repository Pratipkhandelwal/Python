t = int(input())
for z in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    #h1 = h.count(max(h))
    #h2 = h.count(min(h))
    if(n==1):
        print(-1)
        continue
    counts = dict()
    for i in h:
      counts[i] = counts.get(i, 0) + 1
    arr = sorted(counts.items(), key=lambda x: x[1])
    l = len(arr)
    if(arr[l-1][1] - arr[0][1]>0):
        print(arr[l-1][1] - arr[0][1])
    else:
        print(-1)
