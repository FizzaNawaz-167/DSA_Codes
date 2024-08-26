from Styling import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#######################
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def Append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node    
            new_node.next = None

    def Insert(self, data, location):
        new_node = Node(data)
        cur = self.head
        position = 1
        isInserted = False

        if self.head is None or location == 1:
            self.Prepend(data) 
            isInserted = True    
        else:
            while cur:
                position = position+1
                if position == location:
                    new_node.next = cur.next
                    cur.next = new_node
                    isInserted = True
                    break
                cur = cur.next

        if not isInserted:
            print(f"The position {location} is out of bound...")
        else:
            self.Display(f"\nList After inserting {data} at position {location}: \n\t")

    def Prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def DeleteFromStart(self):
        isDeleted = True

        if self.head is None:
            print("\n\nNothing to delete")
            isDeleted = False
        elif self.head.next is None:
            self.head = None
            print("\n\nThe only element deleted")
            isDeleted = False
        else:
            self.head = self.head.next

        return isDeleted 

    def DeleteFromEnd(self):
        isDeleted = True

        if self.head is None:
            print("\n\nNothing to delete")
            isDeleted = False
        elif self.head.next is None:
            self.head = None
            print("\n\nThe only element deleted")
            isDeleted = False
        else:
            cur = self.head
            while self.head:
                if cur.next.next == None:
                    cur.next = None
                    break            
                else:
                    cur = cur.next 

        return isDeleted

    def DeleteElement(self, data):
        cur = self.head
        isDeleted = False

        if self.head is None or self.head.next is None:
            isDeleted = False if self.head is None else True
            self.DeleteFromStart()
        else:  
            if data == self.head.data:
                self.DeleteFromStart()
                isDeleted = True

            while cur.next:                     # notice the logic
                if cur.next.data == data:
                    cur.next = cur.next.next
                    isDeleted = True
                else:    
                    cur = cur.next

        if not isDeleted:
            print(f"\nThe element {data} is not found in the list...")
        else:
            self.Display(f"\nList After deleting {data}: \n\t")                

    def Search(self, data):
        cur = self.head
        position = 0
        isFound = False

        while cur.next: 
            position = position+1 
            if cur.data == data:
                print(f"\nElement {data} is present at position {position} ")
                isFound = True    
            cur = cur.next

        if cur.data == data:
            print(f"\nElement {data} is present at position {position+1} ")
            isFound = True

        if not isFound:
            print(f"\n\nElement {data} is not present in the list...")      

    def Copy(self):
        new_list = SinglyLinkedList()
        cur = self.head
        while cur:
            new_list.Append(cur.data)
            cur = cur.next

        return new_list

    def show(self, val,  string):
        print(f"{string}",end = "")
        cur = val
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next    

    def Display(self, string):
        print(f"{string}",end = "")

        if not self.head:
            print("\empty", end="")
            return

        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
########################################################################################### CLASS SinglyLinkedList ###########
##############
class Sorting:
    def BubbleSort(self, head):
        swap = True

        while swap:
            swap = False
            cur0 = head
            while cur0.next:
                if cur0.data > cur0.next.data:
                    cur0.data, cur0.next.data = cur0.next.data, cur0.data
                    swap = True
                cur0 = cur0.next
   
    def SelectionSort(self, head):
        cur = head

        while cur:
            min_value = cur
            cur0 = cur.next

            while cur0:
                if min_value.data > cur0.data:
                    min_value = cur0
                cur0 = cur0.next

            cur.data, min_value.data = min_value.data, cur.data    
            cur = cur.next   

    def InsertionSort(self, head):
        new = SinglyLinkedList()

        if not head or not head.next:
            return head

        copy = Node(0) 
        copy.next = head
        cur = head
        while cur.next:
            if cur.next.data < cur.data:
                temp = cur.next
                cur.next = cur.next.next
                prev = copy
                while prev.next.data < temp.data:
                    prev = prev.next
                temp.next = prev.next
                prev.next = temp
            else:
                cur = cur.next

        return copy.next    
########################################################################################### CLASS SORTING ############

######################### MAIN FUNCTION STARTS HERE
def mainSLL():     
    list = SinglyLinkedList()
    list.Append(10)
    list.Append(25)
    list.Prepend(12)
    list.Prepend(23)
    list.Append(11)

    repeat = True
    while repeat:
        case1 = True
        case2 = True
        case3 = True
        case4 = True

        x()
        Heading("PAGE", "SINGLY LINKED LIST")
        print("CHOOSE ANY OPERATION TO PERFORM ON SINGLY LINKED LIST.\n")
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
                    list.Display("The List: ")
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
                            list.Display("The List: ")
                            element = int(input("\n\nEnter element to Prepend: "))
                            list.Prepend(element) 
                            list.Display(f"\nList After Prepending {element}: \n\t")

                        case 2:
                            Heading("OPERATION", "Insert At End")
                            list.Display("The List: ")
                            element = int(input("\n\nEnter element to Append: "))
                            list.Append(element) 
                            list.Display(f"\nList After Appending {element}: \n\t")

                        case 3:
                            Heading("OPERATION", "Insert At Any Position")
                            list.Display("The List: ")
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
                    list.Display("The List: ")
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
                            list.Display("The List: ")
                            true = list.DeleteFromStart()
                            if true:
                                list.Display("\n\nList After deleting first element: \n\t")   
                        case 2:
                            Heading("OPERATION", " Delete From End")
                            list.Display("The List: ")
                            true = list.DeleteFromEnd() 
                            if true:
                                list.Display("\n\nList After deleting last element: \n\t")
                        case 3:
                            Heading("OPERATION", " Delete From Any Position")
                            list.Display("The List: ")
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
                    list.Display("The List: ")
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
                            list.Display("The List: ")
                            cur = list.Copy()
                            sorting.BubbleSort(cur.head)
                            list.show(cur.head ,"\n\nSorted list:\n\t")
                        case 2:
                            Heading("OPERATION", "Selection Sorting")
                            list.Display("The List: ")
                            cur = list.Copy()
                            sorting.SelectionSort(cur.head)
                            list.show(cur.head ,"\n\nSorted list:\n\t")
                        case 3:
                            Heading("OPERATION", "Insertion Sorting")
                            list.Display("The List: ")
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
                    list.Display("The List: ")
                    
                    element = int(input("\n\nEnter element to search: "))
                    list.Search(element)
                    
                    Options()
                    let = int(input("\n\n=> enter: "))
                    case4 = True if let == 1 else False 
            #######################################################################################################    
            case 0:
                x()

        repeat =  False if switch == 0 else True

mainSLL()