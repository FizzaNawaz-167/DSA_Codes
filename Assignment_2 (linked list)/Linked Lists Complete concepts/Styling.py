import os
import time

def x():
    time.sleep(0.3)
    os.system('cls')

def Heading(str1, str2):
    print(f"{str1} | {str2}")
    print("-"*161)
    print()  # skip line

def Options():
    print("\n"*5)
    print("1| BACK TO LAST PAGE ", end = "\n")
    print("0| MAIN PAGE ", end="")    

def start():
    os.system('cls')
    for i in range(3):
        print("\n"*16, "\t"*8, end = " ")
        print("Starting! . ", end = ". " *i)
        x()

def end():
    os.system('cls')
    for i in range(6):
        print("\n"*16, "\t"*8, end = " ")
        print("Ended!", end = "")
        print("Thank you")   
        x()


