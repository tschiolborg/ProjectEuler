# Difference of (1+2+...+n)^2 - 1^2+2^2+...+n^2 with use of "sum"-function
def sumSquareDiff(n):
    s1 = pow(sum(range(1,n+1)),2)
    s2 = sum([pow(d,2) for d in range(1,n+1)])
    return s1-s2

# with use of formulars n*(n+1)/2 and n*(2n+1)*(n+1)/6
def sumSquareDiff2(n):
    s1 = n*(n+1)/2
    s2 = n*(2*n+1)*(n+1)/6
    return s1**2 - s2

n = 100
print(sumSquareDiff2(n))


