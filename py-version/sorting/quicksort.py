def partition(array, low, high):
    pivot = array[high];
    i = low - 1;

    for j in range(low, high):
        if (array[j] <= pivot):
            i += 1;

            array[i], array[j] = array[j], array[i];
    
    array[i + 1], array[high] = array[high], array[i + 1];

    # print(array);

    return i + 1;

def quickSort(array, low, high):
    if (low <= high):
        pivotIndex = partition(array, low, high);

        quickSort(array, low, pivotIndex - 1);
        quickSort(array, pivotIndex + 1, high);


array = [1, 9, 2, 8, 3, 6, 5, 7, 4];
print(array);
quickSort(array, 0, len(array) - 1);
print(array);
