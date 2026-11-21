class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, data):
        node = DoublyLinkedListNode(data)
        
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        
        self.tail = node
