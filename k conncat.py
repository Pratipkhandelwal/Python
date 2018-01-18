def mssl(arr, x, f):
        max_sum = -999999999
        sum1 = 0
        c_sum = 0
        times = f
        b=1
        prev=-1
        curr = 0
        do:
              curr = 0
              for i in range((x+1)%len(arr)*b):
              sum1+=arr[i]
              if sum1>max_sum:
                 max_sum = sum1
              if sum1<0:
                 sum1 = 0
              curr = curr + max_sum
              b+=1
              if(curr>prev): 
                 prev = curr
              else:
                  prev=max_sum
              print("curr is :",curr)
              print("prev is :",prev)
              while(b<=f)
              
    return (prev)    
                                                                               
 
    
t = int(input())
for p in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    c = mssl(a,n,k)
    print(c)
        
