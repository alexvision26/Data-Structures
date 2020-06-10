"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        new_node.prev = None
        new_node.next = self.head
        if not self.is_empty():
            curr = self.head
            curr.prev = new_node
            new_node.insert_before(curr)
        self.head = new_node
        if not self.tail:
            self.tail= new_node
            self.head.next = self.tail
            self.tail.prev = self.head
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head == self.tail:
            a_val = self.head.value
            self.tail = None
            self.head = None
            self.length = 0
            return a_val
        else:
            b_val = self.head.value
            self.delete(self.head)
            self.length -= 1
            return b_val


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            curr_tail = self.tail
            curr_tail.next = new_node
            new_node.prev = curr_tail
            self.tail = new_node
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.head is self.tail:
            a_val = self.head.value
            self.tail = None
            self.head = None
            self.length -= 1
            return a_val
        else:
            b_val = self.tail.value
            self.tail.delete()
            self.length -= 1
            return b_val

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        node.prev = None
        node.next = self.head
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.is_empty():
            return None
        if self.head is self.tail:
            return None
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
        curr_tail = self.tail
        curr_tail.next = node
        node.prev = curr_tail
        self.tail = node



    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return None
        if self.head is self.tail:
            self.head = self.tail = None
        if node is self.head:
            self.head = node.next
            # self.head.prev = None
            node.delete()
        if node is self.tail:
            self.tail = node.prev
            # self.tail.next = None
            node.delete()
        else:
            node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
        if self.is_empty():
            return f"There is not elements inside this list!"
        printval = self.head
        nums = []
        while printval is not None:
            nums.append(printval.value)
            printval = printval.next
        value = max(nums)
        return value
