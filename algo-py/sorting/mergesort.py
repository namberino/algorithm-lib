# time complexity: O(n * log(n)) (for all cases)
def mergeSort(array):
    if (len(array) > 1 and array != None):
        mid = len(array) // 2;

        left = array[:mid];
        right = array[mid:];

        mergeSort(left);
        mergeSort(right);

        i = j = k = 0;

        while (i < len(left) and j < len(right)):
            if left[i] <= right[j]:
                array[k] = left[i];
                i += 1;
            else:
                array[k] = right[j];
                j += 1;
            k += 1;

        while (i < len(left)):
            array[k] = left[i];
            i += 1;
            k += 1;

        while (j < len(right)):
            array[k] = right[j];
            j += 1;
            k += 1;


array = [1, 9, 2, 8, 3, 6, 5, 7, 4];
print(array);
mergeSort(array);
print(array);
