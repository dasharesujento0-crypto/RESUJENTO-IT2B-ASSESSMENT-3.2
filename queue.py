"""Queue (FIFO): the first letter enqueued is the first letter dequeued."""

from collections import deque


def display(queue):
    return "Front " + str(list(queue)) + " Rear"


word = "RESUJENTO"
queue = deque()
print("Queue created (empty):", display(queue))

for letter in word:
    queue.append(letter)  # enqueue at the rear
    print("Enqueued", letter, "->", display(queue))

print("\nInitial queue:", display(queue))
print()

while len(queue) > 0:
    dequeued = queue.popleft()  # dequeue from the front
    print("Dequeued", dequeued, "->", display(queue))

print("\nThe queue is now empty.")
