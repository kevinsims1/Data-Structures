import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left == target:
                    return True
                else:
           
                    if self.left != None:
                        return self.left.contains(target)

            if target > self.value:
                if self.right == target:
                    return True
                else:
                    if self.right != None:
                        return self.right.contains(target)
            return False

            

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not self.left and self.right:
            print(self.value)

        if self.left:
            self.left.in_order_print(node)
            if self.right:
                print(self.value)
        
        if not self.right and self.left:
            print(self.value)
            

        if not self.left and not self.right:
            print(self.value)

        if self.right:
            self.right.in_order_print(node)
        
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        storage.enqueue(node)
        while storage.len() > 0:
            current = storage.dequeue()
            print(current.value)
            if current.left:
                storage.enqueue(current.left)
            if current.right:
                storage.enqueue(current.right)






    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()
        storage.push(node)
        while storage.len() > 0:
            current = storage.pop()
            print(current.value)
            if current.left:
                storage.push(current.left)
            if current.right:
                storage.push(current.right)
            

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
