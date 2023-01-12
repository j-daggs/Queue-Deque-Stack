#  John Daggs

#  10/1/2021

#  Purpose of Stack.py:
#  The purpose of this file is to contain a class named Stack.
#  This class will be designed and contain methods so that objects may be created from it and act in the nature of a
#  stack, in which the addition and removal of items always happens at the same end – known as the top of the stack
#  The data items in a stack act in a last-in first-out (LIFO) manner
#  , where the most recently added item is the item that is removed first.

#  collaborators/resources -
#  Class Notes/Powerpoint on Stack/Queue/Deque


class Stack(object):
    def __init__(self):                             # the class constructor
        self.stack = []                             # initializing the list stack

    def push(self, item):                           # adds item to top of the stack, should push/pop from end of list
        #                                             (more efficient at end for stack)
        self.stack.append(item)      # appending to the end of the stack

    def pop(self):                                  # removes and returns the top item on the stack
        if self.is_empty():                         # checking if stack is empty
            return None                             # returning None if stack is empty
        else:                                       # else (if the stack is not empty)
            return self.stack.pop()                 # popping from the end of the stack

    def peek(self):                                 # returns the top item on the stack, but does not remove it
        if self.is_empty():                         # checking if the stack is empty
            return None                             # returning None if stack is empty
        else:                                       # else (if stack is not empty)
            return self.stack[len(self.stack) - 1]  # returning the top value - at the end of stack (index = length -1)

    def is_empty(self):                             # returns True if the stack is empty, False otherwise
        if len(self.stack) > 0:                     # checking if length of stack is greater than zero, see if is empty
            return False                            # returning False (it is not empty) if length is greater than zero
        else:                                       # else (if the length was not greater than zero)
            return True                             # returning True (it is empty) if length is not greater than zero

    def size(self):                                 # returns the number of items on the stack
        return len(self.stack)                      # returning the length of the stack as the size
