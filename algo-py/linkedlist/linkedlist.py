class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
    
    def printList(self):
        printval = self.head;

        while (printval is not None):
            print(printval.data);
            printval = printval.next;


linkedList = LinkedList();

linkedList.head = Node(1);
second = Node(2);
third = Node(3);

linkedList.head.next = second;
second.next = third;

linkedList.printList();
