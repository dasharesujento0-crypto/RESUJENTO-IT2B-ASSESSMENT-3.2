"""Linked list: insert at the end, then remove the first node each time."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # None marks the end of the list


class LinkedList:
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
linked_list = LinkedList()
print("Linked list created (empty):", linked_list.display())

for letter in word:
    linked_list.insert_at_end(letter)
    print("Inserted", letter, "->", linked_list.display())

print("\nInitial linked list:", linked_list.display())
print()

while not linked_list.is_empty():
    removed = linked_list.remove_first()
    print("Removed", removed, "->", linked_list.display())

print("\nThe linked list is now empty.")
