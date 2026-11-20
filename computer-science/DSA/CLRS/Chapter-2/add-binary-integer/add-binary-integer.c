#include <stdio.h>
#include <stdlib.h>

#define MAX_BIN_SIZE 64

typedef struct {
  int bits[MAX_BIN_SIZE];
  size_t length;
} BinaryInteger;


BinaryInteger binary_integer(const int digit[], size_t length)
{
  BinaryInteger given_binary_integer = {0};
  
  given_binary_integer.length = length;

  for(size_t i = 0; i < length; ++i) {
    given_binary_integer.bits[i] = digit[length - 1 - i];
  }

  return given_binary_integer;
}

BinaryInteger binary_integer_add(BinaryInteger integer_1, BinaryInteger integer_2) 
{
  BinaryInteger sum_integer = {0};
  int remainder = 0;
  size_t length = 0;

  if (integer_1.length >= integer_2.length) {
    length = integer_1.length;
  }
  else {
    length = integer_2.length;
  }

  for (size_t i = 0; i < length; i++) 
  {
    int sum_digit = integer_1.bits[i] + integer_2.bits[i] + remainder;
    sum_integer.bits[i] = sum_digit % 2;
    remainder = sum_digit / 2; 
  }

  sum_integer.length = length;
  if (remainder != 0) {
    sum_integer.bits[length] = remainder;
    sum_integer.length++;
  }

  return sum_integer;
}

void binary_integer_print(BinaryInteger input_integer) 
{
  size_t length = input_integer.length;

  for (size_t i = 0; i < length; ++i) {
    printf("%d", input_integer.bits[length-1-i]);
  }
}

int main() {
  BinaryInteger a; 
  int a_digit[4] = {1, 1, 0, 0};

  a = binary_integer(a_digit, 4);
  binary_integer_print(a);

  return EXIT_SUCCESS;
}
