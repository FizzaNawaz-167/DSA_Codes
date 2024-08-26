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

        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node    
            new_node.next = self.head

    def Insert(self, data, location):
        new_node = Node(data)
        cur = self.head
        position = 1
        isInserted = False

        if self.head is None or location == 1:
            self.Prepend(data)   
            isInserted = True 
        else:
            while cur.next != self.head:
                position = position+1
                if position == location:
                    new_node.next = cur.next
                    cur.next = new_node
                    isInserted = True
                    break
                cur = cur.next

        if location == position+1:
            self.Append(data)
            isInserted = True        

        if isInserted == False:
            print(f"The position {location} is out of bound...")
        else:
            self.Display(f"\nList After inserting {data} at position {location}: \n\t")
            
    def Prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            new_node.next = self.head
            cur.next = new_node
            self.head = new_node

    def updatePosition(self, location, data):
        cur = self.head
        isUpdated = False
        position = 0

        while cur.next != self.head:
            position += 1
            if position == location:
                cur.data = data
                isUpdated = True
                break
            cur = cur.next  

        if cur.next == self.head:
            cur.data = data
            isUpdated = True     

        if not isUpdated:
            print(f"\nThe position {location} don't exists...")
        else:
            print(f"\nSuccessfully updated {data} at position {location}.")

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
            cur = self.head
            while cur:
                if cur.next == self.head:
                    self.head = self.head.next
                    cur.next = self.head
                    break            
                else:
                    cur = cur.next

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
            while self.head:
                if cur.next.next == self.head:
                    cur.next = self.head
                    break            
                else:
                    cur = cur.next

        return isDeleted          

    def DeletePositon(self, location):
        cur = self.head
        position = 1
        Deleted = False

        if self.head is None or location == 1:
            answer = self.DeleteFromStart() 
            data = cur.data
            Deleted = True if answer == True else False   
        else:
            while cur.next != self.head:
                position = position+1
                if position == location:
                    if cur.next == None:
                        break
                    data = cur.next.data     
                    cur.next = cur.next.next
                    Deleted = True
                    break
                cur = cur.next  

        if not Deleted:
            print(f"\nThe position {location} is out of bound...")
        else:
            self.Display(f"\nList After deleting {data} from location {location}: \n\t")

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

            while cur.next != self.head:                     
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

        while cur.next != self.head: 
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

    def Display(self, string):
        print(f"{string}", end = "")
        
        if not self.head:
            print("\tempty", end="")
            return

        cur = self.head
        while True:
            print(cur.data, end=" -> ")
            cur = cur.next

            if cur == self.head:
                break
########################################################################################### CLASS SinglyLinkedList ###########

######################### MAIN FUNCTION STARTS HERE
def mainSCLL():
        
    list = SinglyLinkedList()
    list.Append(3)
    list.Append(6)
    list.Append(1)
    list.Prepend(10)                    
    list.Append(14)

    repeat = True
    while repeat:
        case1 = True
        case2 = True
        case3 = True
        go_to_main = False

        x()
        Heading("PAGE", "SINGLY_CIRCULAR LINKED LIST")
        print("CHOOSE ANY OPERATION TO PERFORM ON LINKED SINGLY_CIRCULAR LINKED LIST.\n")
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
                    list.Display("The List: ")
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
                            list.Display("The List: ")
                            element = int(input("\n\nEnter element to Prepend: "))
                            list.Prepend(element) 
                            list.Display(f"\nList After Prepending {element}: \n\t")

                        case 2:
                            Heading("OPERATION", "Insert At End")
                            list.Display("The List: ")
                            element = int(input("\n\nEnter element to Append: "))
                            list.Append(element) 
                            list.Display(f"\nList After Aing {element}: \n\t")

                        case 3:
                            Heading("OPERATION", "Insert At Any Position")
                            list.Display("The List: ")
                            element = int(input("\n\n\nEnter element to Insert: "))
                            location = int(input("Enter the position: "))
                            list.Insert(element, location) 
                        
                        case 4:
                            Heading("OPERATION", "Update The Position")
                            list.Display("The List: ")
                            position = int(input("\n\n\nEnter the position: "))
                            element = int(input("Enter element to update: "))
                            list.updatePosition(position, element) 
                            list.Display(f"\nList After updating position {position}: \n\t")
                            
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
                    list.Display("The List: ")
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
                            Heading("OPERATION", " Delete Any Element")
                            list.Display("The List: ")
                            element = int(input("\n\nEnter element to delete: "))
                            list.DeleteElement(element)
                        case 4:
                            Heading("OPERATION", " Delete From Any Position")
                            list.Display("The List: ")
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
                    list.Display("The List: ")
                    
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
