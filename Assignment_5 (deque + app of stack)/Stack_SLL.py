import os
import time
from Styling import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_LinkedList:
    def __init__(self):
        self.head = None
        self.top = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.top = new_node
        
        self.top.next = new_node
        self.top = new_node
            
    def pop(self):
        cur = self.head
        ret = self.top.data

        if self.head is None:
            return
        
        if cur == self.top:
            self.head = None
            self.top = None

        else:    
            while cur.next != self.top:
                cur = cur.next
        
            self.top = cur   
            cur.next = None

        return ret

    def peek(self):
        return self.top.data

    def size(self):
        i = 0
        cur = self.head
        while cur: 
            i += 1           
            cur = cur.next
        return i    

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def is_full(self):
        if self.size() == 7:
            return True
        else:
            return False 

    def display(self, String):
        print(f"{String}", end="\t")

        if self.head is None:
            print("empty")
            return None

        cur = self.head
        while cur:            
            print(cur.data , end = " -> ")
            cur = cur.next  

################################################################
def Main_SL():
    ss = Stack_LinkedList()
    ss.push(9)
    ss.push(5)
    ss.push(7)
    ss.push(1)

    repeat = True
    detail = 0

    while(repeat):
        case1 = True
        case2 = True

        os.system('cls')
        Heading("Page", "Stack Implementation By Linked List")

        ss.display("Stack: ")
        print("\n\nCHOOSE ANY OPTION TO PROCEED\n")
        print("\t1| PUSH")
        print("\t2| POP \n")
        print("\t3| SIZE")
        if detail == 3:
            print("\t  > Size of stack is: ", int(ss.size()))
        print("\t4| PEEK")
        if detail == 4:
            print("\t  > Peek element of stack is: ", ss.peek())
        print("\t5| EMPTY")
        if detail == 5:
            print("\t  > Stack empty: ", ss.is_empty())
        print("\t6| FULL")
        if detail == 6:
            print("\t  > Stack full: ", ss.is_full())
        print("\n\n0| Back")
        print("9| Main")
        detail = 0

        switch = int(input("\n\n=> enter: "))
        match switch:
            case 1:
                while case1:
                    os.system('cls')
                    Heading("OPERATION", "PUSH")
                    ss.display("Stack: ")

                    print("\n\n\n\t1 - Push")
                    print("\t0 - Back")
                    
                    let = int(input("\n\nenter... "))

                    if let == 1 and not ss.is_full():
                        element = int(input("Enter element to push: "))
                        ss.push(element)
                        print(f"Pushed {element} to stack.")
                        time.sleep(1)
                    elif let == 1 and ss.is_full():
                        print("Stack is full, can't push...")
                        time.sleep(2)
                        case1 = False

                    if let == 0:
                        case1 = False         
            #######################################################################################################
            case 2:
                while case2:
                    os.system('cls')
                    Heading("OPERATION", "POP")
                    ss.display("Stack: ")

                    print("\n\n\n\t1 - Pop")
                    print("\t0 - Back")
                    
                    let = int(input("\n\nenter... "))

                    if let == 1 and not ss.is_empty():
                        value = ss.pop()
                        print(f"Poped {value} from stack.")
                        time.sleep(1)
                    elif let == 1 and ss.is_empty():
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

               