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

def main():
    min_heap = [22, 5, 11, 19, 2, 11, 25, 5]

    while True:
        print(min_heap)  
        if len(min_heap) == 1: break  

        for index, value in enumerate(min_heap):    Build_Heap(min_heap, index+1, value)
        f = min_heap.pop(0)

        for index, value in enumerate(min_heap):    Build_Heap(min_heap, index+1, value)
        s = min_heap.pop(0)
        
        res = f + s
        min_heap.append(res)

main()