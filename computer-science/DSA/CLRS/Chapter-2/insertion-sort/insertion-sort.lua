local function insertion_sort(num_array)
  local length = #num_array
  for i = 1, length, 1 do
    local key = num_array[i]
    local j = i - 1

    while j > 0 and key < num_array[j] do
      num_array[j+1] = num_array[j]
      j = j - 1
    end
    num_array[j + 1] = key
  end

  return num_array
end

local function print_array(num_array)
  local output = ""
  local length = #num_array

  for i = 1, length, 1 do
    output = output .. " " .. num_array[i]
  end

  output = "[" .. output .. "]"

  print(output)
end

local num_array = {3, 1, 5, 6, -3, -4, 15, 2, 3}

print("before")
print_array(num_array)

print('after')
local sorted_array = insertion_sort(num_array)
print_array(sorted_array)
