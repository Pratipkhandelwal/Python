t = int(input())
for z in range(t):
    n = input()
    d = {'0':6, '1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
    s = 0
    for i in range(len(n)):
        s=s+d[n[i]]
    if s % 2 == 0:
        print('1' * (s // 2))
    else:    
        print('7' + '1' * ((s - 3) // 2))
