local function linear_search(input_array, target_value)
  local length = #input_array
  for i = 1, length, 1 do
    local key = input_array[i]
    if key == target_value then
      return i
    end
  end
  return -1
end

local function print_array(input_array)
  local output = ""
  local length = #input_array

  for i = 1, length, 1 do
    output = output .. " " .. input_array[i]
  end

  print(output)
end

local number_array = {1, 3, 5, 6}
local target1 = 3
local target2 = -5

print_array(number_array)
print("target 1 = ", target1)
print("located at", linear_search(number_array, target1))
print("target 2 = ", target2)
print("located at", linear_search(number_array, target2))
