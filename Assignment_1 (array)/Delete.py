from Styling import Options
from Styling import x
import os
import time

def DeleteFromStart(array):
    print("OPERATION | Delete from start")
    print("-"*163)
    # print("\nGiven Array: ")
    printArr(array, "\nGiven Array: \n")

    arrayIn = [0] * (len(array) - 1)

    for i in range(len(array)-1):
        arrayIn[i] = array[i+1]

    array = arrayIn
    
    print("\n\nArray after deleting first element:")
    return array

def DeleteFromEnd(array):
    print("OPERATION | Delete from end")
    print("-"*163)
    # print("\nGiven Array: ")
    printArr(array, "\nGiven Array: \n")

    arrayIn = [0] * (len(array) - 1)

    for i in range(len(array)-1):
        arrayIn[i] = array[i]

    array = arrayIn
    print("\n\nArray after deleting last element:")
    return array    

def DeleteFromanywhere(array):
    print("OPERATION | Delete from anywhere")
    print("-"*163)
    # print("\nGiven Array: ")
    printArr(array, "\nGiven Array: \n")

    numIn = int(input("\n\nEnter element to delete: "))

    j = 0
    k = -1
    for i in range(len(array)-1):
        k += 1
        if array[i] == numIn:
            array[i] = array[i+1]
            i -= 1
            j += 1
            k += 1
        else:
            array[i] = array[k]  

    if array[len(array)-1] == numIn:
        j += 1          
    arrayIn = [0] * (len(array) - j)

    for i in range(len(arrayIn)):
        arrayIn[i] = array[i] 
    array = arrayIn

    if j > 0:
        print(f"=> Total entries of {numIn} deleted : {j}\n")
        print(f"\nArary after deleting {numIn} is: ") 
    else:
        print(f"\nElement {numIn} is not present in the array...")            
    return array

def printArr(array, string):
    if len(array) == 0:
        print("\t NULL")
    else:
        print(f"{string}", end = "")

        for i in range(0, len(array)):
            print("  ", array[i], end=" ")

def MenuDelete(array):
    choiceD = 1
    count = 1
    while choiceD == 1:
        x()
        print("PAGE | Deletion")
        print("-"*163)
        printArr(array, "Given Array : ")

        print("\n\nPOSSIBLE OPERATIONS OF DELETION ON AN ARRAY: \n")
        print("\t1 | DeleteFromStart")
        print("\t2 | DeleteFromEnd")
        print("\t3 | DeleteFromanywhere")
        print("\n\t0 | BACK TO MAIN")

        switchD = int(input("\n\nenter => "))
        x()
        if len(array) > 0 or count == 1:
            match switchD:
                case 1:
                    array = DeleteFromStart(array)
                    printArr(array, "")
                case 2:
                    array = DeleteFromEnd(array)
                    printArr(array, "")
                case 3:
                    array = DeleteFromanywhere(array)
                    printArr(array, "")
                case 0:
                    count = 0
                    return array    
                case _:
                    print(f"\t\n_Incorrect Choice_{switchD}  \n\n\n") 
        else:
            print("PAGE | Deletion")
            print("-"*163)
            print("\n\n\n\t  ...THE ARRAY GOT NULL...")
            print("\tInsert some elements in your array!")
          
        if count == 1:  
            Options()
            choiceD = int(input("\n\n\nenter => "))    

    return array