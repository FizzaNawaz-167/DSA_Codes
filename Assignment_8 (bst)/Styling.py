import os
import time

def x():
    time.sleep(0.1)
    os.system('cls')

def Heading(str1, str2):
    os.system('cls')
    print(f"{str1} | {str2}")
    print("-"*161)
    print()


def delete(root, item, LOC, PAR):
    if LOC is None:
        return root  # info not found, no change

    # Case 1: LOC to delete has no children (leaf LOC)
    if LOC.left is None and LOC.right is None:
        if PAR:
            if PAR.left == LOC:
                PAR.left = None
            else:
                PAR.right = None
        else:
            root = None

    # Case 2: LOC to delete has one child
    elif LOC.left is None or LOC.right is None:
        if LOC.left:
            child = LOC.left
        else:
            child = LOC.right

        if PAR:
            if PAR.left == LOC:
                PAR.left = child
            else:
                PAR.right = child
        else:
            root = child

    # Case 3: LOC to delete has two children
    else:
        SUC_PAR = LOC
        SUC = LOC.right
        while SUC.left:
            SUC_PAR = SUC
            SUC = SUC.left

        # Replace the LOC with its in-order SUC
        LOC.info = SUC.info

        # Delete the in-order SUC
        if SUC_PAR.left == SUC:
            SUC_PAR.left = SUC.right
        else:
            SUC_PAR.right = SUC.right

    return root
