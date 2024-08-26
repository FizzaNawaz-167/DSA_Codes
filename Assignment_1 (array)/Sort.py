from Styling import Options
from Styling import x
import os
import time   

def BubbleSort(ss_arr):
    print("OPERATION | Bubble sort")
    print("-"*163)
    printArr(ss_arr, "\nGiven Array: ")

    n = len(ss_arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if ss_arr[j] > ss_arr[j+1]:
                temp = ss_arr[j]
                ss_arr[j] = ss_arr[j+1]
                ss_arr[j+1] = temp

    print("\n\nArray after Bubble Sort: ") 

def InsertionSort(ss_arr):
    print("OPERATION | Insertion sort")
    print("-"*163)
    printArr(ss_arr, "\nGiven Array: ")
    
    n = len(ss_arr)

    for i in range(1, n):
        key = ss_arr[i]
        j = i-1
        while j>=0 and ss_arr[j]>key:
            ss_arr[j+1] = ss_arr[j]
            j = j-1

        ss_arr[j+1] = key

    print("\n\nArray after Insertion Sort: ")

def SelectionSort(ss_arr):
    print("OPERATION | Selection sort")
    print("-"*163)
    printArr(ss_arr, "\nGiven Array: ")

    n = len(ss_arr)

    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if ss_arr[min_index] > ss_arr[j]:
                min_index = j

        if min_index != i:
            ss_arr[i], ss_arr[min_index] = ss_arr[min_index], ss_arr[i]

    print("\n\nArray after Selection Sort: ") 

def getArray():
    size = int(input("\nSpecify the size of array: "))
    arr = [None] * size
    print("\nEnter array elements: ")

    for i in range(0, size):
        arr[i] = int(input())
    return arr

def printArr(ss_arr, argument):
    print(f"{argument}", end = "")
    for i in range(0, len(ss_arr)):
        print("  ", ss_arr[i], end=" ")

def MenuSort(ss_arr, j):
    choiceS = 1
    count = 1
    while choiceS == 1:
        x()
        print("PAGE | Sorting")
        print("-"*163)

        if j == 0:
            ss_arr = getArray()
        else:  
            let = int(input("\nUse Last Given Array (1) or Enter New One (0):"))
            if let == 1:
                pass
            else:    
                ss_arr = getArray()               

        copyArr = [0]*len(ss_arr)
        for i in range(len(ss_arr)):
            copyArr[i] = ss_arr[i]

        x()
        j = 1
        print("PAGE | Sorting")
        print("-"*163)

        printArr(ss_arr, "\nThe Array : ")

        print("\n\nPOSSIBLE OPERATIONS OF SORTING ON AN ARRAY: \n") 
        print("\n\t1 | SelectionSort")
        print("\t2 | BubbleSort")
        print("\t3 | InsertionSort")
        print("\n\t0 | BACK TO MAIN") 

        switchS = int(input("\n\n\nenter => "))
        x()
        match switchS:
            case 1:
                SelectionSort(ss_arr)
                printArr(ss_arr, "")
            case 2:
                BubbleSort(ss_arr)
                printArr(ss_arr, "")
            case 3:
                InsertionSort(ss_arr)
                printArr(ss_arr, "")
            case 0:
                count = 0
                return copyArr    
            case _:
                print(f"\t\n_Invalid Choice_{switchS}  \n\n\n") 
       
        if count == 1:
            Options()
            choiceS = int(input("\n\nenter => "))
    
    
    return copyArr    