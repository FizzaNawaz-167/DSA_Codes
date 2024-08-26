from Styling import *
from SinglyLL import *
from DoublyLL import *
from SinglyCircularLL import *
from DoublyCircularLL import *

def main():
    repeat = True
    while repeat:
        x()
        Heading("PAGE", "MAIN")
        print("CHOOSE A LINKED LIST TO PERFORM ANY OPERATION ON.\n")
        print("\t1 | SINGLY LINKED LIST")
        print("\t2 | DOUBLY LINKED LIST")
        print("\t3 | SINGLY CIRCULAR LINKED LIST")
        print("\t4 | DOUBLY CIRCULAR LINKED LIST")
        print("\n\t0 | EXIT")

        switch = int(input("\n\n=> enter: "))

        match switch:
            case 1:
                mainSLL()
            case 2:
                mainDLL()
            case 3:
                mainSCLL()
            case 4:
                mainDCLL() 
            case 0:
                x()  

        repeat = False if switch == 0 else True

main()
