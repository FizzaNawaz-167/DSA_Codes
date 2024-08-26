from Styling import *
from Stack_Array import *
   
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    print(arr)
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    print(arr)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    print()
    return i + 1

def quicksort(arr):
    stack = Static_Stack()
    stack.push(0)
    stack.push(len(arr) - 1)
    
    while not stack.is_empty():
        high = stack.pop()
        low = stack.pop()
        
        pivot_index = partition(arr, low, high)
        
        if pivot_index - 1 > low:
            stack.push(low)
            stack.push(pivot_index - 1)
        
        if pivot_index + 1 < high:
            stack.push(pivot_index + 1)
            stack.push(high)


array = [18, 12, 17, 9, 11]
quicksort(array)
# def Main_QS():
#     repeat = True
#     while repeat:
#         Heading("Operation", "Quick Sort")
#         size = int(input("Enter size of array: "))
#         array = [None]*size

#         print("Enter elements into array: ")
        # for i in range(0, size):
        #     array[i] = int(input())

        # os.system('cls')
        # Heading("Operation", "Quick Sort")

        # print("The Array: ", end=" | ")
        # for i in range(0, len(array)):
        #     print(array[i], end=" | ")

        # quicksort(array)
        # print("\n\nArray after sorting: \n\t", end=" | ")
        # for i in range(0, len(array)):
        #     print(array[i], end=" | ")

        # print("\n\n\n0| Back")
        # print("9| Repeat The Process")

        # option = int(input("\n\n=> enter: "))  

        # repeat = True if option == 9 else False  
