import os

class Node:
    def __init__(self, data, pri_num):
        self.data = data
        self.pri_num = pri_num
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.top = -1

    def Enqueue(self, data, pri_num):
        new_node = Node(data, pri_num)
        cur = self.head

        if self.head is None:
            self.head = new_node
            new_node.next = None
        elif self.head.pri_num > new_node.pri_num:
            new_node.next = self.head
            self.head = new_node
        else:
            while cur.next and cur.next.pri_num <= new_node.pri_num:
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node

    def Dequeue(self):
        self.head = self.head.next 

    def Display(self):
        cur = self.head

        if self.head is None:
            return None
        else: 
            while cur:
                print(F"| {cur.data} |{cur.pri_num}|" , end = " -> ")
                cur = cur.next

PQ = Queue()
PQ.Enqueue(40, 3)
PQ.Enqueue(16, 4)
PQ.Enqueue(77, 2)
PQ.Enqueue(21, 2)

repeat = True

while(repeat):
    os.system('cls')
    print("\nPRIORITY QUEUE \n" + '-'*160 + "\n")
    print(PQ.Display())
    print("\n\n1 | Enqueue")
    print("2 | Dequeue")
    print("\n0 | Exit")

    choose = int(input("\n\n\nenter => "))

    match choose:
        case 1:
            data = int(input("Data to enter: "))
            p_no = int(input("Priority number: "))
            PQ.Enqueue(data, p_no)
        case 2:
            PQ.Dequeue()
        case 0:
            repeat = False   