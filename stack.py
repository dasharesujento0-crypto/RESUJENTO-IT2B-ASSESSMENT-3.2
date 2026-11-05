"""Stack (LIFO): the last letter pushed is the first letter popped."""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def display(self):
        return "Bottom " + str(self.items) + " Top"


word = "RESUJENTO"
stack = Stack()
print("Stack created (empty):", stack.display())

for letter in word:
    stack.push(letter)
    print("Pushed", letter, "->", stack.display())

print("\nInitial stack:", stack.display())
print()

while not stack.is_empty():
    popped = stack.pop()
    print("Popped", popped, "->", stack.display())

print("\nThe stack is now empty.")
