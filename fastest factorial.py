def get_factorial2(n):
    old = [1]
    current = []
    for i in range(2, n+1):
        carry = 0
        for digit in old:
            prod = int(digit) * i + carry
            rem = prod % 10
            current.append(rem)
            carry = prod / 10

        if carry != 0:
            for j in str(carry)[::-1]:
                current.append(j)  # add j as a str
        old = current
        current = []
    
    return "".join(map(str,old[::-1])) # convert everything to str before concatenation and returning the results
                
            

n = int(input())
print(get_factorial2(n))
