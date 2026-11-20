def recursive_binary_search_num(sorted_num_array: list[int], search_key: int, lower_index: int, upper_index: int) -> int:
    """
    Applies a recursive binary search on an integer array sorted in ascending order. 
    Uses sentinal value for -1.

    Parameters:
        sorted_num_array: list[int] = array to be searched
        lower_index: int = lower index of the array (pass 0 initially)
        upper_index: int = upper index of the array (pass length-1 of the array initially)

    Return:
        index : index where the algorithm found the search_key
        if -1 is returned, the search_key is not found.
    """
    if lower_index > upper_index:
        return -1
    
    middle_index = (upper_index + lower_index) // 2
    key = sorted_num_array[middle_index]

    if search_key == key:
        return middle_index
    
    if search_key < key:
        return recursive_binary_search_num(sorted_num_array, search_key, lower_index, middle_index - 1)
    else:
        return recursive_binary_search_num(sorted_num_array, search_key, middle_index + 1, upper_index)
