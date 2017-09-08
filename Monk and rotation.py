from collections import deque
def rotate(lst, x):
 d = deque(lst)
 d.rotate(x)
 lst[:] = d
 t = int(input())
 for _ in range(t) :
  n,k = input().split()
  n = int(n)
  k = int(k)
  l = list(map(int,input().split()))
 for i in range(n) :
  l[i] = int(l[i])
  rotate (l,k)
  print (*l)
