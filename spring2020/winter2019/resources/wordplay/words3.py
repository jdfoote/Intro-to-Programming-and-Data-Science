import scrabble

VOWELS = ['a', 'e', 'i', 'o', 'u']

# Print all words that have all 5 vowels.
for word in scrabble.wordlist:
    all_vowels = True
    for vowel in VOWELS:
        if vowel not in word:
            all_vowels = False

    if all_vowels:
        print(word + " has all vowels")
