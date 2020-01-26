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

## inplace removing element from a list of posivite numbers
def remove_number(arr,num):
    k = 0
    print(arr)
    for i in range(len(arr)):
        if arr[i]==num: 
            arr[i]=-1
            k+=1
    arr.sort(reverse=True)
    while k>0:
        k-=1
        arr.pop()
    return arr
print(remove_number([3,3,2,33],3))
    

