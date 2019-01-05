A = int(input())
if A<0:
    A = -A
    b = str(A)[::-1]
    print('-' + b)
else:
    print(str(A)[::-1])
if(-2147483648 > A):
    print(0)
if(2147483648 < A):
    print(0)
        


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        sgn = -1 if A < 0 else 1
        A = abs(A)
        string = str(A)
        reverse = string[::-1]
        result = int(reverse)
        if result > 2**31 - 1:
            return 0
        return sgn * result
        
