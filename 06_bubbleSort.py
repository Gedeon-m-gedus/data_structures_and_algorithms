def bubbleSort(arr):
    for n in range(len(arr)):
        j=0
        for i in range(1,len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr