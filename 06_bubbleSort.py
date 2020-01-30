## this bubble sort algorithms, at each iteration it bubbles the big number to the right side
def bubbleSort(arr):
    for n in range(len(arr)):
        j=0
        for i in range(1,len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr

arr = [2,3,4,0,7,0,3,1]
print(bubbleSort(arr))