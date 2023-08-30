class Node:
	# constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# A function that swap left node and right node of tree of every k'th level
def swapEveryKLevel(root, level, k):
	# Base Case
	if (root is None or (root.left is None and root.right is None)):
		return

	# If current level + 1 is present in swap vector then we swap left and right node
	if (level + 1) % k == 0:
		root.left, root.right = root.right, root.left
	
	# Recur for left and right subtree
	swapEveryKLevel(root.left, level + 1, k)
	swapEveryKLevel(root.right, level + 1, k)

# Method to find the inorder tree traversal
def inorder(root):
	
	# Base Case
	if root is None:
		return
	inorder(root.left)
	print(root.data,end=" ")
	inorder(root.right)

"""
	   1
      / \
     2	 3
    /	/ \
   4   7   8
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(8)
root.right.left = Node(7)

k = 2
print("Before swapping:")
inorder(root)

# swapEveryKLevel(root, k)
swapEveryKLevel(root, 1, k)

print ("\nAfter swapping: ")
inorder(root)

print()
