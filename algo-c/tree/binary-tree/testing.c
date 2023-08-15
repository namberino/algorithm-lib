#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int value;

struct node
{
    int value;
    struct node *left, *right;
};

struct node* newNode(int item);
struct node* insert(struct node* node, int value);
struct node* search(struct node* node, int value);
int findMax(struct node* node);
int findMin(struct node* node);

int main()
{
    struct node* root = newNode(8);
    insert(root, 1);
	insert(root, 3);
	insert(root, 4);
	insert(root, 6);
	insert(root, 7);
	insert(root, 10);
	insert(root, 14);
	insert(root, 17);

    value = 6;

    printf("Searching for value: %d\n\n", value);

    if (search(root, value) == NULL)
        printf("%d not found\n\n", value);
    else
        printf("%d found\n\n", value);

    value = 50;

    printf("Searching for value: %d\n\n", value);

    if (search(root, value) == NULL)
        printf("%d not found\n", value);
    else
        printf("%d found\n\n", value);

    printf("Max: %d\n", findMax(root));
    printf("Min: %d\n", findMin(root));

    return 0;
}

struct node* newNode(int item)
{
    struct node* rtnNode = malloc(sizeof(struct node));
    rtnNode -> value = item;
    rtnNode -> left = rtnNode -> right = NULL;
}

struct node* insert(struct node* node, int value)
{
    if (node == NULL)
        return newNode(value);

    if (value < node -> value)
        node -> left = insert(node -> left, value);

    if (value > node -> value)
        node -> right = insert(node -> right, value);

    return node;
}

struct node* search(struct node* node, int value)
{
    if (node == NULL || node -> value == value)
    {
        if (node == NULL)
            printf("Returning a null node\n\n");
        else
            printf("Found %d, returning node\n\n", node -> value);
        return node;
    }

    if (value > node -> value)
    {
        printf("Checking %d\n", node -> value);
        return search(node -> right, value);
    }

    printf("Checking %d\n", node -> value);
    return search(node -> left, value);
}
