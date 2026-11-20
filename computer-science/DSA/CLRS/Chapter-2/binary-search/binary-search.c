#include "stdlib.h"

int binary_search_int(const int *int_array, size_t int_array_length, int search_key) {
  // sentinal value of -1 if not found, assuming an ascending array

  size_t lower_index = 0;
  size_t upper_index = int_array_length - 1;

  while (lower_index <= upper_index) {

    size_t middle_index = lower_index + (upper_index - lower_index) / 2; // protection against overflows

    int key = int_array[middle_index];

    if (search_key == key) {
      return (int)middle_index; // casting to int
    }

    if (search_key < key) {
      upper_index = middle_index; // no -1 to protect against overflows
    }
    else {
      lower_index = middle_index + 1;
    }
  }

  return -1;
}
