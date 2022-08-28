# i and j loop from 10^n-1 to 10^(n-1) (here 999 and 100) and let k = i*j, where k is tested if a palindrome
# for not testing the same number twice j is stopped when j = i, this also makes the loop faster
# if k is found to be a smaller number than the newest found palindrome then the loop is stopped
def largestPalindrom(n):
    (p,x,y) = (0,0,0)
    for i in range(pow(10,n)-1,pow(10,n-1),-1):
        for j in range(pow(10,n)-1,i,-1):
            k = i*j
            if k < p:
                break
            klist = [int(d) for d in str(k)]
            k1 = klist[:int(len(klist)/2.0+0.5)]
            k2 = klist[int(len(klist)/2):]
            if k1 == k2[::-1]:
                (p,x,y) = (k,i,j)
    return (p,x,y)


n = 3
print(largestPalindrom(n))



