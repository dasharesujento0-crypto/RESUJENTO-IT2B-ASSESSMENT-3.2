"""Array: add letters to the end, then remove the last element each time."""

word = "RESUJENTO"
letters = []
print("Array created (empty):", letters)

for letter in word:
    letters.append(letter)
    print("Added", letter, "->", letters)

print("\nInitial array:", letters)
print()

while len(letters) > 0:
    removed = letters.pop()  # pop() without an index removes the last element
    print("Removed", removed, "->", letters)

print("\nThe array is now empty.")
