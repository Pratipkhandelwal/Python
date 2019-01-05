def MinSwaps(lst1, lst2):
    lst3 = [None] * len(lst1)

    for i in range(len(lst1)):
        lst3[i] = lst2.index(lst1[i])

    return calculateSwapsToSort(lst3)


def calculateSwapsToSort(lst):
    numOfSwaps = 0
    for index in range(len(lst)):
        if index != lst[index]:
            whereIsIndexMatchingNum = lst.index(index) # this variable!
            lst[index], lst[whereIsIndexMatchingNum] = lst[whereIsIndexMatchingNum], lst[index]

            #This is incorrect but the above is correct. I don't see the difference...
            #lst[index], lst[lst.index(index)] = lst[lst.index(index)], lst[index] 

            numOfSwaps +=1
        pass
    return numOfSwaps


A = [1, 2, 3, 0, 4]
B = [3, 4, 1, 0, 2]

print(MinSwaps(A, B))
