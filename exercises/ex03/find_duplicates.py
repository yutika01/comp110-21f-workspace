"""Finding duplicate letters in a word."""

__author__ = "730480382"

word: str = input("Enter a word: ")
i: int = 0
j: int = i+1
duplicate_count: int = 0
duplicate: bool = False
while i < len(word):
    j = i + 1
    while j < len(word):
        if word[i] == word[j]:
            duplicate_count = duplicate_count + 1
        j = j+1
    i = i+1


if (duplicate_count > 0):
    duplicate = True
else:
    duplicate = False
print("Found duplicate: " + str(duplicate))