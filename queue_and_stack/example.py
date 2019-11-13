"""Reverse a Single Linked List"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
class SL:
    def __init__(self,head=None):
        self.head = head

    def add(self, value):
        current_next = Node(value)
        current_next.next = self.head
        self.head = current_next

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        
        
sl = SL()
sl.add(1)
sl.add(2)
sl.add(3)
sl.add(4)
sl.add(5)

sl.print_list()
sl.reverse()
sl.print_list()

        
