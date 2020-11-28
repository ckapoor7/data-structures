#Implementation of a stack using a linked list

import math

class node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

class stack:
    
    def __init__(self):
        self.head = None #Initialise an empty stack
    
    #Function to check for an empty stack
    def is_empty(self):
        return (self.head == None)
    
    #Function to push elements in the stack
    def push(self,value):
        if self.head == None: #If the stack is empty, then start from the head 
            self.head = node(value)
        
        else: #LIFO addition of elements to the stack
            new_val = node(value)
            new_val.next = self.head
            self.head = new_val
    
    #Function to pop elements from the stack (LIFO)
    def pop(self):
        if not self.is_empty():
            node_data = self.head
            self.head = self.head.next #Shift pointer to element after the head
            node_data.next = None
            return node_data.value
        else:
            print("Empty stack")
    
    
    #Function to find the minimum value in the stack
    def min_val(self):
        val = float(math.inf)
        
        while (self.head != None):
            if (val > self.head.value):
                val = self.head.value
            self.head = self.head.next #Shift pointer to the next element
        
        return val
            
    #Function to find the maximum value in the stack
    def max_val(self):
        val = float(-math.inf) #set maximum initially to a very large value
        
        while(self.head != None):
            if (val < self.head.value):
                val = self.head.value
            self.head = self.head.next
        
        return val
        
    
    #Displays all elements present in the stack
    def display_stack(self):
        pointer = self.head #Initialise the pointer to be at the head of the stakc
        
        if self.is_empty():
            print("Empty stack")
        
        else:
            while (pointer != None):
                print(pointer.value)
                pointer = pointer.next
                
            
