def count_inversions(num_array: list[int]) -> int:
    length = len(num_array)
    number_inv = 0

    for i in range(1, length):
        key = num_array[i]
        j = i - 1
        while j >= 0 and key < num_array[j]:
            num_array[j + 1] = num_array[j]
            number_inv += 1
        num_array[j + 1] = key

    return number_inv
