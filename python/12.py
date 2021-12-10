from math import sqrt, log

# test all triangular numbers untill one is found to have more than n divisors
def triangularNumbersDivisors(n):
    divisors = 0
    k = 0 # triangular number
    i = 1 # counter or ith triangular number
    while divisors <= n:
        divisors = 0
        k = i*(i+1)/2
        limit = int(sqrt(k))
        for j in range(1,1+limit): # j is possible divisor
            if k % j == 0: # if j is divisor in k, then k/j must also be a divisor, unless j*j = k
                divisors += 2
        if limit**2 == k:
            divisors -= 1
        i += 1
    return (k,divisors)

# primes is used for triangularNumbersDivisors2, see 10.py
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

# the number of divisors of k can be calculated as d = (a_1+1)*...*(a_n+1) for a_i being the exponent of primefactor p_i.
# As d-1 is the number of combinations of the primefactors that is divisible in k.
# large numbers of primes is needed to count the exponents
def divisorsOf(k,primes):
    divisors = 1
    for p in primes:
            if p*p > k: # the prime above or equal to p this must be the last last primefactor with exponent 1.
                divisors *= 2
                break
            a = 1
            while k % p == 0: # each time p is divisible the exponent is counted up.
                a += 1
                k /= p
            if a > 1:
                divisors *= a
            if k == 1:
                break
    return divisors

# As the triangular number kan be written as k = i*(i+1)/2, the divisors for d_k = d_k1 * d_k2,
# where (k1,k2) = (i/2,i+1) when i is even and (k1,k2) = (i,(i+1)/2) when i is odd.
def triangularNumbersDivisors2(n,primes): 
    divisors = 0
    (k1,k2) = (1,1) # the product of these is the triangular number
    i = 0 # counter or ith triangular number
    while divisors <= n:
        divisors = 1
        i += 1
        (k1,k2) = (i/2,i+1)
        if i % 2 != 0:
            (k1,k2) = (i,(i+1)/2)
        divisors = divisorsOf(k1,primes) * divisorsOf(k2,primes)
    return k1*k2



n = 500

import time
'''
t1 = time.time()
print(triangularNumbersDivisors(n))
t2 = time.time()
print(t2-t1)
'''

t1 = time.time()
primes = primesTo(2000)
print(triangularNumbersDivisors2(n,primes))
t2 = time.time()
print(t2-t1)
