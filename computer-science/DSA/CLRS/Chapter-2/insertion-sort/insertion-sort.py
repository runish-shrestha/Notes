def insertion_sort( num_array : list[int] ) -> list[int]:
    
    length = len(num_array)
    
    for i in range(1, length):
        
        key = num_array[i]
        j = i - 1
        
        # inserting elements to their right positions

        while j >= 0 and key > num_array[j]:
            num_array[j + 1] = num_array[j]
            j -= 1
        num_array[j+1] = key

    return num_array


input_array = [1, 3, -2, 13, 5, 7]

print("Before Sorting: ", input_array)

sorted_array = insertion_sort(input_array)

print("After Sorting: ", sorted_array)
