class BinaryInteger:

    def __init__(self, values : list[int]):
        self.__value = values
    
    def _pad_zero(self, num_zeroes):
        for i in range(num_zeroes):
            self.__value.append(0)


    def add(self, binary_integer : BinaryInteger):
           
        # check which integer is smaller and pad them zeroes

        if len(self) >= len(binary_integer):
            num_zeroes = len(self) - len(binary_integer)
            binary_integer._pad_zero(num_zeroes)
        else:
            num_zeroes = len(binary_integer) - len(self)
            self._pad_zero(num_zeroes)

        # add 
        remainder = 0
        for i in range(len(self)): 
            ordinary_sum = self.__value[i] + binary_integer.__value[i] + remainder 
            binary_sum = ordinary_sum % 2
            remainder = ordinary_sum // 2
            self.__value[i] = binary_sum

        if remainder != 0:
            self.__value.append(remainder)
    
    
    def __str__(self):
        output_string = ""
        for digit in self.__value:
            output_string = str(digit) + output_string
        return output_string

    def __len__(self):
        return len(self.__value)

a = BinaryInteger([1])      # 1
b = BinaryInteger([0, 1])   # 2
a.add(b)
print(a)
