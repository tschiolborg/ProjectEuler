# test every fib and add to sum if even
def fibSum(n):
    a = 0
    b = 1
    sum = 0
    while b < n:
        temp = b
        b = b + a
        a = temp
        if b % 2 == 0:
            sum += b
    return sum

# avoid if-statement because every 3rd number is even since odd+odd=even, odd+even=odd and so on
def fibSum2(n):
    a = 1
    b = 1
    c = 2
    sum = 0
    while b < n:
        sum += c
        a = c + b
        b = a + c
        c = b + a
    return sum



n = 4000000
print(fibSum(n))
print(fibSum2(n))

