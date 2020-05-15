import scrabble

# Print all words that are palindromes.
for word in scrabble.wordlist:

    # convert all words that are word_lists
    word_list = list(word)

    # make a second copy of a word list and reverse it
    word_list_rev = list(word)
    word_list_rev.reverse()

    if len(word) > 1 and word_list == word_list_rev:
        print(word)
