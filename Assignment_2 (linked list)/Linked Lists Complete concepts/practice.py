def new_list(self):
    new_list_node = Node()
    storage = int(input("Enter size of list: "))
    print("Enter elements in list: ")

    for i in range(1, storage):
        element = int(input())
        self.Append(new_list_node)

