from PN_ITPost import *
from Check_Pairs import *
from Evaluate_Postfix import *
from Quick_Sort import *
from Styling import *
from evaluate import *


def App_Stack():
    repeat = True
    while(repeat):

        os.system('cls')
        Heading("Page", "Applications Of Stack")
        option = 0
        infix = input("Enter Expression: ")

        print("\n\nCHOOSE ANY OPTION FROM FOLLOWING")
        print("\n\t1| CHECK PAIRS")
        print("\t2| INFIX TO POSTFIX")
        print("\t3| EVALUATE POSTFIX")
        print("\t4| QUICK SORT")
        print("\n\n0| Back")
        print("9| Repeat The Process")

        option = int(input("\n\n=> enter: "))

        while option != 9 and option != 0:

            Heading("Page", "Applications Of Stack")
            print(f"Enter Expression: {infix}")

            print("\n\nCHOOSE ANY OPTION FROM FOLLOWING")
            
            print("\n\t1| CHECK PAIRS")
            if option == 1:
                print(f"\t  > {Main_CP(infix)}")
            
            print("\t2| INFIX TO POSTFIX")
            if option == 2:
                postfix = Main_ITP(infix)
                print(f"\t  > Postfix Expression: {postfix}")

            print("\t3| EVALUATE POSTFIX")
            if option == 3:
                print(f"\t  > Evaluting postfix we get :", Main_EP(infix))
                print(f"\t  > Enter 10 To Check Process")

            print("\t4| QUICK SORT")
            if option == 4:
                Main_QS()

            if option != 4:
                print("\n\n0| Back")
                print("9| Repeat The Process")
                option = int(input("\n\n=> enter: "))
            elif option == 4:
                option = 100 

            if option == 10:
                Main_EPSteps(infix)

        repeat =  False if option == 0 else True
