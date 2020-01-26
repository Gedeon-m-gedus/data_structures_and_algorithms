#Computing divisors of a number
def possible_div(n):
    i = 1
    l = []
    k = n**0.5
    while i<=k:
        if n % i ==0:
            l.append(i)
            j = int(n/i)
            if j !=i:l.append(j)
        i += 1
    return l
print(possible_div(10))  
