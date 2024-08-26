import os
import time
from Styling import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_LinkedList:
    def __init__(self):
        self.head = None
        self.top = -1

    def Enqueue(self, data):
        if self.is_full():
            print("Queue is full, can't enqueue")
            time.sleep(2)
            return 

        new_node = Node(data)
        cur = self.head

        if self.head is None:
            self.head = new_node
            new_node.next = None
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.next = None
            self.top = new_node

    def Dequeue(self):
        if self.is_empty():
            print("Queue is null, can't dequeue")
            time.sleep(2)
            return

        if self.head.next == None:
            self.head = None
            return

        ret = self.head
        self.head = self.head.next

        return ret

    def peek(self):
        if self.head == None:
            return None

        return self.top.data

    def size(self):
        if self.head == None:
            return 0

        i = 0
        cur = self.head
        while cur: 
            i += 1           
            cur = cur.next
        return i    

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def is_full(self):
        if self.size() == 6:
            return True
        else:
            return False 
    
    def Display(self, String):
        cur = self.head
        print(f"{String}", end="\t")

        if self.is_empty():
            print("empty ")
            return None

        if self.head is None:
            return None
        else: 
            while cur:
                print(f"{cur.data}" , end = " -> ")
                cur = cur.next

################################################################
def Main_QL():
    q = Queue_LinkedList()
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)
    q.Enqueue(4)

    repeat = True
    detail = 0

    while(repeat):
        case1 = True
        case2 = True

        os.system('cls')
        Heading("Page", "Queue Implementation By Array")

        q.Display("Queue: ")
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
            print("\t  > Queue empty: ", q.is_empty())
        print("\t6| FULL")
        if detail == 6:
            print("\t  > Queue full: ", q.is_full())
        print("\n\n0| Back")
        print("9| Main")
        detail = 0

        switch = int(input("\n\n=> enter: "))
        match switch:
            case 1:
                while case1:
                    os.system('cls')
                    Heading("OPERATION", "ENQUEUE")
                    q.Display("Queue: ")

                    print("\n\n\t1 - Enqueue")
                    print("\t0 - Back")
                    
                    let = int(input("\n\nenter... "))

                    if let == 1 and not q.is_full():
                        element = int(input("Enter element to enqueue: "))
                        q.Enqueue(element)
                        print(f"Pushed {element} to stack.")
                        time.sleep(1)
                    elif let == 1 and q.is_full():
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
                    q.Display("Queue: ")

                    print("\n\n\t1 - Dequeue")
                    print("\t0 - Back")
                    
                    let = int(input("\n\nenter... "))

                    if let == 1 and not q.is_empty():
                        value = q.Dequeue()
                        print(f"Poped {value} from stack.")
                        time.sleep(1)
                    elif let == 1 and q.is_empty():
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