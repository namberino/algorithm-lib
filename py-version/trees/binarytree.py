class Node:
    def __init__(self, key):
        self.left = None;
        self.right = None;
        self.val = key;

    def traversePreOrder(self):
        print(self.val, end=' ');
        if self.left:
            self.left.traversePreOrder();
        if self.right:
            self.right.traversePreOrder();

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder();
        print(self.val, end=' ');
        if self.right:
            self.right.traverseInOrder();

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder();
        if self.right:
            self.right.traversePostOrder();
        print(self.val, end=' ');


root = Node(15);

root.left = Node(8);

root.left.left = Node(77);
root.left.left.right = Node(35);

root.left.right = Node(41);
root.left.right.right = Node(24);
root.left.right.right.left = Node(68);
root.left.right.right.left.right = Node(99);

print("PreOrder Traversal: ", end="");
root.traversePreOrder();

print("\nInOrder Traversal: ", end="");
root.traverseInOrder();

print("\nPostOrder Traversal: ", end="");
root.traversePostOrder();

print();
