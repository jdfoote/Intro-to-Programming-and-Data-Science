import scrabble

# Print all letters that never appear doubled in an English word.
for letter in "abcdefghijklmnopqrstuvwxyz":
    exists = False
    for word in scrabble.wordlist:
        if letter + letter in word:
            exists = True
            break
    if not exists:
        print("There are no English words with a double " + letter)
