// Basic imports

#include <stdio.h>
#include <stdlib.h>

size_t linear_search(const int input_array[], const int target_value, const size_t length) {

  for (size_t i = 0; i < length; ++i) {
    int key = input_array[i];
    if (key == target_value) {
      return i;
    }
  }

  return length;
}

void print_array(const int input_array[], const size_t length) {
  printf("[");

  for (size_t i = 0; i < length; i++) {
    if (i > 0) {
      printf(", ");
    }
    printf("%d", input_array[i]);
    
  }

  printf("]");
}

int main() {
  int input_array[5] = {1, -3, 5, 9, 3};
  size_t length = sizeof input_array / sizeof input_array[0];
  int targets[2] = {9, -5};

  printf("The array: ");
  print_array(input_array, length);
  for (size_t i = 0; i < 2; i++) {
    printf("\ntarget %zu : %d\n",
           i + 1,
           targets[i]);
    printf("target %zu found at location: %zu\n",
           i + 1,
           linear_search(input_array, targets[i], length));
  }
}
