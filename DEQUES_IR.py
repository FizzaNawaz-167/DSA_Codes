import os
import time

class Deque:
    def __init__(self):
        self.front = 0
        self.rare = 0
        self.queue = [None]*5
  
    def Enqueue_R(self, value):
        if self.rare == len(self.queue):
            return

        self.queue[self.rare] = value
        self.rare = self.rare + 1

    def Dequeue_R(self):
        if self.rare == 0:
            return

        self.rare = self.rare - 1
        self.queue[self.rare] = None

    def Dequeue_F(self):
        if self.front == len(self.queue):
            print('cant dequeue f = N')
            return

        self.queue[self.front] = None
        self.front = self.front + 1              


q = Deque()
q.Enqueue_R(1)
q.Enqueue_R(2)
q.Enqueue_R(3)
q.Enqueue_R(4)
q.Enqueue_R(5)

repeat = True
while repeat:
    os.system('cls')
    print("\nINPUT RESTRICTED DEQUE:\n")
    print(q.queue)
    print("\n1 | enqueue")
    print("2 | dequeue rare")
    print("3 | dequeue front")

    choose = int(input("\n\n\nenter => "))

    match choose:
        case 1:
            data = int(input("value to enter: "))
            q.Enqueue_R(data)  
            time.sleep(2)          
        case 2:
            q.Dequeue_R()
        case 3:
            q.Dequeue_F()
        case 0:
            repeat = False 
