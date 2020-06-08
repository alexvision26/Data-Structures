"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Stack:
    class Node:
        def __init__(self, element, _next): #instantiate the node class that will navigate the data structure of the stack
            self.element = element
            self._next = _next

    def __init__(self): #initialioze the stack class
        self.head = None
        self.size = 0

    def __len__(self): #this method overrides the len function to just simple return the size accounted for by the stack class
        return self.size

    def is_empty(self): #method checks if the stack is empty
        return self.size == 0

    def push(self, element): #method pushes on the new element to the stack based on the input
        self.head = self.Node(element, self.head)
        self.size += 1 #adds to the size counter every time this method is called, or any element is added to the stack

    def pop(self):
        if self.is_empty(): #if the stack is empty, there is nothing to pop
            return None
        result = self.head.element #sets the first element of the stack to be removed to the result
        self.head = self.head._next #sets up the next element in the stack after the result is popped
        self.size -= 1 #accounts for the update in the stack size
        return result #returns the result

    def top(self): #this method returns the top element in the stack (or the last)
        if self.is_empty():
            return None
        return self.head.element
