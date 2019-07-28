t = int(input())
for z in range(t):
    s,y = map(str,input().split())
    n = int(y)
    k = 0
    a = s.count('a')
    b = s.count('b')
    if(a<b and s[0]!='a'):
        print(0)
        continue
    else:
        prev = 0
        t = n * s
        j = 0
        flag = 0
        for i in range(0,len(s)*n):
                c = t[:i+1]
                a = c.count('a')
                b = c.count('b')
                j+=1
                if( a > b ):
                    k+=1
                    if((j+1)%len(s)==0):
                        current = k
                        if(current==prev):
                            k = k + ((len(s)*n) - (j+1))//len(s)
                            flag = 1
                            break        
                prev = k
                if(flag==1):
                    break
        print(k)
        
