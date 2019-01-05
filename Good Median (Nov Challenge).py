#import novt6b

M=1000000007
C=None
SC=None

def genC(n,M):
    C=[[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(n+1):C[i][0]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            C[i][j]=C[i-1][j]+C[i-1][j-1]        
    return C

def genSC(n,M):
    SC=[[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(n+1):SC[i][0]=C[i][0]
    for i in range(1,n+1):
        for j in range(1,n+1):
            SC[i][j]=(C[i][j]%M+SC[i][j-1]%M)%M        
    return SC
    
def series_sum(l1,l2,m):#todo what if l1==l2==0,m==1?
    #print(l1,l2,m)
    if l1>l2:l1,l2=l2,l1
    s=0
    for i in range(m-1):
        if l1==0:
            s=(s%M+SC[l1+l2+m-2-i][l1+m-2-i]%M)%M
        else:
            s=(s%M+((SC[l1+l2+m-2-i][l1+m-2-i]%M-SC[l1+l2+m-2-i][l1-1]%M)+M)%M)%M
    return s
    

def findSubs(arr,M):
    arr.sort()
    sum_e=0
    sum_o=0
    i=0
    while i<len(arr)-1:
        j=i+1
        while j<len(arr) and arr[j]==arr[i]:
            j+=1
        sum_e=(sum_e%M + series_sum(i,len(arr)-j,j-i)%M)%M
        i=j
    sum_o=pow(2,len(arr)-1,M)
    #print(sum_e,sum_o)
    total=(sum_e+sum_o)%M
    return total

#import random as r
C=genC(1000,M)
SC=genSC(1000,M)
t=int(input())
for _ in range(t):
    int(input())
    arr=[int(i) for i in input().split()]
    #arr=[r.randrange(1001) for i in range(1001)]
    #print(sorted(arr))
    print(findSubs(arr,M))
    #ans1=findSubs(arr,M)
    #ans2=novt6b.findSubs(arr,M)
    '''if ans1!=ans2:
        print(ans1,ans2)
        print(sorted(arr))'''
    
            
