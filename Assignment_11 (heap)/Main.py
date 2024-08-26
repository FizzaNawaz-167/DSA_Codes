from Styling import *
from MinHeap import *
from MaxHeap import *
from HeapSort import *

repeat = True
while repeat:
    Heading('Page', 'Heap')
    print('\nSELECT SOME HEAP TYPE TO CONTINUE:')
    print('\n\t1| Min Heap')
    print('\t2| Max Heap')
    print('\t3| Heap Sort')
    print('\n\t0| Exit')

    choose = int(input('\n\n\n=> Enter '))

    match choose:
        case 1:
            mainMin()
        case 2:
            mainMax()
        case 3:
            HeapSort()    
        case 0:
            repeat = False        