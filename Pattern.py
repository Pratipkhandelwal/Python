s=""
x = "Sentience2K19."
y = "Sentience."
z = "2K19."
for i in range(1,101):
    if(i%3==0 and i%5==0):
        s+=x
    elif(i%3==0):
        s+=y
    elif(i%5==0):
        s+=z
    else:
        s+=str(i)+'.'
print(s[:-1])
        
        
