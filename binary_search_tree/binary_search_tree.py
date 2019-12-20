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
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
                return
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True
        else:
            if target > self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False
            else:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False
            
    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # cb(self.value)
        # if self.right:
        #     self.right.for_each(cb)
        # if self.left:
        #     self.left.for_each(cb)
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            cb(current_node.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #Recursive
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            current_node = stack.pop()
            if current_node.left is None and current_node.right is None:
                print(current_node.value)
            else:
                if current_node.left is None:
                    print(current_node.value)
                else:
                    current_node.dft_print(current_node.left)

                if current_node.right:
                    current_node.dft_print(current_node.right)
        
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        while queue.size > 0:
            current_value = queue.dequeue()
            print(current_value.value)
            if current_value.left:
                queue.enqueue(current_value.left)
            if current_value.right:
                queue.enqueue(current_value.right)
        #make a queue
        #put root in queue
        #while queue > 0
            #pop out front of queue
            #callBack
            #if left add to queue
            # if right add to queue



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # iterative
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)
        
        #Recursive
        # stack = Stack()
        # stack.push(node)
        # while stack.len() > 0:
        #     print(stack.pop().value)
        #     if node.right:
        #         node.dft_print(node.right)
        #     if node.left:
        #         node.dft_print(node.left)

        #steps
        # Make a stack
        # put the root node in the stack
        # #while stack not empty
        # pop the root out of stack
        # callBack
        # if right add right to stack
        # if left add left to stack






            

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
