
num2let = {"1":3,"2":3,"3":5,"4":4,"5":4,"6":3,"7":5,"8":5,"9":4,"10":3,"11":6,"12":6,"13":8,"15":7,"18":8,"20":6,"30":6,"40":5,"50":5,"60":5,"70":7,"80":6,"90":6,"100":10,"1000":11}

def numInWord(n):
    if num2let.get(str(n),0) != 0:
        return num2let[str(n)]
    if n < 1:
        return 0
    if n < 20:
        return numInWord(n-(n/10)*10) + 4
    elif n < 100:
        return numInWord(n-(n/10)*10) + numInWord((n/10)*10)
    elif n < 1000:
        if n % 100 != 0:
            return numInWord(n-(n/100)*100) + numInWord((n/100)*100) + 3
        else:
            return numInWord(n/100) + 7
    else:
        return 0

# count all of the letters for every word of all numbers from 1 to 1000.
sum = 0
for i in range(1,1001):
    sum += numInWord(i)
print(sum)


