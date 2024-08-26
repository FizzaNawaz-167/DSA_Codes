from Insert import MenuInsert
from Delete import MenuDelete
from Sort import MenuSort
from Search import search
from Styling import start
from Styling import end
from Styling import x
import os
import time

def main():
    array = [1, 4, 6, 3, 8]
    ss_arr = [None]
    i = 1
    j = 0
    while i != 0:
        print("PAGE | MAIN")
        print("-"*163)
        print("\nSELECT ANY OPERATION TO PERFORM ON ARRAY : \n") 
        print("\t1 | Insertion")
        print("\t2 | Deletion")
        print("\t3 | Sorting")
        print("\t4 | Searching")
        print("\n\t0 | EXIT")

        switch = int(input("\n\n\nenter => "))
      
        match switch:
            case 1:
                array = MenuInsert(array)                
            case 2:
                array = MenuDelete(array)           
            case 3:
                ss_arr = MenuSort(ss_arr, j)
                j = 1
            case 4:
                ss_arr = search(ss_arr, j)
                j = 1
            case 0:
                end()
            case _:
                print(f"\t\n_Invalid Choice_{switch}  \n\n\n")
                time.sleep(2)

        if array is None:
            array = []
        x()
        i = switch

start()        
main()
