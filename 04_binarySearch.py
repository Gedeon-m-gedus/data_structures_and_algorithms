def binary_search(input_array, value):
    """Your code goes here."""
    l = len(input_array)
    pos = l//2
    i = 0
    for j in range(l):
        indx = pos
        print (j,' ',input_array[indx],' ',indx)
        i+=1
        
        if input_array[indx]==value:
            return 1
        elif input_array[indx]<value: 
            b = l//(4*i)
            if b == 0:b=1
            pos = pos + b
            if indx == pos: return -1
        elif input_array[indx]>value: 
            b = l//(4*i)
            if b == 0:b=1
            pos = pos - b
            if indx == pos: return -1
        if pos > l-1 or pos < 0:return -1
        

test_list = [1,3,9,11,15,19,29,39,41,71,92]
test_val1 = 2
test_val2 = 92
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))