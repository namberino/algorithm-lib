#include <stdio.h>
#include <string.h>

void sort(int array[], int size);

int main() {
    int arr[] = {5, 7, 3, 4, 2, 1, 6, 9, 8};
    int size = sizeof(arr) / sizeof(arr[0]); // size is 7

    sort(arr, size);

    for (int i = 0; i < size; i++) {
        printf("%i\n", arr[i]);
    }

    return 0;
}

void sort(int array[], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}