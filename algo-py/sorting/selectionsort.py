def selectionSort(array):
    for i in range(len(array)):
        minIndex = i;

        for j in range(i + 1, len(array)):
            if (array[j] < array[minIndex]):
                minIndex = j;

        if (minIndex != i):
            array[minIndex], array[i] = array[i], array[minIndex];
    

array = [1, 9, 2, 4, 3, 6, 5, 7, 8];
print(array);
selectionSort(array);
print(array);
