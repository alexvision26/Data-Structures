"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

import sys
from singly_linked_list import LinkedList

class Queue:
    def __init__(self): #initialize the Queue class that will manage the values of the head (first item in the queue) tail (newest or latest item added to the queue)
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self): #override the len function to return the size of the queue instantiated in the class
        return self.size

    def is_empty(self): #checks the current length of the queue. This value is changed when elements or queued or dequeued
        return self.size == 0

    def enqueue(self, element): 
        self.storage.add_to_tail(element)
        self.size += 1 

    def dequeue(self):
        if self.is_empty(): #checks if queue is empty, if it is, this function will not be able to dequeue anything
            return None
        result = self.storage.remove_head()
        self.size -= 1 #it will account for the dequeued element
        return result
