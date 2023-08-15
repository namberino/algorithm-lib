#include <stddef.h>
#include <stdio.h>

int linearsearch(int array[], int value, size_t length);
int binarysearch(int array[], int value, int low, int high);

int main()
{
    int array[] = {11, 23, 36, 42, 58, 65, 74, 87, 94};
    size_t length = sizeof(array) / sizeof(int);
    int value = 74;

	printf("Performing a linear search\n");
	int linVal = linearsearch(array, value, length);
	if (linVal != -1)
		printf("Element found at index: %d\n\n", linVal);
	else
		printf("Element not found\n\n");

	printf("Performing a binary search\n");
	int binVal = binarysearch(array, value, 0, length - 1);
	if (binVal != -1)
		printf("Element found at index: %d\n", binVal);
	else
		printf("Element not found\n");
	
	return 0;
}

int linearsearch(int array[], int value, size_t length)
{
	int count = 0;

	for (int i = 0; i < length; i++)
	{
		printf("Checking the %d element\n", i);
		if (array[i] == value)
			return count;

		count++;
	}
	return -1;
}

int binarysearch(int array[], int value, int low, int high)
{
    while (low <= high)
    {
        int mid = low + (high - 1) / 2;
        printf("Midpoint: %d\n", mid);

        if (value == array[mid])
            return mid;

        if (value > array[mid])
        {
            printf("Checking right half\n");
            low = mid + 1;
        }
        else
        {
            printf("Checking left half\n");
            high = mid - 1;
        }
    }

	return -1;
}
