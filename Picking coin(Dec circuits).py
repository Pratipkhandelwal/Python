t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = n
    if(n<k):
        print("Bob")
        continue
    
    if(k==1):
        if(n%2==0):
            print("Bob")
            continue
        else:
            print("Alice")
            continue
        
    for i in range(1,n):
        if(a >= pow(k,i)):           
            alice_rem = a - pow(k,i)
            flag = 1
        if(alice_rem >= pow(k,i) and alice_rem>0):
            bob_rem = alice_rem - pow(k,i)
            flag = 2
            a = bob_rem
        else:
            break
    if(flag==2):
        print("Bob")
    else:
        print("Alice")
