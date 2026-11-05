"""Singly linked list: each node holds data and a reference to the next node.

Letters are inserted at the end and removed from the front.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_first(self):
        removed_data = self.head.data
        self.head = self.head.next  # the head moves to the next node
        return removed_data

    def display(self):
        if self.head is None:
            return "None"
        letters = []
        current = self.head
        while current is not None:
            letters.append(current.data)
            current = current.next
        return " -> ".join(letters) + " -> None"


word = "RESUJENTO"
singly_list = SinglyLinkedList()
print("Singly linked list created (empty):", singly_list.display())

for letter in word:
    singly_list.insert_at_end(letter)
    print("Inserted", letter, "->", singly_list.display())

print("\nInitial singly linked list:", singly_list.display())
print()

while not singly_list.is_empty():
    removed = singly_list.remove_first()
    print("Removed", removed, "->", singly_list.display())

print("\nThe singly linked list is now empty.")
