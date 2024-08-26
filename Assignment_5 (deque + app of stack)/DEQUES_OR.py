import os
import time

class Queue:
    def __init__(self):
        self.size = 5
        self.queue = [None]*self.size     #list(range(self.size))
        self.i = 0
        self.o = 0
        self.i_left = 0
        self.is_empty = True
        self.is_full = False

    def _increment(self, value):
        if (value + 1) == self.size:
            return 0
        else:
            return (value + 1)

    def _decrement(self, value):
        if (value - 1) == -1:
            return 0
        else:
            return (value - 1)               

    def  enqueueRight(self, value):
        if self.is_full:
            print("Queue is full, can't enqueue")
            time.sleep(2)
            return 

        self.o = self._decrement(self.o)
        self.i = self.o

        self.queue[self.i] = value
        self.i = self._decrement(self.i)

        if self.i == self.o:
            self.is_full = True

        self.is_empty = False         

    def  enqueueLeft(self, value):
        if self.is_full:
            print("Queue is full, can't enqueue")
            time.sleep(2)
            return

        self.queue[self.i_left] = value
        self.i_left = self._increment(self.i_left)

        if self.i_left == self.o:
            self.is_full = True

        self.is_empty = False 
    
    def dequeue(self):
        if self.is_empty:
            print("Queue is null, can't dequeue")
            time.sleep(2)
            return

        self.o = self.i
        self.i = self._increment(self.i)
        
        var = self.queue[self.o]
        self.queue[self.o] = None
        self.o = self._increment(self.o)

        if self.i_left == self.o == self.i or self.i_left == self.i:
            self.is_empty = True

        self.is_full = False
        return var

def DEQUES_OR():
    q = Queue()
    q.enqueueLeft(1)
    q.enqueueLeft(2)
    q.enqueueLeft(3)
    q.enqueueLeft(4)
    q.enqueueLeft(5)

    repeat = True
    while repeat:
        os.system('cls')
        print("\nOUTPUT RESTRICTED DEQUE:\n")
        print(q.queue)
        print("\n1 | enqueue front")
        print("2 | enqueue rare")
        print("3 | dequeue ")

        choose = int(input("\n\n\nenter => "))

        match choose:
            case 1:
                data = int(input("value to enter: "))
                q.enqueueRight(data)            
            case 2:
                data = int(input("value to enter: "))
                q.enqueueLeft(data)
            case 3:
                q.dequeue()
            case 0:
                repeat = False 
