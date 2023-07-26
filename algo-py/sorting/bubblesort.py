# time complexity: O(n^2) (worst case) and O(n) (best case)
def bubbleSort(array):
    if (len(array) > 1 and array != None):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if (array[j] > array[j + 1]):
                    array[j], array[j + 1] = array[j + 1], array[j];

    return array



array = [1, 9, 2, 4, 3, 6, 5, 7, 8];
bubbleSort(array);
print(array);
