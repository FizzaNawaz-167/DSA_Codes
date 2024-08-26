from Styling import *

class TreeNode:
    def __init__(self, info):
        self.left = None
        self.info = info
        self.right = None

def INSERT(self, item, loc, par):
    new_node = TreeNode(item)
    
    if self is None:
        return new_node

    if item < par.info:
        par.left = new_node
    else:
        par.right = new_node

    return self

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

def TRAVERSE(self): 
    queue = []
    result = []

    if self:
        queue.append(self)

    while queue:
        current = queue.pop(0)
        result.append(current.info)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result
       
def main():
    repeat = True

    while repeat:
        Heading('PAGE','BINARY SEARCH TREE APPLICATION (Find Duplicates)')

        print('HERE WE ARE WORKING WITH:\n')
        print('\t1| DUPLICATES IN BST')
        print('\t2| BFS IN BINARY TREE')
        print('\n\t0| EXIT')

        option = int(input('\n\n=> Enter '))

        Heading('PAGE','ENTER THE ARRAY')
        # array = [23, 56, 11, 11, 54, 78, 90, 23, 15, 30]

        size = int(input('Size of array: '))
        array = [None]*size

        print('Enter array elements: ')
        for index in range(size):
            array[index] = int(input())

        Root = None
        
        match option:
            case 1:
                Heading('PAGR', 'FIND DUPLICATES IN BST')
                print('The array: ', end=' | ')
                for value in array:
                    print(value, end=' | ')

                duplicates = []

                if not Root:
                    for index, value in enumerate(array):
                        loc, par = FIND(Root, value)

                        if loc is not None:
                            duplicates.append(array.pop(index))
                        else:
                            Root = INSERT(Root, value, loc, par)

                print('\n\nThe Tree: ', end=' | ')
                for value in array:
                    print(value, end=' | ')

                print('\n\nDuplicates: ', end=' | ')
                for value in duplicates:
                    print(value, end=' | ')

                
                let = input('\n\n\nDone_ ')

            case 2:
                Heading('PAGR', 'BREADTH FIRST SEARCH IN BINARY TREE')
                duplicates = []

                if not Root:
                    for index, value in enumerate(array):
                        loc, par = FIND(Root, value)

                        if loc is not None:
                            duplicates.append(array.pop(index))
                        else:
                            Root = INSERT(Root, value, loc, par)

                queue = TRAVERSE(Root)

                print('The Tree: ', end=' | ')
                for value in queue:
                    print(value, end=' | ')

                let = input('\n\n\nDone_ ')    

main()    
