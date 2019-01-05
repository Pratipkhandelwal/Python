def nextDuplicates(c):
    dupl_c = dict()
    sorted_ind_c = sorted(range(len(c)), key=lambda x: c[x])
    for i in range(len(c) - 1):
        if c[sorted_ind_c[i]] == c[sorted_ind_c[i+1]]:
            dupl_c[ sorted_ind_c[i] ] = sorted_ind_c[i+1]
    return dupl_c

t = int(input())
for z in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    #result=[idx for idx, item in enumerate(a) if item in a[:idx]]
    #print(result)
    b = nextDuplicates(a)
    if(len(b)==0):
        print("Poor Chef")
        continue
    
    else:     
        for k,v in b.items():
            if(k+1) in a and (v+1) in a:
                flag=1
                break
            else:
                flag=0
                continue

        if(flag==1):
            print("Truly Happy")
        else:
            print("Poor Chef")

