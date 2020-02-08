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

#Given an array of integers nums, write a method that returns the "pivot" index of this array.

def pivotIndex(nums):
    for i in range(len(nums)):
        s1 = sum(nums[:i])
        s2 = sum(nums[i+1:])
        if s1 ==s2 : return i
    return -1

#In a given integer array nums, there is always exactly one largest element.

#Find whether the largest element in the array is at least twice as much as every other number in the array.

#If it is, return the index of the largest element, otherwise return -1.

def dominantIndex( nums):
        
        mx = max(nums)
        for i in range(len(nums)):
            if nums[i]==mx: t = i
            if nums[i]!=mx:
                if mx>=2*nums[i]:
                    k = False
                else: return -1
            
        return t
#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne( digits):
        dig = "".join([str(i) for i in digits])
        dig2 = int(dig)
        dig3 = dig2+1
        dig4 = str(dig3)
        return [int(char) for char in dig4]

## given a list, write a function that return sub array with at most k odd number, and the sub lists have to be contigious

def distinctSubKodds(nums,k):
    sol = {}
    for i in range(len(nums)):
        sol.add(nums[i])
        odd_count = 0
        A_sol = []
        for j in range(i,len(nums)):
            if nums[j]%2 != 0:
                odd_count += 1
                if odd_count > k:
                    break
                A_sol.append(nums[j])

##creating pascal triangle
def generate( numRows):
            l1 = [1]
            l2 = [1,1]
            ans = [l1,l2]
            if numRows <= 0: return []
            if numRows == 1: return [[1]]

            while numRows>2:
                md = []
                numRows-=1
                for i in range (len(l2)-1):
                    md.append(l2[i]+l2[i+1])
                l2 = l1+md+l1
                ans.append(l2)
            return ans

## checking string within big string
def strStr( haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '' and needle == '': return 0
        l = len(needle)
        k = 0
        while k<len(haystack):
            if haystack[k:k+l]==needle: return k
            k +=1
        return -1
def strStr( haystack, needle):
    try:
        return haystack.index(needle)
    except:
        return -1
            