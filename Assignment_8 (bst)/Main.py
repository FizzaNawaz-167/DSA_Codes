from Styling import *

class TreeNode:
    def __init__(self, info):
        self.left = None
        self.info = info
        self.right = None

def FIND(self, item):
    par = None
    PTR = self

    while PTR:
        if item == PTR.info:
            return PTR, par

        if item < PTR.info:
            par = PTR
            PTR = PTR.left
        else:
            par = PTR
            PTR = PTR.right

    return None, par

def Search(self, item):
    path = []

    while self:
        if item == self.info:
            path.append(self.info)
            return path

        if item < self.info:
            path.append(self.info)
            self = self.left
        else:
            path.append(self.info)
            self = self.right

    return None     

def INSERT(self, item, loc, par):
    new_node = TreeNode(item)
    
    if self is None:
        return new_node

    if item < par.info:
        par.left = new_node
    else:
        par.right = new_node

    return self

def DELETE(self, item, loc, par):
    if loc is None:
        return self 

    if loc.left and loc.right:

        suc_par = loc
        suc = loc.right

        while suc.left:
            suc_par = suc
            suc = suc.left

        loc.info = suc.info

        if suc_par.left == suc:
            suc_par.left = suc.right
        else:
            suc_par.right = suc.right    

    else:

        if not loc.left and not loc.right:
            child = None

        elif not loc.left and loc.right:   
            child = loc.left

        elif not loc.right and loc.left:
            child = loc.right     

        if par:
            if par.left == loc:
                par.left = child
            else:
                par.right = child
        else:
            self = child

    return self

def TRAVERSE(self):
    if self is not None:
        TRAVERSE(self.left)
        print(self.info, end=' | ')
        TRAVERSE(self.right)

def MAIN():
    root = TreeNode(50)
    array = [30, 70, 20, 40, 60, 80 ,47]

    for index in array:
        loc, par = FIND(root, index)
        root = INSERT(root, index, loc, par)

    repeat = True
    while repeat:

        Heading('Page', 'Binary Search Tree')
        print('The Tree:', end='\t| ')
        TRAVERSE(root)

        print("\n\nENTER ANY OPERATION TO PERFORM:\n")
        print("\t1| INSERT A NODE")
        print("\t2| DELETE A NODE")
        print("\t3| SEARCH A NODE")
        print("\n\t0| Exit")

        switch = int(input("\n\n\n=>enter "))
        match switch:
            case 1:
                index = int(input("Enter value to INSERT: "))

                loc, par = FIND(root, index)
                root = INSERT(root, index, loc, par)
                TRAVERSE(root)

            case 2:
                index = int(input("Enter value to DELETE: "))

                loc, par = FIND(root, index)
                root = DELETE(root, index, loc, par)
                TRAVERSE(root)

            case 3:
                item = int(input('Enter a value to SEARCH: '))
                pathTracker = Search(root, item)
                if pathTracker:
                    if len(pathTracker) == 1:
                        print(item,'is the root.')
                    print('The path to',item,'is:',pathTracker)
                else:
                    print(f"{item} is not present in the tree.")   

                let = input('\n\nDone_ ')

            case 0:
                x()   

        repeat = False if switch == 0 else True         

########################################################
MAIN()    