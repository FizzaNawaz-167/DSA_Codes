from Styling import *

def Build_Heap(Tree, N, item):
    PTR = N-1

    while PTR > 0:
        PAR = int((PTR+1)/2)

        if item >= Tree[PAR-1]:             
            Tree[PTR] = item
            return

        Tree[PTR] = Tree[PAR-1]
        PTR = PAR-1

    Tree[0] = item 

def Delete_Heap(Tree, tree, N):   

    if len(tree) < 1:
        return  

    item = tree[0]
    Last = Tree[len(Tree)-1]
    PTR = 0
    Left = 1
    Right = 2

    while Right <= (N-1):
        if Last <= tree[Left] and Last <= tree[Right]:      
            tree[PTR] = Last
            return tree

        if tree[Right] >= tree[Left]:                   
            tree[PTR] = tree[Left]
            PTR = Left
        else:
            tree[PTR] = tree[Right]
            PTR = Right

        Left = 2*PTR + 1
        Right = 2*PTR + 2

    if Left == (N-1) and Last > tree[Left]:             
        PTR = Left

    tree[PTR] = Last 
    return tree          

def mainMin():
    array = [12, 34, 23, 21, 81, 45 ,90, 44, 67]          
    repeat = True

    while repeat:
        Heading('Page', 'Min Heap')
        print('The Heap: ' ,end=' | ')

        if array:
            for value in array:
                print(value, end=' | ')
        else:
            print('Empty')        

        print("\n\nENTER SOME OPTION TO CONTINUE:")
        print("\n\t1| INSERT")
        print("\t2| DELETE")
        print("\t0| EXIT") 
        option = int(input("\n\n=>enter "))   

        match option:
            case 1:
                if not array:
                    array = []                      

                index = len(array)                  
                Tree = [0]*(len(array)+1)           

                for i in range(len(array)):        
                    Tree[i] = array[i]

                let = int(input("Enter value to insert: "))
                Tree[index] = let               

                for index, value in enumerate(Tree):
                    Build_Heap(Tree, index+1, value)  

                array = [0]*len(Tree)           
                for i in range(len(Tree)):
                    array[i] = Tree[i]      

            case 2:

                if array:
                    tree = [0]*(len(array)-1)
                    N = len(tree)
                    
                    for i in range(0, N):
                        tree[i] = array[i]

                    array = Delete_Heap(array, tree, N)
                    print(array)

            case 0:
                repeat = False   
# main() 