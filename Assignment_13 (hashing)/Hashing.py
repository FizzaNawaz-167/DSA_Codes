import os

def Heading():
    os.system('cls')
    print('HASHING TECHNIQUE | CHAINING')
    print('-'*160)
    print()

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

def Hashing(array):
    dummy_array = [0]*10

    for index, value in enumerate(array):
        node = Node(value)
        reminder = value % 10

        if dummy_array[reminder] == 0:
            dummy_array[reminder] = node
        else:
            cur = dummy_array[reminder]
            while cur.next:
                cur = cur.next
            cur.next = node  

    return dummy_array

def Traverse(array):
    print('\n\nCHAINING:\n\t _______\n\t| index |\n\t|-------|')

    for index, value in enumerate(array):
        if value == 0:
            print(f'\t| {str(index).center(5)} |')
        else:
            cur = value
            print(f'\t| {str(index).center(5)}', end= ' | ')
            while cur:
                print('-> ', end= str(cur.info).ljust(5))
                cur = cur.next
            print()

    print('\t|_______|')        

def Search(array, target):
    reminder = target % 10
    iterate = 0

    if array[reminder] != 0:
        cur = array[reminder]
        while cur:
            iterate += 1
            if cur.info == target:
                return reminder, iterate
            cur = cur.next

    return reminder, None

repeat = True
while repeat:
    Heading()

    print('CHOOSE AS PER YOUR CONVENIENCE:\n')
    print('\t1 | USE DEFAULT ARRAY')
    print('\t9 | CREATE NEW ARRAY')

    choice = int(input('\n\nEnter_ '))
    if choice == 1:
        array = [123, 902, 657, 32, 43, 129, 54, 932, 432, 83, 675, 55, 877]
    elif choice == 9:
        size = int(input('Enter array size: '))
        array = [0]*size
        print('Enter array elements: ') 
        for i in range(size):
            array[i] = int(input())   

    Heading()        

    print('THE ARRAY:', end='\n\t | ')
    for values in array:
        print(values, end=' | ')

    dummy_array = Hashing(array)
    Traverse(dummy_array)

    print('\n1 | SEACRCH')
    print('0 | Exit')

    switch = int(input('\n\nenter_ '))
    match switch:
        case 1:
            target = int(input('Enter element to search: '))
            index, location = Search(dummy_array, target)
            if location:
                print(f'{target} is found at index {index} on position {location} in the list.')
            else:
                print(f'{target} not found in the list at index {index}.')    
        case 0:
            repeat = False     

    repeat = int(input('\nRepeat-1 or Exit-0 : '))
    repeat = False if repeat == 0 else True