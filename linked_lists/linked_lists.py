from copy import deepcopy

class Node:
    def __init__(self, contents: str):
        self.contents = contents
        self.next = None

    def __repr__(self):
        return self.contents

    def __add__(self, term):
        if not isinstance(term, str):
            return NotImplemented
        else:
            self.contents += term

    def __radd__(self, term):
        if not isinstance(term, str):
            return NotImplemented
        else:
            self.contents = term + self.contents

red_fish = Node("Red Fish")
blue_fish = Node("Blue Fish")
one_fish = Node("One Fish")
two_fish = Node("Two Fish")

brain = Node("brain")
shoulders = Node("shoulders")
knees = Node("knees")
toes = Node("toes")

class LinkedList:
    def __init__(self):
        self.head = None

    def append_right(self, node : Node):

        # remove linkage to next node for safety
        node.next = None
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def __repr__(self):
        string_to_return = f"{self.head}"
        current_node = self.head
        while current_node:
            string_to_return += f" -> {current_node.next}"
            current_node = current_node.next
        return string_to_return
                
    def __add__(self, term):
        if not isinstance(term, LinkedList):
            return NotImplemented
        else:
            self_copy = deepcopy(self)
            term_copy = deepcopy(term)
            current_node = self_copy.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = term_copy.head
            return self_copy

link1 = LinkedList()

link1.append_right(red_fish)
link1.append_right(blue_fish)
link1.append_right(one_fish)
link1.append_right(two_fish)


link2 = LinkedList()

link2.append_right(brain)
link2.append_right(shoulders)
link2.append_right(knees)
link2.append_right(toes)

# print(link1)
# print(link2)

link12 = link1 + link2

# print(f"link1: {link1}\n")
# print(f"link2: {link2}\n")
# print(f"link12: {link12}\n")

# red_fish.contents = "Rote Fish"
# toes.contents = "feets"
# link2.head.contents = "Eyes"

# print(f"link1: {link1}\n")
# print(f"link2: {link2}\n")
# print(f"link12: {link12}")
