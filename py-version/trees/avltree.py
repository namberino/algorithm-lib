from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        return 0 if not node else node.height

    def getBalanceFactor(self, node):
        return 0 if not node else (self.getHeight(node.left) - self.getHeight(node.right))

    def getMinNode(self, node):
        return node if not node or not node.left else self.getMinNode(node.left)

    def search(self, key):
        node = self.root

        while (node is not None and key != node.key):
            if (key < node.key):
                node = node.left
            else:
                node = node.right

        return node

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        bf = self.getBalanceFactor(root)

        if bf > 1 and key < root.left.key:
            return self.rightRotate(root)
        
        if bf < -1 and key > root.right.key:
            return self.leftRotate(root)
        
        if bf > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if bf < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.lefr
                root = None
                return temp
            
            # find successor
            temp = self.getMinNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        bf = self.getBalanceFactor(root)

        if bf > 1 and self.getBalanceFactor(root.left) >= 0:
            return self.rightRotate(root)
        
        if bf < -1 and self.getBalanceFactor(root.right) <= 0:
            return self.leftRotate(root)
        
        if bf > 1 and self.getBalanceFactor(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if bf < -1 and self.getBalanceFactor(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def leftRotate(self, node):
        B = node.right
        Y = B.left
        
        B.left = node
        node.right = Y
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        B.height = 1 + max(self.getHeight(B.left), self.getHeight(B.right))

        return B

    def rightRotate(self, node):
        A = node.left
        Y = A.right
        
        A.right = node
        node.left = Y
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        A.height = 1 + max(self.getHeight(A.left), self.getHeight(A.right))
        
        return A
    
    def minValue(self, root):
        current = root
    
        while(current.left is not None):
            current = current.left
    
        return current.key
    
    def maxValue(self, root):
        current = root
    
        while(current.right is not None):
            current = current.right
    
        return current.key
    
    def printTree(self):
        if self.root:
            queue = deque()
            queue.append(self.root)

            level_order = ''
            level_order_with_details = ''

            while(queue):
                node = queue.popleft()
                level_order += f'{node.key} '
                level_order_with_details += f'{node.key}: '.ljust(5) + f'h = {self.getHeight(node)}, bf = {self.getBalanceFactor(node)}\n'

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            print('\nLevel-order traversal:')
            print(level_order)
            print(f'\nLevel-order traversal with height and balance factor:') 
            print(level_order_with_details)
        else:
            print('\nAVL tree is empty!')

def printSearchResult(result):
    return result.key if result else 'not found'


avl = AVLTree()   
keys = [50, 25, 75, 15, 35, 60, 120, 10, 68, 90, 125, 83, 100]

for key in keys:
    avl.root = avl.insert(avl.root, key)

avl.printTree()

result = avl.minValue(avl.root)
print(f'Minimum value of tree: {result}')

result = avl.maxValue(avl.root)
print(f'Maximum value of tree: {result}')

result = avl.search(125)
print(f'Search for 125: {printSearchResult(result)}')

result = avl.search(1)
print(f'Search for 1: {printSearchResult(result)}')

avl.root = avl.delete(avl.root, 120)
print('\nAfter deleting 120:')
avl.printTree()

avl.root = avl.delete(avl.root, 10)
print('After deleting 10:')
avl.printTree()
