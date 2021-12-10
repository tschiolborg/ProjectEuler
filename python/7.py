from math import sqrt

# same as 5.py, where instead of finding primes to n, it finds n primes from 1st to nth prime
def nPrimes(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        isPrime = True
        for p in primes:
            if p > sqrt(i):
                break
            if i % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        if (i-1) % 6 == 0:
            i += 4
        else:
            i += 2
    return primes

# returns nth prime
def nthPrime(n):
    primes = nPrimes(n)
    return primes[-1]

n = 10001

print(nthPrime(n))



