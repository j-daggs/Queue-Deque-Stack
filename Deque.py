#  John Daggs

#  10/1/2021

#  Purpose of Deque.py:
#  The purpose of this file is to contain a class named Deque.
#  This class will be designed and contain methods so that objects may be created from it and act in the nature of a
#  deque, in which addition and removal can occur at both ends, essentially combining the
#  abilities of a stack and a queue

#  collaborators/resources -
#  Class Notes/Powerpoint on Stack/Queue/Deque


class Deque(object):

    def __init__(self):               # the class constructor
        self.deque = []               # initializing the list deque

    def add_front(self, item):        # adds item to the front of the deque
        self.deque.insert(0, item)    # inserting item at front of deque at index 0

    def add_rear(self, item):         # adds item to the rear of the deque
        self.deque.append(item)       # appending item to the rear (default) of deque at end of list

    def remove_front(self):           # removes and returns the item at the front of the deque
        if self.is_empty():           # checking if the deque is empty
            return None               # if deque is empty, return None b/c there is nothing to remove
        else:                         # else (if deque is not empty)
            return self.deque.pop(0)  # popping and returning the item at index 0 of the deck to remove front

    def remove_rear(self):            # removes and returns the item at the rear of the deque
        if self.is_empty():           # checking if the deque is empty
            return None               # if deque is empty, return None b/c there is nothing to remove
        else:                         # else (if deque is not empty)
            return self.deque.pop()   # popping, returning item at end of deque (default) of the deck to remove front

    def is_empty(self):               # returns True if the deque is empty, False otherwise
        if len(self.deque) > 0:       # checking if length of the deque is greater than zero to check if its is empty
            return False              # returning False (that it is not empty) if the length is greater than zero
        else:                         # else (if the length was not greater than zero)
            return True               # returning true (that it is empty) if the length was not greater than zero

    def size(self):                   # returns the number of items in the deque
        return len(self.deque)        # returning the length of the deque as the size
