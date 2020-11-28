#Implementation of a queue as a linked list

class node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        
class queue:
    
    def __init__(self):
        self.head = self.tail = 0
    
    
    #Check for an empty queue
    def is_empty(self):
        return self.head == None
    
    
    #Add (ie-enqueue) items to the queue 
    def enq(self,value):
        pointer = node(value)
        
        if self.tail == None:
            self.head = self.tail = pointer
        
        self.tail.next = pointer
        self.tail = pointer
    
    #Remove (ie-dequeue) items from the queue based on FIFO
    def dq(self):
        if not self.is_empty():
            pointer = self.head
            self.head = pointer.next
