import os
def Heading():
    os.system('cls')
    print('Radix Sort')
    print('-'*161)

def Process(array, divisor):
    n = len(array)                  
    output = [0] * n                
    count = [0] * 10
    
    for i in range(n):
        index = array[i] // divisor
        count[index % 10] += 1      # increment the value present at certain index -> no. of times a no. exixts

    for i in range(1, 10):
        count[i] += count[i - 1]

    print(count)

    i = n - 1
    while i >= 0:
        index = array[i] // divisor
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
        print(count, output)

    for i in range(n):
        array[i] = output[i]
    print(array)    

def RadixSort(array):
    max_num = max(array)
    
    divisor = 1
    while max_num // divisor > 0:
        Process(array, divisor)
        divisor *= 10

repeat = True
while repeat:
    # Heading()
    # size = int(input('\nEnter Size Of Array: '))
    # array = [0]*size
    # print('Enter Array Elements: ')
    # for i in range(size):
    #     array[i] = int(input())

    Heading()
    # print('\nThe Array: ', end='\t | ')
    # for i in range(size):
    #     print(array[i], end=' | ')

    array = [13, 15, 41, 57, 12]
    size = 5
    RadixSort(array)
    print('\n\nSorted Array: ', end='\t | ')
    for i in range(size):
        print(array[i], end=' | ')

    choice = int(input('\n\n\nRepeat_1/Exit_0: '))
    repeat = False if choice == 0 else True