def selection_sort(num_array: list[int]) -> list[int]:
    length = len(num_array)
    for i in range(length-1):
        min_value = num_array[i]
        min_index = i
        for j in range(i + 1, length):   
            if min_value > num_array[j]:
                min_value = num_array[j]
                min_index = j
        num_array[i], num_array[min_index] = min_value, num_array[i]
    return num_array
