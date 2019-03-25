def sub_lists(list1,k): 
  
    sublist = [[]] 
    c = 0
    m = 1000000007
    for i in range(len(list1) + 1): 
          
        for j in range(i + 1, len(list1) + 1): 
              
            sub = list1[i:j]
            if(sum(sub)<=k):
                c+=1
      
    return c%m
            
  
# driver code 
t = int(input())
for z in range(t):
    n,m,k = map(int,input().split())
    arr = list(map(int,input().split()))
    brr = arr * m
    
    print(sub_lists(brr,k)) 
