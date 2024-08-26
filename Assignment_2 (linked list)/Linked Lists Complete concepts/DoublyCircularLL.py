from Styling import *

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def Append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = self.head
            self.head.prev = new_node

    def Insert(self, data, location):
        new_node = Node(data)
        cur = self.head
        position = 0
        isInserted = False
        
        if self.head is None or location == 1:
            self.Prepend(data) 
            isInserted = True   
        else:
            while cur.next != self.head:
                position = position+1
                if position == location:
                    new_node.next = cur
                    new_node.prev = cur.prev
                    cur.prev.next = new_node
                    cur.prev = new_node
                    isInserted = True
                    break
                cur = cur.next

        if location == position+1:
            new_node.next = cur
            new_node.prev = cur.prev
            cur.prev.next = new_node
            cur.prev = new_node
            isInserted = True
        elif location == position+2:
            self.Append(data)
            isInserted = True

        if isInserted == False:
            print(f"The position {location} is out of bound...")
        else:
            self.print_list(f"\nList After inserting {data} at position {location}: \n\t")
            
    def Prepend(self, data):
        new_node = Node(data)
        cur = self.head 

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            while cur.next != self.head:    
                cur = cur.next
            new_node.next = self.head
            new_node.prev = cur
            self.head.prev = new_node
            cur.next = new_node
            self.head = new_node

    def DeleteFromStart(self):
        isDeleted = True

        if self.head is None:
            print("\n\nNothing to delete")
            isDeleted = False
        elif self.head.next == self.head:
            self.head = None
            print("\n\nThe only element deleted")
            isDeleted = False
        else:
            last_node = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next
            self.head.prev = last_node

        return isDeleted    

    def DeleteFromEnd(self):
        isDeleted = True

        if self.head is None:
            print("\n\nNothing to delete")
            isDeleted = False
        elif self.head.next == self.head:
            self.head = None
            print("\n\nThe only element deleted")
            isDeleted = False
        else:
            cur = self.head
            while cur.next != self.head:
                if cur.next.next == self.head:
                    cur.next.next.prev = cur
                    cur.next = self.head
                    break            
                else:
                    cur = cur.next

        return isDeleted            

    def DeleteElement(self, data):
        isDeleted = False

        if self.head is None or self.head.next is None:
            isDeleted = False if self.head is None else True
            self.DeleteFromStart()
            return

        current = self.head
        while True:
            if current.data == data:
                if current.next == current:  
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                    if current == self.head:
                        self.head = current.next
                isDeleted = True

            current = current.next
            if current == self.head:
                break          

        if not isDeleted:
            print(f"\nThe element {data} is not found in the list...")
        else:
            self.print_list(f"\nList After deleting {data}: \n\t")                               

    def Search(self, data):
        cur = self.head
        position = 0
        isFound = False

        while cur.next != self.head: 
            position = position+1 

            if cur.data == data:
                print(f"\nElement {data} is present at position {position} ")
                isFound = True    
            cur = cur.next
            
        if not isFound:
            print(f"\n\nElement {data} is not present in the list...")      

    def Copy(self):
        new_list = DoublyCircularLinkedList()
        cur = self.head
        while cur:
            new_list.Append(cur.data)
            cur = cur.next
            if cur == self.head:
                break

        return new_list

    def show(self, value, string):
        print(f"{string}",end = "")
        cur = value
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
            if cur == value:
                break

    def print_list(self, String):
        print(F"{String}", end="")
        
        if not self.head:
            print("\tempty", end="")
            return

        cur = self.head
        while True:
            print(cur.data, end=" -> ")
            cur = cur.next

            if cur == self.head:
                break    
########################################################################################### CLASS DoublyCircularLinkelist ###########

class Sorting:
    def BubbleSort(self, head):
        swap = True

        while swap:
            swap = False
            cur0 = head
            while cur0.next != head:
                if cur0.data > cur0.next.data:
                    cur0.data, cur0.next.data = cur0.next.data, cur0.data
                    swap = True
                cur0 = cur0.next

    def SelectionSort(self, head):
        cur = head

        while True:
            min_value = cur
            cur0 = cur.next

            while cur0 != head:
                if min_value.data > cur0.data:
                    min_value = cur0
                cur0 = cur0.next

            cur.data, min_value.data = min_value.data, cur.data    
            cur = cur.next 
            if cur == head:
                break   

    def InsertionSort(self, head):
        pass

######################### MAIN FUNCTION STARTS HERE
def mainDCLL():

    list = DoublyCircularLinkedList()
    list.Append(8)
    list.Prepend(6)
    list.Append(7)
    list.Append(1)
    list.Prepend(2)

    repeat = True
    while repeat:
        case1 = True
        case2 = True
        case3 = True
        case4 = True

        x()
        Heading("PAGE", "DOUBLY_CIRCULAR LINKED LIST")
        print("CHOOSE ANY OPERATION TO PERFORM ON LINKED DOUBLY_CIRCULAR LINKED LIST.\n")
        print("\t1 | INSERTION")
        print("\t2 | DELETION")
        print("\t3 | SORTING")
        print("\t4 | SEARCHING")
        print("\n\t0 | BACK TO MAIN")

        switch = int(input("\n\n=> enter: "))
        match switch:
            case 1:
                while case1:
                    x()
                    Heading("OPERATION", "INSERTION")
                    list.print_list("The List: ")
                    print("\n\nSELECT ANY ONE OPTION.")
                    print("\n\t1 | Insert At Start")
                    print("\t2 | Insert At End")
                    print("\t3 | Insert At Any Position")
                    print("\n\t0 | BACK")

                    choose = int(input("\n\n=> enter: "))
                    
                    x()
                    match choose:
                        case 1:
                            Heading("OPERATION", "Insert At Start")
                            list.print_list("The List: ")
                            element = int(input("\n\nEnter element to Prepend: "))
                            list.Prepend(element) 
                            list.print_list(f"\nList After Prepending {element}: \n\t")

                        case 2:
                            Heading("OPERATION", "Insert At End")
                            list.print_list("The List: ")
                            element = int(input("\n\nEnter element to Append: "))
                            list.Append(element) 
                            list.print_list(f"\nList After Appending {element}: \n\t")

                        case 3:
                            Heading("OPERATION", "Insert At Any Position")
                            list.print_list("The List: ")
                            element = int(input("\n\n\nEnter element to Insert: "))
                            location = int(input("Enter the position: "))
                            list.Insert(element, location) 
                        case 0:
                            break

                    Options()
                    let = int(input("\n\n=> enter: "))
                    case1 = True if let == 1 else False 

            #######################################################################################################
            case 2:
                while case2:
                    x()
                    Heading("OPERATION", "DELETION")
                    list.print_list("The List: ")
                    print("\n\nSELECT ANY ONE OPTION.")
                    print("\n\t1 | Delete From Start")
                    print("\t2 | Delete From End")
                    print("\t3 | Delete From Any Position")
                    print("\n\t0 | BACK")

                    choose = int(input("\n\n=> enter: "))
                    
                    x()
                    match choose:
                        case 1:
                            Heading("OPERATION", " Delete From Start")
                            list.print_list("The List: ")
                            true = list.DeleteFromStart()
                            if true:
                                list.print_list("\n\nList After deleting first element: \n\t")   
                        case 2:
                            Heading("OPERATION", " Delete From End")
                            list.print_list("The List: ")
                            true = list.DeleteFromEnd() 
                            if true:
                                list.print_list("\n\nList After deleting last element: \n\t") 
                        case 3:
                            Heading("OPERATION", " Delete From Any Position")
                            list.print_list("The List: ")
                            element = int(input("\n\nEnter element to delete: "))
                            list.DeleteElement(element)                         
                        case 0:
                            break

                    Options()
                    let = int(input("\n\n=> enter: "))
                    case2 = True if let == 1 else False 

            #######################################################################################################
            case 3:
                while case3:
                    sorting = Sorting()
                    x()
                    Heading("OPERATION", "SORTING")
                    list.print_list("The List: ")
                    print("\n\nSELECT ANY ONE OPTION.")
                    print("\n\t1 | Bubble Sort")
                    print("\t2 | Selection Sort")
                    print("\t3 | Insertion Sort")
                    print("\n\t0 | BACK")

                    choose = int(input("\n\n=> enter: "))
                    
                    x()
                    match choose:
                        case 1:
                            Heading("OPERATION", "Bubble Sorting")
                            list.print_list("The List: ")
                            cur = list.Copy()
                            sorting.BubbleSort(cur.head)
                            list.show(cur.head ,"\n\nSorted list:\n\t")
                        case 2:
                            Heading("OPERATION", "Selection Sorting")
                            list.print_list("The List: ")
                            cur = list.Copy()
                            sorting.SelectionSort(cur.head)
                            list.show(cur.head ,"\n\nSorted list:\n\t")
                        case 3:
                            Heading("OPERATION", "Insertion Sorting")
                            list.print_list("The List: ")
                            cur = list.Copy()
                            retValue = sorting.InsertionSort(cur.head)
                            list.show(retValue ,"\n\nSorted list:\n\t")
                        case 0:
                            break

                    Options()
                    let = int(input("\n\n=> enter: "))
                    case3 = True if let == 1 else False 

            #######################################################################################################
            case 4:
                while case4:
                    x()
                    Heading("OPERATION", "SORTING")
                    list.print_list("The List: ")
                    
                    element = int(input("\n\nEnter element to search: "))
                    list.Search(element)
                    
                    Options()
                    let = int(input("\n\n=> enter: "))
                    case4 = True if let == 1 else False 

            #######################################################################################################    
            case 0:
                x()

        repeat =  False if switch == 0 else True

mainDCLL()