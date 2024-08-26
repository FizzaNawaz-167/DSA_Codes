def Build_Heap(Tree, N, item):
    PTR = N-1

    while PTR > 0:
        PAR = int((PTR+1)/2)

        if item <= Tree[PAR-1]:             # >= for min_heap & <= for max_heap
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
        if Last >= tree[Left] and Last >= tree[Right]:      # <= for min and >= for max
            tree[PTR] = Last
            return tree

        if tree[Right] <= tree[Left]:                   # >= for min and <= for max
            tree[PTR] = tree[Left]
            PTR = Left
        else:
            tree[PTR] = tree[Right]
            PTR = Right

        Left = 2*PTR + 1
        Right = 2*PTR + 2

    if Left == (N-1) and Last < tree[Left]:             # > for min and < for max
        PTR = Left

    tree[PTR] = Last 
    return tree          

###################################################

sorted_List = []

array = [90, 67, 81, 44, 34, 21, 45, 12]            # max_heap

while len(array) > 1:
    tree = [0]*(len(array)-1)
    N = len(tree)

    for i in range(0, N):
        tree[i] = array[i]

    sorted_List.append(array[0])
    array = Delete_Heap(array, tree, N)

print(sorted_List)
