"""Doubly linked list: each node has next and prev references.

Letters are inserted at the end and removed from the end.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove_last(self):
        removed_data = self.tail.data
        if self.head is self.tail:
            # Removing the only node: both head and tail must become None
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None  # the new tail must not point to the removed node
        return removed_data

    def display(self):
        if self.head is None:
            return "None"
        letters = []
        current = self.head
        while current is not None:
            letters.append(current.data)
            current = current.next
        return "None <- " + " <-> ".join(letters) + " -> None"


word = "RESUJENTO"
doubly_list = DoublyLinkedList()
print("Doubly linked list created (empty):", doubly_list.display())

for letter in word:
    doubly_list.insert_at_end(letter)
    print("Inserted", letter, "->", doubly_list.display())

print("\nInitial doubly linked list:", doubly_list.display())
print()

while not doubly_list.is_empty():
    removed = doubly_list.remove_last()
    print("Removed", removed, "->", doubly_list.display())

print("\nThe doubly linked list is now empty.")
