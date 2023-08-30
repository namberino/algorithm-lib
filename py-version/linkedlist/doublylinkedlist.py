class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        self.prev = None;

class DoublyLinkedList:
    def __init__(self):
        self.head = None;

    def push(self, newData):
        newNode = Node(newData);
        newNode.next = self.head;

        if (self.head is not None):
            self.head.prev = newNode;

        self.head = newNode;

    def bottomIterate(self):
        print("Checking from bottom up");
        
        currentNode = self.head;
        while (currentNode.next is not None):
            currentNode = currentNode.next;

        while (currentNode is not None):
            print("Checked %i" % currentNode.data);
            currentNode = currentNode.prev;

    def remove(self, value):
        currentNode = self.head;
        while (currentNode is not None):
            if (currentNode.data == value):
                if (currentNode.prev is not None and currentNode.next is not None):
                    currentNode.prev.next = currentNode.next;
                    currentNode.next.prev = currentNode.prev;
                else:
                    self.head = currentNode.next;
                
                break;

            currentNode = currentNode.next;


doublyLinkedList = DoublyLinkedList();
doublyLinkedList.push(1);
doublyLinkedList.push(2);
doublyLinkedList.push(3);
doublyLinkedList.push(4);
doublyLinkedList.push(5);
doublyLinkedList.bottomIterate();
doublyLinkedList.remove(3);
doublyLinkedList.bottomIterate();
