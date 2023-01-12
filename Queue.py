#  John Daggs

#  10/1/2021

#  Purpose of Queue.py:
#  The purpose of this file is to contain a class named Queue.
#  This class will be designed and contain methods so that objects may be created from it and act in the nature of a
#  queue, where addition happens at one end (known as the rear), and removal happens at the other end (the front).
#  Data items move through a queue first-in first-out (a.k.a FIFO), in which the first added item will be removed first.

#  collaborators/resources -
#  Class Notes/Powerpoint on Stack/Queue/Deque


class Queue(object):

    def __init__(self):               # the class constructor
        self.queue = []               # initializing the list queue

    def enqueue(self, item):          # adds item to the rear of the queue
        self.queue.insert(0, item)    # inserting the item at index zero (the rear) of the queue

    def dequeue(self):                # removes and returns the item at the front of the queue
        if self.is_empty():           # checking if the queue is empty
            return None               # returning None if the queue is empty
        else:                         # else (if the queue is not empty)
            return self.queue.pop()   # popping, returning the item at the front of the queue (at the end of the list)

    def is_empty(self):               # returns True if the queue is empty, False otherwise
        if len(self.queue) > 0:       # checking if length of the queue is greater than zero to check if its is empty
            return False              # returning False (that it is not empty) if the length is greater than zero
        else:                         # else (if the length was not greater than zero)
            return True               # returning True (that it is empty) if the length was not greater than zero

    def size(self):                   # returns the number of items in the queue
        return len(self.queue)        # returning the length of the queue as the size
