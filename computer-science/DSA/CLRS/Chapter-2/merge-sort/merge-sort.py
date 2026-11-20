def merge(num_array: list[int], initial_index: int, middle_index: int, final_index: int) -> None:
    
    left_array = num_array[initial_index : middle_index + 1]
    right_array = num_array[middle_index + 1 : final_index + 1]

    left_array_length = len(left_array)
    right_array_length = len(right_array)

    i, j, k = 0, 0, initial_index

    while i < left_array_length and j < right_array_length:
        if left_array[i] <= right_array[j]:
            num_array[k] = left_array[i]
            i += 1
            k += 1
        else:
            num_array[k] = right_array[j]
            j += 1
            k += 1

    while i < left_array_length:
            num_array[k] = left_array[i]
            i += 1
            k += 1

    while j < right_array_length:
            num_array[k] = right_array[j]
            j += 1
            k += 1

def merge_sort(num_array: list[int], initial_index: int, final_index: int) -> None:

    if initial_index >= final_index:
        return

    middle_index = (initial_index + final_index) // 2
    merge_sort(num_array, initial_index, middle_index)
    merge_sort(num_array, middle_index + 1, final_index)
    merge(num_array, initial_index, middle_index, final_index)
