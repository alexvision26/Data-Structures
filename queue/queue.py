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
class Queue:
    class Node:
        def __init__(self, element, _next):
            # initiate the Node for the stack that will hold the current and next element
            self.element = element
            self._next = _next

    def __init__(self): #initialize the Queue class that will manage the values of the head (first item in the queue) tail (newest or latest item added to the queue)
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self): #override the len function to return the size of the queue instantiated in the class
        return self.size

    def is_empty(self): #checks the current length of the queue. This value is changed when elements or queued or dequeued
        return self.size == 0

    def enqueue(self, element): 
        new = self.Node(element, None) #creates a new element to be queued based in input value
        if self.is_empty(): #checks if queue is empty, if it is, it will set the head of the queue to the input element
            self.head = new
        else: #if queue has length, then it will add to the tail, (or the back of the queue)
            self.tail._next = new
        self.tail = new
        self.size += 1 

    def dequeue(self):
        if self.is_empty(): #checks if queue is empty, if it is, this function will not be able to dequeue anything
            return None
        result = self.head.element #if it has length, it will set the result of the first item to be dequeued
        self.head = self.head._next #then it will set the head as the following element after the result
        self.size -= 1 #it will account for the dequeued element
        if self.is_empty():  #if after dequeueing the element, the queue length is 0, it will set the tail to none and then return the current result, being the item dequeued
            self.tail = None
        return result

    def first(self): #this is a method that returns the first item in the queue
        if self.is_empty():
            return f"Queue is empty."
        return self.head.element
