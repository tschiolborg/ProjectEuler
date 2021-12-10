# test all i=1..n if n%a = 0 or n%b = 0, then add them to the sum
def sumMultiple(n,a,b):
    sum = 0
    for i in range(1,n):
        if i % a == 0 or i % b == 0: #important to have in same if to not count doubles
            sum += i
    return sum

# sum multiples of a to n:  a*sum(i,i=1..k) = a*(k*(k+1))/2 , where k = int(n/a)
def sumMultiple2(n,a):
    k = n/a
    return a*(k*(k+1))/2

a = 3
b = 5
n = 1000
print(sumMultiple(n,a,b))
print(sumMultiple2(n,a)+sumMultiple2(n,b)-sumMultiple2(n,a*b))


