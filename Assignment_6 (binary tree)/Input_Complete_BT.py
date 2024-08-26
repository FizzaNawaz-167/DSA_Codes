from Styling import *

class TreeNode:
    def __init__(self, info):
        self.left = None
        self.info = info
        self.right = None

def Get_CompleteBT(self, array, size):
    root = self
    count = -1
    global get_parent
    index = 0
    array = array

    for i in range(0, len(array)):
        if self is not None:
            if i > 0:
                ReturnNode(root, array[i])
                self = get_parent 

            count += 1
            if count == size-1:
                break 

            index = 2*(i+1)
            array[index-1] = input(f"\nEnter left element of {self.info}: ")
            if index <= len(array):
                self.left = TreeNode(array[index-1])

            count += 1
            if count == size-1:
                break

            index = 2*(i+1) + 1
            array[index-1] = input(f"Enter right element of {self.info}: ")
            if index <= len(array):
                self.right = TreeNode(array[index-1])
               

def ArrayRep(self):
    global count
    global length
    global repArr
    index = 0
    i = 0

    if self is not None:
        for i in range(0, length):
            if self.info == repArr[i]:
                i = i+1
                break

        if self.left:
            index = 2*(i)
            repArr[index-1] = self.left.info

        if self.right:
            index = 2*(i) + 1
            repArr[index-1] = self.right.info   

        ArrayRep(self.left)
        ArrayRep(self.right)

def ReturnNode(self, target):
    global get_parent

    if self is not None:
        if self.info == target:
            get_parent = self
            return
        ReturnNode(self.left, target)       
        ReturnNode(self.right, target)

def pre_order(self):
    stack = [0]*20
    Top = 1
    stack[Top] = None

    while self is not None:
        if self.info is None:
            print(end='')
        else:
            print(self.info, end=' - ')

        if self.right:
            Top += 1
            stack[Top] = self.right
        if self.left:
            self = self.left
        else:
            self = stack[Top] 
            Top -= 1

def in_order(self):
    stack = [0]*20
    Top = 1
    stack[Top] = None

    while self is not None:
        Top += 1
        stack[Top] = self
        self = self.left

    self = stack[Top]
    Top -= 1

    while self is not None:
        if self.info is None:
            print(end='')
        else:
            print(self.info, end=' - ')
        if self.right:
            self = self.right
            in_order(self)
        self = stack[Top]
        Top -= 1  

def post_order(self):
    stack=[]
    stack.append(self)
    global prev
    
    while self is not None:
        
        if self.right is not None and self.right.info is not None and self.right.info[0] != '-':
            self.right.info = '-' + self.right.info
            stack.append(self.right)
        elif self.left is not None:
            stack.append(self.left)
            self=self.left
        elif self.left is None:
            break   

    element = stack.pop()
    while True:
        if element.info is not None and element.info[0] != '-':
            if element.info[0] != prev:
                print(element.info, end=' - ')
                prev = element.info
        elif element.info is not None and element.info[0] == '-':
            element.info = element.info[1]
            stack.append(element)
            post_order(element)
    
        if len(stack)==0:
            break        
        element=stack.pop() 

def MainICBT():
    getin = True
    global length
    global repArr
  
    store_sz = 0
    Heading("Page", "Complete Binary Tree")
    if not getin:
        choose = int(input("Re-Enter The Tree(0) or Use Previous One(1): "))
        getin = True if choose == 0 else False
    if getin:
        print("\nENTER SOME VALUES TO GET THE IMPLEMENTATION OF COMPLETE BINARY TREE:")         
        size = int(input("Number of nodes: "))

        if size < 2:
            store_sz = 2
        elif size < 4:
            store_sz = 4
        elif size < 8:
            store_sz = 8
        elif size < 16:
            store_sz = 16
        elif size < 32:
            store_sz = 32

        array = [None]*store_sz
        length = len(array)

        array[0] = input("Enter root info: ")   
                    
        GET = TreeNode(array[0])
        Get_CompleteBT(GET, array, size) 
        repArr = array
        getin = False

    caseBT = True
    caseBTT = True

    while caseBT:
        Heading("Page", "Complete Binary Tree")
        print("ARRAY REPRESENTATION:",end="\n\t| ")

        ArrayRep(GET)

        for J in range(0, length):
            if repArr[J] == None:
                repArr[J] = ' '
            print(repArr[J], end=' | ')
        
        print("\n\nFOLLOWING ARE THE POSSIBLE TRAVERSALS FOR TREE\n")
        print("\t1| PRE-ORDER")
        print("\t2| IN-ORDER")
        print("\t3| POST-ORDER") 
        print("\n\t0| Back")
        print("\t9| Refresh")

        let = int(input("\n\n\n-> enter "))
        caseBTT = False if let == 0 else True

        while caseBTT:
            
            Heading("Page", "Complete Binary Tree")
            print("ARRAY REPRESENTATION",end="\n\t| ")
            ArrayRep(GET)

            for J in range(0, length):
                if repArr[J] == None:
                    repArr[J] = ' '
                print(repArr[J], end=' | ')

            print("\n\nFOLLOWING ARE THE POSSIBLE TRAVERSALS FOR TREE\n")
            print("\t1| PRE-ORDER")
            if let == 1:
                print('',end='\t\t')
                pre_order(GET)
                print()

            print("\t2| IN-ORDER")
            if let == 2:
                print('',end='\t\t')
                in_order(GET)
                print()

            print("\t3| POST-ORDER") 
            if let == 3:
                print('',end='\t\t')
                post_order(GET)
                print()

            print("\n\t0| Back")
            print("\t9| Refresh")

            let = int(input("\n\n\n-> enter "))
            caseBTT = False if let == 9 or let == 0 else True

        caseBT = False if let == 0 else True

length = 8
prev = ''    
count = -1
repArr = [None]*50