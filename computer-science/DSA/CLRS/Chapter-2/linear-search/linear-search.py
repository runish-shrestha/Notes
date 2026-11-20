def linear_search(input_array : list[int], target : int) -> int:
    length = len(input_array)

    for i in range(0, length):
        key = input_array[i]
        if key == target:
            return i
    
    return -1

num_array = [1, 3, 5, 6]
target1 = 5
target2 = 9

print("num_array: ", num_array)
print("target 1: ", target1, " is at ", linear_search(num_array, target1))
print("target 2: ", target2, " is at ", linear_search(num_array, target2))

