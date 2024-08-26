import os
import time

class Queue:
    def __init__(self):
        self.size = 5
        self.queue = [None]*self.size     #list(range(self.size))
        self.i = 0
        self.o = 0
        self.o_right = 0
        self.is_empty = True
        self.is_full = False

    def _increment(self, value):
        if (value + 1) == self.size:
            return 0
        else:
            return (value + 1)

    def _decrement(self, value):
        if value == 0 or value == -5:
            self.i = 0
            return 0
        else:
            return (value-1)               

    def  enqueue(self, value):
        if self.is_full:
            print("Queue is full, can't enqueue")
            time.sleep(2)
            return 

        self.queue[self.i] = value
        self.i = self._increment(self.i)

        if self.i == self.o:
            self.is_full = True

        self.is_empty = False 

        # print(f"enqueue: i = {self.i}, o = {self.o}, o_right = {self.o_right}")    

    def dequeueLeft(self):
        if self.is_empty:
            print("Queue is null, can't dequeue")
            time.sleep(2)
            return

        var = self.queue[self.o]
        self.queue[self.o] = None
        self.o = self._increment(self.o)

        if self.i == self.o:
            self.is_empty = True

        self.is_full = False
        # print(f"dequeueFront= {self.i}, o = {self.o}, o_right = {self.o_right}")
        return var

    def dequeueRight(self):
        if self.is_empty:
            print("Queue is null, can't dequeue")
            time.sleep(2)
            return 

        self.i = self.i - 1
        self.o_right = self.i 

        var = self.queue[self.o_right]
        self.queue[self.o_right] = None
        self.o_right = self._decrement(self.o_right)

        if self.o_right == self.i == self.o_right:
            self.is_empty = True

        self.is_full = False
        # print(f"dequeueRare= {self.i}, o = {self.o}, o_right = {self.o_right}")   
        return var 

def DEQUES_IR():              
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    repeat = True
    while repeat:
        os.system('cls')
        print("\nINPUT RESTRICTED DEQUE:\n")
        print(q.queue)
        print("\n1 | enqueue")
        print("2 | dequeue front")
        print("3 | dequeue rare")

        choose = int(input("\n\n\nenter => "))

        match choose:
            case 1:
                data = int(input("value to enter: "))
                q.enqueue(data)
            case 2:
                q.dequeueLeft()
            case 3:
                q.dequeueRight()
            case 0:
                repeat = False            
