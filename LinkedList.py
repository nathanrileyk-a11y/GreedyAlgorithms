class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.hashmap = {}

    def insert_beginning(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            self.tail = new

        else:
        
            self.head.prev = new
            new.next = self.head
            self.head = new

        self.hashmap[data] = new

    def insert_end(self, data):
        new = Node(data)
        if not self.tail:
            self.tail = new
            self.head = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

        self.hashmap[data] = new
    
    def delete(self, data):
        
        N = self.find(data)
        
        if N == self.head and N == self.tail:
            self.head = None
            self.tail = None
            
        elif N == self.head:
            self.head = N.next
            self.head.prev = None
        elif N == self.tail:
            self.tail = N.prev
            self.tail.next = None
        else:
            prev = N.prev
            next = N.next 
            prev.next = next
            next.prev = prev
        del self.hashmap[data]

    def find(self, data):
        return self.hashmap[data]
    

    