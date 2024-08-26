from Styling import *
import time
import os

class Static_Stack:
    def __init__(self, size = 6):
        self.top = -1
        self.stack = [None]*size

    def push(self, value):
        if self.is_full():
            return

        self.top += 1
        self.stack[self.top] = value       
    
    def pop(self):
        ret = self.stack[self.top]
        self.top -= 1
        return ret 

    def peek(self):
        return self.stack[self.top]

    def size(self):
        return self.top+1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top == len(self.stack)-1:
            return True
        else:
            return False            

    def display(self, String):
        print(f"{String}", end="\t| ")

        if self.is_empty():
            print("empty |")
            return None

        for i in range(0, self.top+1):   
            print(self.stack[i], end=" | ")

################################################################
def Main_SA():
    ss = Static_Stack()
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
        Heading("Page", "Stack Implementation By Array")

        ss.display("Stack: ")
        print("\n\nCHOOSE ANY OPTION TO PROCEED\n")
        print("\t1| PUSH")
        print("\t2| POP \n")
        print("\t3| SIZE")
        if detail == 3:
            print("\t  > Size of stack is: ", ss.size())
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
                        case1 = False     
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
