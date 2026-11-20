#include <stdio.h>
#include <stdlib.h>

void insertion_sort(int num_array[], size_t length) {
  for (size_t i = 1; i < length; ++i) {
    int key = num_array[i];
    int j = i - 1;
    while (j >= 0 & key < num_array[j]) {
      num_array[j + 1] = num_array[j];
      j--;
    }
    num_array[j + 1] = key;
  };
}

void print_array(const int num_array[], size_t length) {
  printf("[");

  for (size_t i = 0; i < length; ++i) {
    printf("%d", num_array[i]);

    if (i < length - 1) {
      printf(", ");
    }
  }

  printf("]");
}

int main(void) {
  int num_array[] = {-12, 11, 13, 5, 6};
  size_t length = sizeof num_array / sizeof num_array[0];

  printf("before sorting: ");
  print_array(num_array, length);
  printf("\nafter sorting: ");
  insertion_sort(num_array, length);
  print_array(num_array, length);

  return EXIT_SUCCESS;
}
