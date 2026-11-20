#include "stdlib.h"
#include "stdio.h"

void merge(double *array,
           size_t initial_index,
           size_t middle_index,
           size_t final_index)
{
  size_t left_array_length = middle_index - initial_index + 1;
  size_t right_array_length = final_index - middle_index;

  double left_array[left_array_length];
  double right_array[right_array_length];
  
  for (size_t i = 0; i < left_array_length; ++i) {
    left_array[i] = array[initial_index + i];
  }

  for (size_t j = 0; j < right_array_length; ++j) {
    right_array[j] = array[middle_index+1+j];
  }

  size_t i = 0;
  size_t j = 0;
  size_t k = initial_index;

  while (i < left_array_length && j < right_array_length) {
    if (left_array[i] < right_array[j]) {
      array[k++] = left_array[i++];
    }
    else {
      array[k++] = right_array[j++];
    }
  }

  while (i < left_array_length) {
    array[k] = left_array[i];
    ++k;
    ++i;
  }
  while (j < right_array_length) {
    array[k] = right_array[j];
    ++k;
    ++j;
  }
}

void merge_sort(double *array, size_t initial_index, size_t final_index) {
  if (initial_index < final_index) {
    size_t middle_index = (initial_index + final_index) / 2;
    merge_sort(array, initial_index, middle_index);
    merge_sort(array, middle_index+1, final_index);
    merge(array, initial_index, middle_index, final_index);
  }
}

void print_array_d(double *array, size_t length) {
  for (size_t i = 0; i < length; ++i) {
    if (i != 0) {
      if (i != length - 1) {
        printf("%f, ", array[i]);
      }
      else printf("%f]", array[i]);
    }
    else {
      printf("[%f, ", array[i]);
    }
  }
}

bool is_sorted(double *array, size_t length) {
  for (size_t i = 0; i < length - 1; ++i) {
    if (array[i] > array[i+1]) {
      return false;
    }
  }
  return true;
}

int main() {
  double A[6] = {3.5, 34.3, 13.4, 5.34, 19.3, 69.3};
  print_array_d(A, 6);
  merge_sort(A, 0, 5);
  printf("\n");
  print_array_d(A, 6);
  if (is_sorted(A, 6)) {
    printf("\nThe new array is sorted!");
  }
}

