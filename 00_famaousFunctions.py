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

##_________________________________________________________________________________
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

##_________________________________________________________________________________
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

##_________________________________________________________________________________
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

##_________________________________________________________________________________
## Intersection of two arrays
def intsectionArrays(arr1,arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    return list(s1.intersection(s2))
print(intsectionArrays([1,2,3,4,5],[1,4,6,7,4,8]))

##_________________________________________________________________________________
## return a list of all array elements being multiplied but excluding index itself
def mult(arr): #naive approach
    ans = []
    p = 1
    for i in  (arr):
        p=p*i
    for i in (arr):
        ans.append(p/i)
    return ans  
arr=[1,2,3,4,5]
print(mult(arr))
def mult(arr):## without using division
    ans = []
    for i in range(len(arr)):
        ans.append(fronnt(arr[:i])*fronnt(arr[i+1:]))
    return ans  
def fronnt(arr):
    p = 1
    for i in arr:
        p=p*i
    return p
arr=[1,2,3,4,5]
print(mult(arr))

##________________________________________________________________________
def mult(arr):#forward and backwward implementation
    cur_mul = 1
    prev_mul = 1
    l1 = []
    for i in range(len(arr)):
        prev_mul = cur_mul
        cur_mul *= arr[i]
        l1.append(prev_mul)
    
    cur_mul = 1
    prev_mul = 1
    l2 = []
    for i in range (-1,-len(arr)-1,-1):
        prev_mul = cur_mul
        cur_mul *= arr[i] 
        l2.append(l1[i]*prev_mul)
    
    return l2[::-1]
arr=[1,2,3,4,5]
print(mult(arr))

##_____________________________________
#getting dictionary from string input, characters will be keys and their frequency will be values
def str_dic(txt):
    dic = {}
    for i in txt:
        if i in dic.keys():
            dic[i]=dic[i]+1
        else:dic[i]=1
    return dic

txt = 'abas'
print(str_dic(txt))


    
    

