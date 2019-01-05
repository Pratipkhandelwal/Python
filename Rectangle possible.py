n = int(input())
a = list(map(int,input().split()))
b = list(set(a))
rect = [ ]
square = []
counts = []
no_of_rect = 0
mod = 1000000007
if(len(b)>=2):
    for i in range(0,len(b)):
        if(a.count(b[i])>=2):
            counts.append(a.count(b[i])//2)
    #print(counts)
    if(len(counts)>=2):                
        for j in range(0,len(counts)-1):
            l = counts[j+1:]
            val = sum(l)
            no_of_rect += counts[j] * val

        print(no_of_rect%mod)
    else:
        print("0")
        
else:
    print("0")
