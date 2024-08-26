from Styling import *
from CompleteBinaryTree import *
from Input_Complete_BT import *

class TreeNode:
    def __init__(self, parent, info):
        self.left = None
        self.parent = parent
        self.info = info
        self.right = None

def Length(self):
    global length
    global terminalFL

    if self is not None:
        if not self.left and not self.right:
            terminalFL += self.info

        Length(self.left)
        Length(self.right)

    for node in terminalFL:
        path = SearchPath(self, node)
        if path:
            if length < len(path):
                length = len(path)

def SearchPath(self, target):  
    if not self:
        return None

    if self.info == target:
        return [self.info]

    l_child = SearchPath(self.left, target)
    if l_child:
        return [self.info] + l_child

    R_child = SearchPath(self.right, target)
    if R_child:
        return [self.info] + R_child

    return None    

def ArrayRep_BT(self):
    global count
    global length
    global get_parent
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

        ArrayRep_BT(self.left)
        ArrayRep_BT(self.right)               

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
        if self.right is not None and self.right.info[0] != '-':
            self.right.info = '-' + self.right.info
            stack.append(self.right)
        elif self.left is not None:
            stack.append(self.left)
            self=self.left
        elif self.left is None:
            break   

    element = stack.pop()
    while True:
        if element.info[0] != '-':
            if element.info[0] != prev:
                print(element.info, end=' - ')
                prev = element.info
        elif element.info[0] == '-':
            element.info = element.info[1]
            stack.append(element)
            post_order(element)
    
        if len(stack)==0:
            break        
        element=stack.pop()    

def ReturnNode(self, target):
    global get_parent

    if self is not None:
        if self.info == target:
            get_parent = self
            return
        ReturnNode(self.left, target)       
        ReturnNode(self.right, target)

def InputTree(treeRoot):
    global SIZE
    repeatInput = True

    Heading("Operation","Enter The Tree")
    root = treeRoot

    while repeatInput:
        Heading("Operation","Enter The Tree")

        print("SPACE AVAILABLE:\n")
        terminal = []
        right = []
        left = []
        SpaceAvailable(treeRoot, terminal, right, left)
        print("Terminal Nodes: ", terminal) 
        print("Left Nodes Free: ", left)
        print("Right Nodes Free: ", right)

        parent = input("\nEnter parent: ")
        node = input("Enter the child: ")
        child_Position = input("Left-l or Right-r: ")

        ReturnNode(root, parent)
        self = get_parent

        if child_Position == 'l' or child_Position == 'L':
            if not self.left:
                self.left = TreeNode(parent, node)
                print("Inserted...")
                SIZE += 1
            elif self.left:
                print(f"\n> {self.info} has already a left child {self.left.info}\n")
               
        if child_Position == 'r' or child_Position == 'R':
            if not self.right:
                self.right = TreeNode(parent, node)
                print("Inserted...")
                SIZE += 1
            elif self.right:
                print(f"\n> {self.info} has already a right child {self.right.info}\n")    
    
        choice = int(input("\n=> Repeat-9 OR Exit-0 ... "))
        repeatInput = True if choice == 9 else False

def SpaceAvailable(self, terminal, right, left):

    if self is not None:
        if not self.left and not self.right:
            terminal += self.info
        elif self.left and not self.right:
            right += self.info
        elif self.right and not self.left:
            left += self.info 

        SpaceAvailable(self.left, terminal, right, left)
        SpaceAvailable(self.right, terminal, right, left)         

def Main():
    root = TreeNode(None, 'A') 
    root.left = TreeNode('A', 'B')
    root.right = TreeNode('A', 'C') 
    root.left.left = TreeNode('B', 'D')
    root.left.right = TreeNode('B', 'E')
    root.right.right = TreeNode('C', 'F')
    root.left.left.left = TreeNode('D', 'G')
    root.left.right.left = TreeNode('E', 'H')
    root.left.right.left.Left = TreeNode('H', 'J')
    root.left.right.right = TreeNode('E ', 'I')

    repreat = True
    getin = True
    global array
    global count 
    global length
    global get_parent
    global repArr
    repArr = [None]*100

    while repreat:
        Heading("Page","Binary Tree")
        print("THE FOLLOWING ARE POSSIBLE OPERATIONS:\n")
        print("\t1| BINARY TREE")
        print("\t2| INSERTION IN BINARY TREE")
        print("\t3| COMPLETE BINARY TREE")
        print("\n\t0| Exit")
        switch = int(input("\n\n\n-> enter "))

        match switch:
            case 1:
                caseT = True
                caseTT = True

                while caseT:
                    Heading("Page", "Binary Tree")
                    print("ARRAY REPRESENTATION:",end = '\n\t| ')
                    Length(root)
                    length = (2**length) - 1
                    repArr[0] = root.info
                    ArrayRep_BT(root)

                    for J in range(0, length):
                        if repArr[J] == None:
                            repArr[J] = ' '
                        print(repArr[J], end=' | ')

                    count = -1
                    length = 0 

                    print("\n\nFOLLOWING ARE THE POSSIBLE TRAVERSALS FOR TREE\n")
                    print("\t1| PRE-ORDER")
                    print("\t2| IN-ORDER")
                    print("\t3| POST-ORDER") 
                    print("\n\t0| Back")
                    print("\t9| Refresh")

                    let = int(input("\n\n\n-> enter "))
                    caseTT = False if let == 0 else True

                    while caseTT:
                        
                        Heading("Page", "Binary Tree")
                        print("ARRAY REPRESENTATION:",end = '\n\t| ')
                        Length(root)
                        length = (2**length) - 1
                        repArr[0] = root.info
                        ArrayRep_BT(root)

                        for J in range(0, length):
                            if repArr[J] == None:
                                repArr[J] = ' '
                            print(repArr[J], end=' | ')

                        count = -1
                        length = 0

                        print("\n\nFOLLOWING ARE THE POSSIBLE TRAVERSALS FOR TREE\n")
                        print("\t1| PRE-ORDER")
                        if let == 1:
                            print('',end='\t\t')
                            pre_order(root)
                            print()
            
                        print("\t2| IN-ORDER")
                        if let == 2:
                            print('',end='\t\t')
                            in_order(root)
                            print()

                        print("\t3| POST-ORDER") 
                        if let == 3:
                            print('',end='\t\t')
                            Set = True
                            post_order(root)
                            print()

                        print("\n\t0| Back")
                        print("\t9| Refresh")

                        let = int(input("\n\n\n-> enter "))
                        caseTT = False if let == 9 or let == 0 else True

                    caseT = False if let == 0 else True

            case 2:
                InputTree(root)
                
            case 3:
                rpt = True
                while rpt:
                    Heading("Page","Implement Complete Binary Tree")
                    print("CHOOSE ANY WAY TO IMPLEMENT TREE:")
                    print("\n\t1| ENTER NODES ONE-BY-ONE")
                    print("\t2| DIRECT IMLEMENTATION")
                    print("\t0| Exit")

                    let = int(input("\n\n\n=> enter "))

                    if let == 1:
                        MainICBT()
                    elif let == 2:
                        MainCBT()
                    elif let == 0:
                        rpt = False     

            case 0:
                x()       
            
        repeat = False if switch == 0 else True

################### GLOBAL VARIABLES DECLARATIONS
SIZE = 20
array = [None]*SIZE
get_parent = TreeNode(None, None)
terminalFL = []
count = -1
length = 0
prev = ''
################### CALLING MAIN FUNCTION
Main()    