for _ in range(int(input())):
    n=int(input());
    l=list(map(int,input().split()));
    l1=list(map(int,input().split()));
    l2=list(enumerate(zip(l,l1)));
    print(list(l2));
    l2.sort(key=lambda x:x[1][1]);
    print("=====================")
    print(list(l2));
    j=0
    print(l2[0][0]+1,end=" ");
    for i in range(1,len(l2)):
        if(l2[i][1][0]>=l2[j][1][1]):
            print(l2[i][0]+1,end=" ");
            j=i;
    print();

