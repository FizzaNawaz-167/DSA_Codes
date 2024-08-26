from Styling import *
from Queue_Array import *
from Queue_SLL import *
from Stack_Array import *
from Stack_SLL import *
import os
import time

repeat = True
while repeat:
    case1 = True
    case2 = True
    x()
    Heading("Page", "Main")
    print("CHOOSE ANY OF THE DATA STRUCTURE\n")
    print("\t1| STACK")
    print("\t2| QUEUE")
    print("\n\t0| Exit")

    switch = int(input("\n\n=> enter: "))
    x()

    match switch:
        case 1:
            while case1:
                os.system('cls')
                let = 0
                Heading("Page", "Stack")
                print("CHOOSE ANY OPTION\n")
                print("\t1| STACK USING ARRAY")
                print("\t2| STACK USING LINKED LIST")
                print("\n\t0| Main")

                option = int(input("\n\n=> enter: "))
                
                match option:
                    case 1:
                        let = Main_SA()
                    case 2:
                        let = Main_SL()
                    case 0:
                        let = 9

                case1 = False if let == 9 else True              
        
        case 2:
            while case2:
                os.system('cls')
                let = 0
                Heading("Page", "Queue")
                print("CHOOSE ANY OPTION\n")
                print("\t1| QUEUE USING ARRAY")
                print("\t2| QUEUE USING LINKED LIST")
                print("\n\t0| Main")

                option = int(input("\n\n=> enter: "))
                
                match option:
                    case 1:
                        let = Main_QA()
                    case 2:
                        let = Main_QL()
                    case 0:
                        let = False

                case2 = False if let == 9 else True

        case 0:
            print("...End...")

    repeat = False if switch == 0 else True                             
