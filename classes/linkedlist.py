class linkedlist:
    def __init__(self, data = None):
        self.next = None
        self.previous = None
        self.data = data

    def __next__(self):
        return self.next

    def __iter__(self):
        current = self
        while current:
            try:
                current = next(current)
                print(current.data)
            except:
                print("End of line")
        current = self

    # Maximum recursion depth error, python doesn't like my linked list.
    # def __str__(self):
    #     return str(self)

    # def start(head):
    #     current = head
    #     while current:
    #         print(current.data, end=" -> ")
    #         current = current.next
    #     print("None")

    def connect(node, data):
        if node is None:
            print("Error")
            return

        new_node = linkedlist(data)
        new_node.previous = node
        new_node.next = node.next

        if node.next:
            node.next.previous = new_node

        node.next = new_node

    # def disconnect(node):
