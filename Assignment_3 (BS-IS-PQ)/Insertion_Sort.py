import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List():
    def __init__(self):
        self.head = None

    def Append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node    
            new_node.next = None

    def InsertionSort(self):
        new = Linked_List()

        if not self.head or not self.head.next:
            return self.head

        copy = Node(0) 
        copy.next = self.head
        cur = self.head
        while cur.next:
            if cur.next.data < cur.data:
                temp = cur.next
                cur.next = cur.next.next
                prev = copy
                while prev.next.data < temp.data:
                    prev = prev.next
                temp.next = prev.next
                prev.next = temp
            else:
                cur = cur.next

        return copy.next        

    def Display(self, string, let):
        print(f"{string}",end = "")
        cur = let
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next

        self.head = None    

repeat = True
l = Linked_List()

while(repeat):
    os.system('cls')
    print("\nINSERTION SORTING \n" + '-'*160 + "\n")

    amount = int(input("Enter a number of elements: "))
    print("Enter the elements: ")
    for i in range(amount):
        data = int(input())
        l.Append(data)

    let = l.InsertionSort() 
    l.Display("\nArray after Insertion Sorting:\n\t", let)

    choice = int(input("\n\nRepeat with 1 ... ")) 
    repeat = True if choice == 1 else False  
