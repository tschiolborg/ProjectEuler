from math import sqrt

# same as 5.py, finds primes bellow n
def sumPrimes(n):
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
    return sum(primes)

# 5 sec faster
# makes the complete list from 2 to n, and then removes all the multiples of each number
def sumPrimes2(n):
    primes = list(range(2,n))
    i = 0
    while primes[i] <= sqrt(n):
        lessThanI = primes[:i+1]
        removedMultipleOfI = list(filter(lambda x: x % primes[i] != 0, primes[i+1:]))
        lessThanI.extend(removedMultipleOfI)
        primes = lessThanI
        i += 1
    return sum(primes)

# much faster
# list of odd numbers and 2 is created, then untill sqrt(n) all multiples of each number is set to 0
# the multiples is found from k^2 to n, since all numbers below is checked, the step-length is set to 2*k,
# because k^2 is odd, and odd + odd is even, which is covered by 2
def sumPrimes3(n):
    primes = [2]
    primes.extend(list(range(3,n,2)))
    i = 1
    while i*2+1 <= sqrt(n):
        if primes[i] != 0:
            k = i*2+1
            for j in range(k**2,n,k*2):
                primes[(j-1)/2] = 0
        i += 1
    # primes = list(filter(lambda x: x != 0, primes))  # <-- optional if the list without 0s is wanted
    return sum(primes)

# slightly faster than sumPrimes3 if the list is wanted.
# Here a boolean list is used 
def primesTo(n): 
    prime = [True for i in range(int(n/2))]
    p = 1
    while (p*2+1 <= sqrt(n)): 
        if (prime[p] == True): 
            k = p*2+1
            for i in range(k*k, n, k*2): 
                prime[(i-1)/2] = False
        p += 1
    primes = [2]
    for p in range(1, int(n/2)): 
        if prime[p]: 
            primes.append(p*2+1)
    return primes

n = 2000000
print(sumPrimes3(n))

