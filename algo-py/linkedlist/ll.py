class Node:
    def __init__(self, key, info) -> None:
        self.key = key;
        self.info = info;
        self.next = None;

class LinkedList:
    def __init__(self) -> None:
        self.head = None;

    def search(self, value):
        p = self.head;

        while (p is not None):
            if (p.key == value):
                print("The student that has a GPA of %d is: %s" % (value, p.info));
                break;
            p = p.next

linkedList = LinkedList();

linkedList.head = Node(7.5, "bit1234");
second = Node(8.3, "bit2345");
third = Node(7.6, "bit3456");
fourth = Node(9, "bit4567");
fifth = Node(9.5, "bit5678");

linkedList.head.next = second;
second.next = third;
third.next = fourth;
fourth.next = fifth;

linkedList.search(9);
