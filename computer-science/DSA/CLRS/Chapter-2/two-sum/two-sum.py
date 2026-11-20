def two_sum_linear(num_array : list[int], sum : int) -> bool:

    hashtable = set() 

    for num in num_array:
    
        if num in hashtable:
            return True
        else:
            hashtable.add(sum - num)

    return False


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

def binary_search_num(sorted_num_array: list[int], search_key: int) -> int:
    # sentinal value will be len + 1, array assumed to be in ascending order

    sorted_num_array_length = len(sorted_num_array)

    lower_index = 0
    upper_index = sorted_num_array_length - 1
    
    found_index = sorted_num_array_length + 1

    while found_index > sorted_num_array_length and lower_index <= upper_index:

        middle_index = (lower_index + upper_index) // 2

        key = sorted_num_array[middle_index]
        
        if search_key == key:
            found_index = middle_index
            return found_index

        if search_key <= key:
            upper_index = middle_index - 1
        else:
            lower_index = middle_index + 1

    return found_index


def two_sum(num_array : list[int], sum : int) -> bool:

    merge_sort(num_array, 0, len(num_array))

    for num in num_array:
        
        if binary_search_num(num_array, num) < len(num_array) + 1:
            return True
    
    return True
