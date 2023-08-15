#include <stdio.h>
#include <stdlib.h>

void insertionSort(int array[]);

int main()
{
	int array[] = {42, 23, 74, 11, 65, 58, 94, 36, 99, 87};
	
	printf("Unsorted: ");
	for (int i = 0; i < 9; i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n");

	insertionSort(array);

	printf("Sorted: ");
	for (int i = 0; i < 9; i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n");

	return 0;
}

void insertionSort(int array[])
{
	size_t arrayLength = (int) sizeof(array) / sizeof(array[0]);

	for (int i = 1; i < arrayLength; i++)
	{
		int key = array[i];
		int j = i - 1;

		while (j >= 0 && key < array[j])
		{
			array[j + 1] = array[j];
			j -= 1;
		}

		array[j + 1] = key;
	}
}
