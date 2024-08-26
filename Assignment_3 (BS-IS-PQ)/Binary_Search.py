import os

repeat = True

while repeat:
    os.system('cls')
    print('BINARY SEARCH \n' + '-'*160 + '\n')
    Data = [11, 22, 30, 33, 40, 44, 50, 60, 67, 80, 88, 99]

    print(Data)
    ITEM = int(input("\nEnter the element to search: "))

    lowerB = 0
    upperB = len(Data) - 1

    BEG = lowerB
    END = upperB
    MID = int((BEG+END)/2)

    LOC = None

    while BEG <= END and Data[MID] != ITEM:
        if ITEM < Data[MID]:
            END = MID - 1
        else:
            BEG = MID + 1

        MID = int((BEG+END)/2)

    if Data[MID] == ITEM:
        LOC = MID
    else:
        LOC = None    

    if LOC == None:
        print(f"{ITEM} not found!!!")
    else:    
        print(f"{ITEM} is present at location : {LOC+1}")

    choice = int(input("\n\nRepeat with 1 ... ")) 

    repeat = True if choice == 1 else False