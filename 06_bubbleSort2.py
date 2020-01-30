#this bubble sort is optimized, it will not compare the elements which are already sorted
def bubbleSort(arr):
    for n in range(len(arr)):
        j=0
        #print(arr)
        for i in range(1,len(arr)-n):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
arr = [2,3,4,0,7,0,-7,3,1]
print(bubbleSort(arr))