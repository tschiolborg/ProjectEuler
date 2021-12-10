from math import log, sqrt

# test all m from n untill one is found with interval equal to n.
# it will only test the numbers n/2..n, starting from the top, because a number i <= n/2 will be a multiple of a number n >= x > n/2 
def smallestMultiple(n):
    isFound = False
    m = n
    while not isFound:
        isFound = True
        m += n
        for i in range(n,n/2,-1):
            if m % i != 0:
                isFound = False
                break
    return m

# finds primes bellow n
# i is only tested for p < sqrt(n), because if k*k=n, when two primes k1*k2=n will be in interval k1 < k < k2
# since every prime > 3 will be on the form 6k+1 or 6k-1 every 2nd or 4th i is tested for being a prime
def primesTo(n):
    n += 1
    primes = [2]
    i = 3
    while i < n:
        isPrime = True
        for p in primes:
            if p > sqrt(n):
                break
            if i % p == 0:
                isPrime = False
        if isPrime:
            primes.append(i)
        if (i-1) % 6 == 0:
            i += 4
        else:
            i += 2
    return primes

# since all numbers <= n can be written as a product of primes <= n,
# then the resulting number can be written only using all of the primes <=n, because it will be a multiple of these.
# The power of each prime "a" from the equation: p^a <= n, can be calculated with: a = floor( log(n)/log(p) )
def smallestMultiple2(n):
    prodSum = 1
    for i in primesTo(n):
        prodSum *= i**int( log(n)/log(i) )
    return prodSum

# smallestMultiple3 is slightly faster, because of faster method in primesTo2, see 10.py
def primesTo2(n):
    n += 1
    primes = [2]
    primes.extend(list(range(3,n,2)))
    i = 1
    while i*2+1 <= sqrt(n):
        if primes[i] != 0:
            k = i*2+1
            for j in range(k**2,n,k*2):
                primes[(j-1)/2] = 0
        i += 1
    primes = list(filter(lambda x: x != 0, primes))
    return primes
def smallestMultiple3(n):
    prodSum = 1
    for i in primesTo2(n):
        prodSum *= i**int( log(n)/log(i) )
    return prodSum


n = 20
print(smallestMultiple3(n))

