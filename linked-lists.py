"""
Created on Thu Nov 26 08:33:03 2020

@author: chaitanya
"""

class node:
    
    def __init__(self,value):
        self.value = value
        self.next = None #Default value of the next node
        
class linked_list:
    
    def __init__(self):
        self.head = None #Default value of the linked list head
        
        
    def append(self, new_val):
        new_node = node(new_val) #Create a new node with the corresponding value
        
        if self.head == None:
            self.head = new_node #Initalise current node as the head if head is not present
            return
            
        prev = self.head #Put the pointer on the head
        
        while (prev.next != None):
            prev = prev.next
        
        prev.next = new_node
        
    
    def sort(self, new_node):
        #This function sorts the nodes in the linked list in ascending order
        
        #Empty linked list
        if self.head == None:
            new_node.next = self.head
            self.head = new_node  
        
        #If the head is at the end of the list...
        elif self.head.value >= new_node.value:
            new_node.next = self.head
            self.head = new_node
        
        else:
            curr = self.head #Initialise the pointer to head
            while (curr.next is not None and curr.next.value < new_node.value):
                curr = curr.next #Shift pointer to next node
            new_node.next = curr.next
            curr.next = new_node
    
    #Remove all occurences of a particular key in the linked list
    def remove(self,key):
        
        pointer = self.head
        prev_node = None
        
        while(pointer != None and pointer.value == key):
            self.head = pointer.next
            pointer = self.head
            
        while (pointer != None):
            
            while(pointer != None and pointer.value != key):
                prev_node = pointer
                pointer = pointer.next
                
            if (pointer == None):
                return 
            
            prev_node.next = pointer.next #Remove the node with the required key value
            pointer = prev_node.next
        
        return 
            
        
    def display_list (self):
        curr = self.head #Put the pointer on the head intially...
        
        while (curr != None):
            print(curr.value)
            curr = curr.next #Shift pointer to next node

    
        
    
