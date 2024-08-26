import os
def Heading():
    os.system('cls')
    print('Merge Sort')
    print('-'*161)

def MergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        MergeSort(left_half)
        MergeSort(right_half)

        i = j = k = 0
        print(f"left-half: {left_half}")
        print(f"right-half: {right_half}")

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
                print(f"array_k i-left = {array}")
            else:
                array[k] = right_half[j]
                j += 1
                print(f"array_k j-right = {array}")
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

        print(f"array_k out = {array}")    

repeat = True
while repeat:
    Heading()
    # size = int(input('\nEnter Size Of Array: '))
    # array = [0]*size
    # print('Enter Array Elements: ')
    # for i in range(size):
    #     array[i] = int(input())

    # Heading()
    # print('\nThe Array: ', end='\t | ')
    # for i in range(size):
    #     print(array[i], end=' | ')

    array = [12, 9, 13, 3, 7, 1]
    size = len(array)

    MergeSort(array)
    print('\n\nSorted Array: ', end='\t | ')
    for i in range(size):
        print(array[i], end=' | ')

    choice = int(input('\n\n\nRepeat_1/Exit_0: '))
    repeat = False if choice == 0 else True
