import os
import time

def Options():
    print("\n"*8)

    # print("~"*25)
    print("1| BACK TO LAST PAGE ", end = "\n")
    print("0| MAIN PAGE ", end="")    
    # print(" ________ ")
    # print("| BACK   |")
    # print("|______1_|")

    # print(" ________ ")
    # print("|  MAIN  |")
    # print("|______1_|")  

def start():
    os.system('cls')
    for i in range(3):

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t", end = " ")

        print("Starting! . ", end = ". " *i)
        time.sleep(0.3)
        os.system('cls')

def end():
    os.system('cls')
    for i in range(6):

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t", end = "   ")

        print("Ended!", end = "")
        # print("\n\t\t\t\t\t\t\t\t\t\t", end = " ")
        print("Thank you")   
        # print("\n\n\t\t\t\t\t\t\t\t\t\t", end = " ")
        # print("",end = "_"*i)
        # print("_",end = "_"*i)

        time.sleep(1)
        os.system('cls')

def x():
    time.sleep(0.3)
    os.system('cls')    
