from Styling import Options
from Styling import x
import time
import os

def InsertAtStart(array):
    print("OPERATION | Insert at start")
    print("-"*163)
    printArr(array, "\nGiven Array: ")

    numIn = int(input("\n\nEnter the element to insert: "))

    arrayIn = [0] * (len(array)+1)

    arrayIn[0] = numIn
    for i in range(len(array)):
        arrayIn[i+1] = array[i]

    array = arrayIn  
    print("\nArray after insertion at start:")  
    return array

def InsertAtEnd(array): 
    print("OPERATION | Insert at end")
    print("-"*163)
    printArr(array, "\nGiven Array: ")

    numIn = int(input("\n\nEnter the element to insert: "))

    arrayIn = [0] * (len(array)+1)

    for i in range(len(array)):
        arrayIn[i] = array[i]

    arrayIn[len(array)] = numIn

    array = arrayIn
    print("\nArray after insertion at end:")
    return array

def InsertAnywhere(array):
    print("OPERATION | Insert anywhere")
    print("-"*163)
    printArr(array, "\nGiven Array: ")

    numIn = int(input("\n\nEnter the element to insert: "))
    pos = int(input("Enter the position: "))    
    
    if pos <= len(array)+1:
        
        arrayIn = [0] * (len(array)+1)
        for i in range(pos-1):
            arrayIn[i] = array[i]

        arrayIn[pos-1] = numIn

        for i in range(pos-1, len(array)):
            arrayIn[i+1] = array[i]

        array = arrayIn
        print(f"\nArray after insertion at position {pos}:")
    else:
        print("\nInvalid position...")    
    return array

def printArr(array, line):
    if len(array) == 0:
        print("\nGiven Array :\tNULL")
    else:
        print(f"{line}", end = "")
        for i in range(0, len(array)):
            print("  ", array[i], end=" ")

def MenuInsert(array):
    choiceIn = 1
    count = 1
    while choiceIn == 1:
        x() 
        print("PAGE | Insertion")
        print("-"*163)
        printArr(array, "\nGiven Array: ")

        print("\n\nPOSSIBLE OPERATIONS OF INSERTION ON AN ARRAY: \n")
        print("\t1 | InsertAtStart")
        print("\t2 | InsertAtEnd")
        print("\t3 | InsertAnywhere")
        print("\n\t0 | BACK TO MAIN")

        switchIn = int(input("\n\n\nenter => "))
        x()
        if len(array) < 15 or count == 1:
            match switchIn:
                case 1:
                    array = InsertAtStart(array)
                    printArr(array, "")
                case 2:
                    array = InsertAtEnd(array)
                    printArr(array, "")
                case 3:
                    array = InsertAnywhere(array)
                    printArr(array, "")
                case 0:
                    count = 0
                    return array
                case _:
                    print(f"\t\n_Incorrect Choice_{switchIn}  \n\n\n")
        else:
            print("PAGE | Insertion")
            print("-"*163)
            print("\n\n\n\t  ...THE ARRAY GOT FULL...")
            print("Delete some elements to create space!")
        
        if count == 1:
            Options()
            choiceIn = int(input("\n\nenter => "))                


    return array