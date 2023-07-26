#include <stdio.h>

void insertionSort(int array[]);

int main()
{
	int array[] = {1, 9, 2, 4, 3, 6, 5, 7, 8};
	
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
	int arrayLength = (int) sizeof(array) / sizeof(array[0]);

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
