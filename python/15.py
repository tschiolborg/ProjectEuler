
# calculates how many different ways are left, while it stores the value in a dict
def ways(x,y):
    w = 0
    s = str(n-x)+" "+str(n-y)
    if values.get(s,0) != 0:
        return values[s]
    if x == n and y == n:
        w = 1
    else:
        if x < n:
            w = ways(x+1,y)
        if y < n:
            w += ways(x,y+1)
    values[s] = w
    return w


values = dict()

n = 20
print(ways(0,0))

