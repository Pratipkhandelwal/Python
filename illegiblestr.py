n=int(input())
str=input()
l=len(str)
x=0
y=0
for i in str:
    if i=='v':
        x+=1
    elif i=='w':
        y+=1
    
print(((int((2*y+x)/2))+(l-(x+y))),(y*2+(l-y)))        
