t=int(input())
for p in range(t):
    s=input().strip();
    count=0
    flag=0
    for i in range(len(s)):
        if s[i]=='1':
            if flag==0:
                count+=1
                if count>2:
                    break
            flag=1
            
        else:
            flag=0
    if count==1:
        print ("YES")
    else:
        print ("NO")
