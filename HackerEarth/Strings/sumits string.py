t = int(input())
for j in range(t):
    s = input()
    l = len(s)
    flag = 0
    for i in range(0,l-1):
        for j in range(1,l):
            if(s[i]==s[j]):
                val = j-i
                if(val==1):
                   flag=1

    if(flag==1):
         print('NO')
    else:
         print('YES')
         
          
                

            
