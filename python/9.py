
# a can max be n/3-1, from where a loop check if a+b+c = n and a^2 + b^2 = c^2
# a go down to 1, b goes up untill a+b+c is too big, where for each b, c goes up untill a+b+c is too big.
# for each a, b = a+1, and for each b, c = b+1
def pythagoreanTriplet(n):
    a = n/3-1
    while a > 0:
        b = a+1
        c = b+1
        while a+b+c <= n:
            while a+b+c <= n:
                if a**2 + b**2 == c**2 and a+b+c == n:
                    return (a*b*c,a,b,c)
                c += 1
            b += 1
            c = b+1
        a -= 1
    return (0,0,0,0)

# a+b+c=n <=> c = n-a-b  ->  a^2+b^2=(n-a-b)^2, when almost same method with only loop for a and b now.
def pythagoreanTriplet2(n):
    for a in range(1,n/3):
        for b in range(a+1,(n-1-a)/2):
            c = n-a-b
            if a**2+b**2 == c**2:
                return (a*b*c,a,b,c)
    return (0,0,0,0)


n = 1000
print(pythagoreanTriplet(n))




