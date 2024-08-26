import os
import time

class Deque:
    def __init__(self):
        self.front = 0
        self.rare = 0
        self.queue = [None]*5

    def Enqueue_F(self, value):
        if self.front == 0:
            print(' f = 1')
            return

        self.front = self.front - 1
        self.queue[self.front] = value

    def Enqueue_R(self, value):
        if self.rare == len(self.queue):
            print(' r = N ')  
            return

        self.queue[self.rare] = value
        self.rare = self.rare + 1

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
    print("\nOUTPUT RESTRICTED DEQUE:\n")
    print(q.queue)
    print("\n1 | enqueue front")
    print("2 | enqueue rare")
    print("3 | dequeue ")

    choose = int(input("\n\n\nenter => "))

    match choose:
        case 1:
            data = int(input("value to enter: "))
            q.Enqueue_F(data)  
            time.sleep(2)          
        case 2:
            data = int(input("value to enter: "))
            q.Enqueue_R(data)
            time.sleep(2)
        case 3:
            q.Dequeue_F()
            time.sleep(2)
        case 0:
            repeat = False 
