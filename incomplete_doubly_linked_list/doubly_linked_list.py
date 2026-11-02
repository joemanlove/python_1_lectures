from node import Node

class DoublyLinkedList:
    """
    A Doubly Linked List (still in development)

    Arguments:
        None

    Attributes:
        head - Node or None type
        tail - Node or None type

    Methods:
        add_head - Adds a Node to the head end, the provided Node becomes the new head.
        add_tail - Adds a Node to the tail end, the provided Node becomes the new tail.

    Examples:
        None
    """

    def __init__(self, *args):
        self.head = None
        self.tail = None
        # protect from index out of range for empty lists
        if args:
            nodes = [Node(arg) for arg in args]
            for i in range(len(nodes) - 1):
                # set next attributes
                nodes[i].next = nodes[i + 1]
                # set previous attributes
                nodes[i + 1].prev = nodes[i]
            self.head = nodes[0]
            self.tail = nodes[-1]

    def add_head(self, new_node):
        """
        Adds a Node to the head end, the provided Node becomes the new head.

        Argument:
            Node type to be added
        """
        if not isinstance(new_node, Node):
            new_node = Node(new_node)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def add_tail(self, new_node):
        """
        Adds a Node to the tail end, the provided Node becomes the new tail.

        Argument:
            Node type to be added
        """
        if not isinstance(new_node, Node):
            new_node = Node(new_node)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
            self.tail = new_node

    # def __add__(self, other):
    #     list1 + list2

    def __repr__(self):
        current_node = self.head
        results = ''
        while current_node:
            results += str(current_node) + '\n'
            current_node = current_node.next
        return results


if __name__ == "__main__":
    test_list = DoublyLinkedList(1)
    print(test_list)
    print(test_list.head == test_list.tail)
    test_list.add_head(42)
    print('after addition at head:')
    print(test_list)
    test_list.add_tail(Node("billy"))
    print('after addition at tail:')
    print(test_list)
