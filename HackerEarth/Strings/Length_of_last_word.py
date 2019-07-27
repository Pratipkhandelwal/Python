s = input()
c = 0
for i in range(0,len(s)):
    if(s[i] != ' '):
        c +=1
    if(s[i]== ' '):
        c = 0
           
print(c)        
