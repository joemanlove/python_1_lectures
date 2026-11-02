"""
Provides Nodes for Doubly Linked Lists
"""

class Node:
    """
    A class for the Nodes in a doubly linked list.

    Arguments:
        contents - Whatever you're storing in your doubly linked list.

    Key Word Arguments:
        next_node - Node or None type, defaults to None
        prev_node - Node or None type, defaults to None

    For best functionality, contents objects should have a __str__ method.
    """
    def __init__(self, contents, next_node=None, prev_node=None):
        self.contents = contents
        self.next = next_node
        self.prev = prev_node

    # def __repr__(self):
    #     response = f"This node contains: {self.contents}."
    #     if self.next:
    #         response += f" The next node contains: {self.next.contents}."
    #     else:
    #         response += " There is no next Node."
    #     if self.prev:
    #         response += f" The previous node contains: {self.prev.contents}."
    #     else:
    #         response += " There is no previous Node."
    #     return response


if __name__ == "__main__":
    test_tail = Node("tail contents")
    test_head = Node("head contents", next_node=test_tail)
    # test_tail.prev = test_head
    # print("Printing node 'test_head':")
    print(test_head)
    # print("Printing node 'test_tail':")
    # print(test_tail)
