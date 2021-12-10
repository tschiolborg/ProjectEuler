
# The Collatz Sequence is defined the return n/2 when n is even, and 3n+1 when n is odd.
# Since 3n+1 is even (3n+1)/2 can be used instead while adding 2.
# Chain length for each n is stored i dict.
def collatzSequence(n):
    c = collatz.get(n,0)
    if c != 0:
        return c
    elif n % 2 == 0:
        collatz[n] = 1 + collatzSequence(n/2)
    else:
        collatz[n] = 2 + collatzSequence((3*n+1)/2)
    return collatz[n]


import time
t1 = time.time()

(I,J) = (0,0)
collatz = {1: 1}
n = 10**6
# since every number above n/2 divided with 2 must be a number below n/2, only numbers above or equal to n/2 must be checked 
for j in range(n/2,n):
    i = collatzSequence(j)
    if i > I:
        (I,J) = (i,j)
print(I,J)

t2 = time.time()
print(t2-t1)
