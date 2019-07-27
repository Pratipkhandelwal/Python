{

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''


# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(a,b):
    diff = {}

    for i in a:
        if i not in diff:
            diff[i] = 0
        diff[i] +=1

    for i in b:
        if i not in diff:
            diff[i] = 0
        diff[i] -=1

    return sum(abs(n) for n in diff.values())
