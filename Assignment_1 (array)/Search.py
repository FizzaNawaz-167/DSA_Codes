from Styling import Options
from Styling import x
import os
import time


def getArray():
    size = int(input("\nSpecify the size of array: "))
    arr = [None] * size
    print("\nEnter array elements: ")

    for i in range(0, size):
        arr[i] = int(input())
    return arr

def putArray(ss_arr):
    print("\nThe Array : ", end = "")
    for i in range(len(ss_arr)):
        print("  ",ss_arr[i], end=" ")    

def search(ss_arr, j):
    choiceSr = 1

    while choiceSr == 1:
        x()
        print("PAGE | Searching")
        print("-"*163)
        check = 0

        if j == 0:
            ss_arr = getArray()
        else: 
            let = int(input("\nUse given array (1) or Enter new one (0):"))
            if let == 1:
                pass
            else:
                ss_arr = getArray()      

        x()
        j = 1
        print("OPERATION | Search element in array")
        print("-"*163)
        putArray(ss_arr)

        element = int(input("\n\nEnter element to search: "))
        for i in range(len(ss_arr)):
            if (ss_arr[i] == element):
                print(f"\n=> {element} is found at position {i+1} (index {i})", end="") 
                check += 1   

        if check == 0:        
            print("\nThe element don't exist...")
        elif check > 0:
            print("\n\t...Search Successful...")

        Options()
        choiceSr = int(input("\n\nenter => "))
   
    return ss_arr    