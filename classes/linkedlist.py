class linkedlist:
    def __init__(self, data = None):
        self.next = None
        self.previous = None
        self.data = data

    # More practice and explanation is needed
    # def __next__(self):
    #     if self.next:
    #         return self.next
    #     else:
    #         raise StopIteration

    # def __iter__(self):
    #     current = self
    #     return next(current)

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
