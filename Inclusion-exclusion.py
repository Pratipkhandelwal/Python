'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
n=int(raw_input())
ans=int(n/2)+int(n/3)+int(n/11)+int(n/13)-int(n/6)-int(n/22)-int(n/26)-int(n/33)-int(n/39)-int(n/143)+int(n/66)+int(n/78)+int(n/286)+int(n/429)-int(n/858)
p=gcd(ans,n)
print(ans/p),
print(n/p)

#n(AᴜBᴜC) = n(A) + n(B) + n(C) – n(A∩B) – n(B∩C) – n(C∩A) + n(A∩B∩C)
#set theory problem
