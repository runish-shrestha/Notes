def merge_count(A: list[int], start_index: int, mid_index: int, end_index: int):
    num_inv = 0

    left_A = A[start_index : mid_index + 1]
    right_A = A[mid_index + 1 : end_index + 1]

    k = start_index
    i = 0
    j = 0
    while i < len(left_A) and j < len(right_A):
        if left_A[i] <= right_A[j]:
            A[k] = left_A[i]
            i += 1
            k += 1
        else:
            A[k] = right_A[j]
            j += 1
            k += 1
            num_inv += len(left_A) - i

    while i < len(left_A):
        A[k] = left_A[i]
        i += 1
        k += 1

    while j < len(right_A):
        A[k] = right_A[i]
        j += 1
        k += 1

    return num_inv


def count_inversion(array: list[int], start_index: int, end_index: int) -> int:
    if end_index <= start_index:
        return 0
    else:
        mid_index = (start_index + end_index) // 2
        inv_1 = count_inversion(array, start_index, mid_index)
        inv_2 = count_inversion(array, mid_index + 1, end_index)
        inv_3 = merge_count(array, start_index, mid_index, end_index)
        return inv_1 + inv_2 + inv_3
