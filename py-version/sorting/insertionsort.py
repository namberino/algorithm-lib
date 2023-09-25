def insertionSort(array):
    for i in range(1, len(array)):
        j = i;

        while (array[j] < array[j - 1]):
            array[j], array[j - 1] = array[j - 1], array[j];
            j -= 1;

array = [1, 9, 2, 4, 3, 6, 5, 7, 8];
print(array);
insertionSort(array);
print(array);
