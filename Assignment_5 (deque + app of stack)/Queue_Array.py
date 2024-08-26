import os
import time
from Styling import *

class Queue:
    def __init__(self):
        self.Size = 5
        self.queue = [None]*self.Size
        self.i = 0
        self.o = 0
        self.is_empty = True
        self.is_full = False

    def _increment(self, value):
        if (value + 1) == self.Size:
            return 0
        else:
            return (value + 1)               

    def  enqueue(self, value):
        if self.full():
            return 

        self.queue[self.i] = value
        self.i = self._increment(self.i)

        if self.i == self.o:
            self.is_full = True

        self.is_empty = False   

    def dequeue(self):
        if self.empty():
            return 

        var = self.queue[self.o]
        self.queue[self.o] = None
        self.o = self._increment(self.o)

        if self.i == self.o:
            self.is_empty = True

        self.is_full = False
        return var

    def empty(self):
        if self.is_empty == True:
            return True
        else:
            return False 

    def full(self):
        if self.is_full == True:
            return True
        else:
            return False              

    def peek(self):
        value = self.queue[self.i-1] 
        return value

    def size(self):
        sz = self.i - self.o
        return sz   
################################################################
def Main_QA():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    repeat = True
    detail = 0

    while(repeat):
        case1 = True
        case2 = True

        os.system('cls')
        Heading("Page", "Queue Implementation By Array")

        print("Queue: ", q.queue)
        print("\n\nCHOOSE ANY OPTION TO PROCEED\n")
        print("\t1| ENQUEUE")
        print("\t2| DEQUEUE \n")
        print("\t3| SIZE")
        if detail == 3:
            print("\t  > Size of Queue is: ", q.size())
        print("\t4| PEEK")
        if detail == 4:
            print("\t  > Peek element of Queue is: ", q.peek())
        print("\t5| EMPTY")
        if detail == 5:
            print("\t  > Queue empty: ", q.empty())
        print("\t6| FULL")
        if detail == 6:
            print("\t  > Queue full: ", q.full())
        print("\n\n0| Back")
        print("9| Main")
        detail = 0

        switch = int(input("\n\n=> enter: "))
        match switch:
            case 1:
                while case1:
                    os.system('cls')
                    Heading("OPERATION", "ENQUEUE")
                    print("Queue: ", q.queue)

                    print("\n\n\t1 - Enqueue")
                    print("\t0 - Back")
                    
                    let = int(input("\n\nenter... "))

                    if let == 1 and not q.full():
                        element = int(input("Enter element to enqueue: "))
                        q.enqueue(element)
                        print(f"Pushed {element} to stack.")
                        time.sleep(1)
                    elif let == 1 and q.full():
                        print("Stack is full, can't push...")
                        time.sleep(2)
                        case1 = False  

                    if let == 0:
                        case1 = False         
            #######################################################################################################
            case 2:
                while case2:
                    os.system('cls')
                    Heading("OPERATION", "DEQUEUE")
                    print("Queue: ", q.queue)

                    print("\n\n\t1 - Dequeue")
                    print("\t0 - Back")
                    
                    let = int(input("\n\nenter... "))

                    if let == 1 and not q.empty():
                        value = q.dequeue()
                        print(f"Poped {value} from stack.")
                        time.sleep(1)
                    elif let == 1 and q.empty():
                        print("Stack is null, can't pop...")
                        time.sleep(2)
                        case2 = False 

                    if let == 0:
                        case2 = False     
            #######################################################################################################
            case 3:
                detail = switch
            #######################################################################################################
            case 4:
                detail = switch
            #######################################################################################################
            case 5:
                detail = switch
            #######################################################################################################
            case 6:
                detail = switch
            #######################################################################################################
            case 0:
                x()
            case 9:
                return 9    

        repeat =  False if switch == 0 else True   
               