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

## Codes to rotate an array iven number of rotaions
def rotate_arr(arr,num):#input array and number of rotations
    while num>0:
        l = []
        num -= 1
        l.append(arr[len(arr)-1])
        l = l + arr[:len(arr)-1]
        arr = l
    return arr
print(rotate_arr([1,2,3,4,5,6],2))

## Converting English clock into french clock
def clock(eng_time):
    h = int(eng_time[0:2])
    if eng_time[8:10] == 'PM' and h != 12:
        h = h + 12
        h = str(h)
        h = h + eng_time[2:8]
    elif eng_time[8:10] == 'AM' and h == 12:
        h = '00'
        h = h + eng_time[2:8]
    elif eng_time[8:10] == 'AM':
        h = eng_time[0:8]
    return h
print(clock('12:23:35PM'))

## Intersection of two arrays
def intsectionArrays(arr1,arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    return list(s1.intersection(s2))
print(intsectionArrays([1,2,3,4,5],[1,4,6,7,4,8]))




    
    

