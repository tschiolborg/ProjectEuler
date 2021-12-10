from math import sqrt
# loop from 2 to sqrt(n), because the highest factor must be k * k = n, 
# for every other factors k1 * k2 = n, must k1 < k < k2, where the smaller factor k1 = i.
# note n is divided by i as long as n % i = 0, in that way multiples of i (that isnt prime) will be not be counted
# +2 for faster loop so multiples of 2 isnt tested
def findLargestPrime(n):
    i = 2
    while i <= sqrt(n):
        while n % i == 0 and n != i:
            n /= i
        if i == 2:
            i -= 1
        i += 2
    return n


n = 600851475143
print(findLargestPrime(n))
