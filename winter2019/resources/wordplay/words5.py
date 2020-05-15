from scrabble import wordlist, scores

for word in wordlist:
    if "mako" in word:
        word_score = 0
        for letter in word:
            word_score = word_score + scores[letter]
            print("score for the word " + word + " is " + str(word_score))

