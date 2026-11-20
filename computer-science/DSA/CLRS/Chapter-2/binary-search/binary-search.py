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

        
