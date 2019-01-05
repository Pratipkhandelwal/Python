import math
a = list(map(int,input().split()))
box = a[1:]
#print(box)
b = list()
#for i in range(0,len(box)):
#    ridge = math.pow(2,box[i])
#    b.append(1)
#    b.append(int(ridge))
#print(*b)
for i in range(0,len(box)):
    if(box[i]==1):
        b.append(1)
        b.append(2)
    if(box[i]==2):
        b.append(1)
        b.append(4)
    if(box[i]==3):
        b.append(3)
        b.append(8)
    if(box[i]==4):
        b.append(5)
        b.append(16)
    if(box[i]==5):
        b.append(11)
        b.append(32)  
    if(box[i]==6):
        b.append(21)
        b.append(64)
    if(box[i]==7):
        b.append(43)
        b.append(128)
    if(box[i]==8):
        b.append(85)
        b.append(256)
    if(box[i]==9):
        b.append(171)
        b.append(512)
    if(box[i]==10):
        b.append(341)
        b.append(1024)
    if(box[i]==11):
        b.append(683)
        b.append(2048)
    if(box[i]==12):
        b.append(1365)
        b.append(4096)
    if(box[i]==13):
        b.append(2731)
        b.append(8192)
    if(box[i]==14):
        b.append(5461)
        b.append(16384)
    if(box[i]==15):
        b.append(10923)
        b.append(32768)
    if(box[i]==16):
        b.append(21845)
        b.append(65536)
    if(box[i]==17):
        b.append(43691)
        b.append(131072)
    if(box[i]==18):
        b.append(87381)
        b.append(262144)
    if(box[i]==19):
        b.append(174763)
        b.append(524288)
    if(box[i]==20):
        b.append(349525)
        b.append(1048576)
    if(box[i]==21):
        b.append(699051)
        b.append(2097152)
    if(box[i]==22):
        b.append(1398101)
        b.append(4194304)
    if(box[i]==23):
        b.append(2796203)
        b.append(8388608)
    if(box[i]==24):
        b.append(5592405)
        b.append(16777216)
    if(box[i]==25):
        b.append(11184811)
        b.append(33554432)
print(*b)
    
