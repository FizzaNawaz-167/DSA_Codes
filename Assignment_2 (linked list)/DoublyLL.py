from Styling import *

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

######################
class DoublyLinkedlist:
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
            new_node.prev = cur
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
                    new_node.prev = cur
                    new_node.next = cur.next
                    cur.next = new_node
                    cur.next.prev = new_node
                    isInserted = True
                    break
                cur = cur.next

        if location == position+1:
            self.Append(data)
            isInserted = True            

        if isInserted == False:
            print(f"\nThe position {location} is out of bound...")
        else:
            self.print_list(f"\nList After inserting {data} at position {location}: \n\t")
            
    def Prepend(self, data):
        new_node = Node(data)
        
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def updatePosition(self, location, data):
        cur = self.head
        isUpdated = False
        position = 0

        while cur:
            position += 1
            if position == location:
                cur.data = data
                isUpdated = True
                break
            cur = cur.next    

        if not isUpdated:
            print(f"\nThe position {location} don't exists...")
        else:
            print(f"\nSuccessfully updated {data} at position {location}.")             
        

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
            self.head.prev = None

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

    def DeletePositon(self, location):
        Deleted = False
        position = 0

        if self.head is None or self.head.next is None:
            self.DeleteFromStart()
            Deleted = False if self.head is None else True
            data = cur.data
            return

        cur = self.head
        while cur:
            position = position + 1
            if position == location:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next

                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                
                Deleted =  True
                data = cur.data
                break

            cur = cur.next

        if not Deleted:
            print(f"\nThe position {location} is out of bound...")
        else:
            self.print_list(f"\nList After deleting {data} from location {location}: \n\t")
       

    def DeleteElement(self, data):
        isDeleted = False

        if self.head is None or self.head.next is None:
            isDeleted = False if self.head is None else True
            self.DeleteFromStart()
            return

        cur = self.head
        while cur:
            if cur.data == data:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next

                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                
                isDeleted =  True    
            cur = cur.next          

        if not isDeleted:
            print(f"\nThe element {data} is not found in the list...")
        else:
            self.print_list(f"\nList After deleting {data}: \n\t")                

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

    def print_list(self, String):
        print(f"{String}", end = "")

        if not self.head:
            print("\tempty", end="")
            return

        cur = self.head
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.next

    def print_list_reverse(self, String):
        print(f"{String}", end = "")

        if not self.head:
            print("\tempty", end="")
            return

        cur = self.head
        while cur.next:
                cur = cur.next

        while cur: 
                print(cur.data, end=" <-> ")
                cur = cur.prev

########################################################################################### CLASS DoublyLinkelist ###########
 
######################### MAIN FUNCTION STARTS HERE
def mainDLL():
        
    list = DoublyLinkedlist()
    list.Append(12)
    list.Prepend(9)
    list.Append(3)
    list.Append(1)
    list.Append(2)


    repeat = True
    while repeat:
        case1 = True
        case2 = True
        case3 = True
        go_to_main = False

        x()
        Heading("PAGE", "DOUBLY LINKED LIST")
        print("CHOOSE ANY OPERATION TO PERFORM ON LINKED DOUBLY LINKED LIST.\n")
        print("\t1 | INSERTION")
        print("\t2 | DELETION")
        print("\t3 | SEARCHING")
        print("\n\t0 | BACK TO MAIN")

        switch = int(input("\n\n=> enter: "))
        match switch:
            case 1:
                while case1:
                    x()
                    Heading("OPERATION", "INSERTION")
                    list.print_list("The List: \n\tFarward: ")
                    list.print_list_reverse("\n\tReversed: ")
                    print("\n\nSELECT ANY ONE OPTION.")
                    print("\n\t1 | Insert At Start")
                    print("\t2 | Insert At End")
                    print("\t3 | Insert At Any Position")
                    print("\t4 | Update Position")
                    print("\n\t0 | BACK")
                    print("\t9 | MAIN")

                    choose = int(input("\n\n=> enter: "))
                    
                    x()
                    match choose:
                        case 1:
                            Heading("OPERATION", "Insert At Start")
                            list.print_list("The List: \n\tFarward: ")
                            list.print_list_reverse("\n\tReversed: ")
                            element = int(input("\n\nEnter element to Prepend: "))
                            list.Prepend(element) 
                            list.print_list(f"\nList After Prepending {element}: \n\t")

                        case 2:
                            Heading("OPERATION", "Insert At End")
                            list.print_list("The List: \n\tFarward: ")
                            list.print_list_reverse("\n\tReversed: ")
                            element = int(input("\n\nEnter element to Append: "))
                            list.Append(element) 
                            list.print_list(f"\nList After Aing {element}: \n\t")

                        case 3:
                            Heading("OPERATION", "Insert Any At Any Position")
                            list.print_list("The List: \n\tFarward: ")
                            list.print_list_reverse("\n\tReversed: ")
                            element = int(input("\n\n\nEnter element to Insert: "))
                            location = int(input("Enter the position: "))
                            list.Insert(element, location) 

                        case 4:
                            Heading("OPERATION", "Update The Position")
                            list.print_list("The List:\n\tFarward: ")
                            list.print_list_reverse("\n\tReversed: ")
                            position = int(input("\n\n\nEnter the position: "))
                            element = int(input("Enter element to update: "))
                            list.updatePosition(position, element) 
                            list.print_list(f"\nList After updating position {position}: \n\t")
                                
                        case 0:
                            break

                        case 9:
                            go_to_main = True
                            break    

                    Options()
                    let = int(input("\n\n=> enter: "))
                    if let == 9:
                        go_to_main = True

                    case1 = True if let == 1 else False 

            #######################################################################################################
            case 2:
                while case2:
                    x()
                    Heading("OPERATION", "DELETION")
                    list.print_list("The List: \n\tFarward: ")
                    list.print_list_reverse("\n\tReversed: ")
                    print("\n\nSELECT ANY ONE OPTION.")
                    print("\n\t1 | Delete From Start")
                    print("\t2 | Delete From End")
                    print("\t  | DELETE ANY ELEMENT THROUGHT:")
                    print("\t3 | Data")
                    print("\t4 | Position")
                    print("\n\t0 | BACK")
                    print("\t9 | MAIN")

                    choose = int(input("\n\n=> enter: "))
                    
                    x()
                    match choose:
                        case 1:
                            Heading("OPERATION", " Delete From Start")
                            list.print_list("The List: \n\tFarward: ")
                            list.print_list_reverse("\n\tReversed: ")
                            true = list.DeleteFromStart()
                            if true:
                                list.print_list("\n\nList After deleting first element: \n\t")   
                        case 2:
                            Heading("OPERATION", " Delete From End")
                            list.print_list("The List: \n\tFarward: ")
                            list.print_list_reverse("\n\tReversed: ")
                            true = list.DeleteFromEnd() 
                            if true:
                                list.print_list("\n\nList After deleting last element: \n\t") 
                        case 3:
                            Heading("OPERATION", " Delete Any Element")
                            list.print_list("The List: \n\tFarward: ")
                            list.print_list_reverse("\n\tReversed: ")
                            element = int(input("\n\nEnter element to delete: "))
                            list.DeleteElement(element)
                        case 4:
                            Heading("OPERATION", " Delete From Any Position")
                            list.print_list("The List: \n\tFarward: ")
                            list.print_list_reverse("\n\tReversed: ")
                            element = int(input("\n\nEnter position to delete: "))
                            list.DeletePositon(element)
                        case 0:
                            break

                        case 9:
                            go_to_main = True
                            break    

                    Options()
                    let = int(input("\n\n=> enter: "))
                    if let == 9:
                        go_to_main = True

                    case2 = True if let == 1 else False 

            #######################################################################################################
            case 3:
                while case3:
                    x()
                    Heading("OPERATION", "SORTING")
                    list.print_list("The List: \n\tFarward: ")
                    list.print_list_reverse("\n\tReversed: ")
                    
                    element = int(input("\n\nEnter element to search: "))
                    list.Search(element)
                    
                    Options()
                    let = int(input("\n\n=> enter: "))
                    if let == 9:
                        go_to_main = True

                    case3 = True if let == 1 else False 

            #######################################################################################################    
            case 0:
                x()

        repeat =  False if (switch == 0 or go_to_main == True ) else True
