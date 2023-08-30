#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int value;

struct node 
{
    int value;
    struct node *left, *right;
};

// A utility function to create a new BST node
struct node* newnode(int item)
{
	struct node* rtnnode = malloc(sizeof(struct node));
	rtnnode -> value = item;
	rtnnode -> left = rtnnode -> right = NULL;
	return rtnnode;
}

// A utility function to insert a new node with given value in BST
struct node* insert(struct node* node, int value)
{
	// If the tree is empty, return a new node
	if (node == NULL)
	    return newnode(value);

	// Otherwise, recur down the tree
	if (value < node -> value)
		node -> left = insert(node -> left, value);
	else if (value > node -> value)
		node -> right = insert(node -> right, value);

	// Return the (unchanged) node pointer
	return node;
}

// Utility function to search a value in a BST
struct node* search(struct node* node, int value)
{
	// Base Cases: tree is empty or value is present at node
	if (node == NULL || node -> value == value)
    {
        if (node == NULL)
            printf("Returning a null node\n\n");
        else
            printf("Found %d, returning node\n\n", node -> value);

		return node;
    }

	// Value is greater than node's value
	if (node -> value < value)
    {
        printf("Checking %d\n", node -> value);
		return search(node -> right, value);
    }

	// Value is smaller than root's value
    printf("Checking %d\n", node -> value);
	return search(node -> left, value);
}

int findMax(struct node* node)
{
    // Base case
    if (node == NULL)
        return INT_MIN;
 
    // Return maximum of 3 values: root's data, max in left subtree, max in right subtree
    int res = node -> value;
    int lres = findMax(node -> left);
    int rres = findMax(node -> right);

    if (lres > res)
        res = lres;
    if (rres > res)
        res = rres;

    return res;
}

int findMin(struct node* node)
{
    // Base case
    if (node == NULL)
        return INT_MAX;
 
    // Return minimum of 3 values: root's data, min in left subtree, min in right subtree
    int res = node -> value;
    int lres = findMin(node -> left);
    int rres = findMin(node -> right);

    if (lres < res)
        res = lres;
    if (rres < res)
        res = rres;

    return res;
}

struct node* delete(struct node* root, int delVal)
{
    // Base case
    if (root == NULL)
        return root;
 
    // Recursive calls for ancestors of node to be deleted
    if (root -> value > delVal) 
    {
        root -> left = delete(root -> left, delVal);
        return root;
    }
    else if (root -> value < delVal) 
    {
        root -> right = delete(root -> right, delVal);
        return root;
    }
 
    // Reach here when root is the node to be deleted.
 
    // If one of the children is empty
    if (root -> left == NULL) 
    {
        struct node* temp = root -> right;
        free(root);
        return temp;
    }
    else if (root -> right == NULL) 
    {
        struct node* temp = root -> left;
        free(root);
        return temp;
    }
    else // If both children exist
    {
        struct node* succParent = root;
 
        // Find successor
        struct node* succ = root -> right;
        while (succ -> left != NULL) 
        {
            succParent = succ;
            succ = succ -> left;
        }
 
        // Delete successor.  Since successor is always left child of its parent we can safely make successor's right
        // child as left of its parent. If there is no succ, then assign succ -> right to succParent -> right
        if (succParent != root)
            succParent -> left = succ -> right;
        else
            succParent -> right = succ -> right;
 
        // Copy Successor Data to root
        root -> value = succ -> value;
 
        // Delete Successor and return root
        free(succ);
        return root;
    }
}

int main()
{
	struct node* root = newnode(8);
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

	value = 60;

    printf("Searching for value: %d\n\n", value);
	if (search(root, value) == NULL)
		printf("%d not found\n\n", value);
	else
		printf("%d found\n\n", value);

    printf("Max: %d\n", findMax(root));
    printf("Min: %d\n", findMin(root));

    value = 10;

    printf("\nDeleting %d\n\n", value);
    delete(root, value);

    printf("Searching for value: %d\n\n", value);
	if (search(root, value) == NULL)
		printf("%d not found\n", value);
	else
		printf("%d found\n", value);
    

	return 0;
}
