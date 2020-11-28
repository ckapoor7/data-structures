#Implementation of a queue as an array
class queue:
    
    def __init__ (self,num_elements):
        self.num_elements = num_elements
        self.head = self.size = 0 
        self.tail = self.size-1
        self.q = [None]*num_elements #initialise an empty queue of the given size
      
    #This function checks if the queue is full or not
    def is_full(self):
        if self.size == self.num_elements:
            return True
    
    #This function checks if the queue is empty or not
    def is_empty(self):
        if self.num_elements == 0:
            return True
        
    #This function adds(ie-enqueues) a specified
    def enq(self,value):
        if not self.is_full:
            self.tail = (self.tail+1)%(self.num_elements)
            self.q[self.tail] = value
            self.size += 1
    
    #This function removes(ie-dequeues) the first element enqued(FIFO)
    def dq(self):
        if not self.is_empty:
            self.head = (self.head+1)%(self.num_elements)
            self.size -= 1
    
    def display(self):
            for i in range(self.tail):
                print(self.q[i])
        
