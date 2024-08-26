from Styling import *

def Build_MinHeap(Tree, N, item):
    PTR = N-1

    while PTR > 0:
        PAR = int((PTR+1)/2)

        if item >= Tree[PAR-1]:             
            Tree[PTR] = item
            return

        Tree[PTR] = Tree[PAR-1]
        PTR = PAR-1

    Tree[0] = item 

def Build_MaxHeap(Tree, N, item):
    PTR = N-1

    while PTR > 0:
        PAR = int((PTR+1)/2)

        if item <= Tree[PAR-1]:             
            Tree[PTR] = item
            return

        Tree[PTR] = Tree[PAR-1]
        PTR = PAR-1

    Tree[0] = item     

def HeapSort():
    repeat = True

    while repeat:
        sorted_List = []

        Heading('page', 'Heap Sort')
        print('Enter Heap Type: ')
        print('\n\t1| Min Heap')
        print('\t2| Max Heap')
        print('\n\t0| Exit')

        option = int(input('\n\n\n=> Enter '))

        Heading('page', 'Heap Sort \ Input Heap')
        size = int(input('\nEnter size of heap: '))
        print('Enter heap elements: ')
        heap = [0]*size

        for i in range(size):
            heap[i] = int(input())

        match option:
            case 1:
                Heading('Page', 'Min Heap Sort')

                for index, value in enumerate(heap):
                    Build_MinHeap(heap, index+1, value)

                print('The Heap: ', end=' | ')
                for values in heap:
                    print(values , end=' | ') 

                while heap:
                    for index, value in enumerate(heap):
                        Build_MinHeap(heap, index+1, value)
                    sorted_List.append(heap.pop(0))
                     
                print('\n\nHeap after sorting: ', end='\n\t | ')
                for value in sorted_List:
                    print(value, end=' | ')

            case 2:
                Heading('Page', 'Max Heap Sort')

                for index, value in enumerate(heap):
                    Build_MaxHeap(heap, index+1, value)

                print('The Heap: ', end=' | ')
                for values in heap:
                    print(values , end=' | ')   

                while heap:
                    for index, value in enumerate(heap):
                        Build_MaxHeap(heap, index+1, value)
                    sorted_List.append(heap.pop(0))  

                print('\n\nHeap after sorting: ', end='\n\t | ')
                for value in reversed(sorted_List):
                    print(value, end=' | ')      

            case 0:
                repeat = False
            
        let = input('\n\n\nDone_ ')    