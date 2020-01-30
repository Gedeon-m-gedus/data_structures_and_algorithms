def binarySearch(arr , number):
    length = len(arr)
    midPoint = length//2
    if length == 0 or midPoint==0: return False
    if arr[midPoint]==number: return True
    elif arr[midPoint]>number:
        return binarySearch(arr[0:midPoint] , number)
    else:# arr[midPoint]<number:
        return binarySearch(arr[midPoint:] , number)

arr = [1,2,3,5,6,7,8,9]
number = 20
print(binarySearch(arr , number))
arr = [1,2,3,5,6,7,8,9]
number = 8
print(binarySearch(arr , number))