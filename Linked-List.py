class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """
        To add a node in the end of the linked list.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """
        To add a node in the start of the linked list.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get(self, index): 
        """
        To check value of a node on a specific index.
        """
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value): 
        """
        To change value of any node in the linkedlist.
        """
        temp = self.get(index)
        temp.value = value

    def pop(self):
       """
       Remove last node of the linkedlist.
       """ 
       if self.length == 0:
           return None
       if self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
       else:
            temp = self.head
            prev = self.head
            while (temp.next):
                prev = temp
                temp = temp.next
            prev.next = None
            self.length -= 1
            return temp


    def print_linkedlist(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next
