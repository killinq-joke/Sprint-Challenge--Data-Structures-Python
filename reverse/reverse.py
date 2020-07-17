class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def display(self):
        current = self.head
        arr = []
        while current:
            arr.append(current.value)
            current = current.get_next()
        print(arr)

    def reverse_list(self, node, prev):
        if not node:
            return
        if node.get_next():
            self.reverse_list(node.get_next(), node)
        else:
            self.head = node
        node.set_next(prev)
        


l = LinkedList()
l.add_to_head(10)
l.add_to_head(5)
l.add_to_head(2)
l.reverse_list(l.head, None)
l.display()