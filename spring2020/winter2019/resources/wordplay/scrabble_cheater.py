import sys
import scrabble

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: scrabble.py [RACK]")
        sys.exit(1)

    rack = list(sys.argv[1].lower())
    valid_words = []

    for word in scrabble.wordlist:
        # Make a copy of the rack for every new word, so we can manipulate it
        # without compromising the original rack.
        available_letters = rack[:]

        valid = True
        for letter in word.lower():
            if letter not in available_letters:
                valid = False
                break
            available_letters.remove(letter)

        if valid:
            # Calculate the Scrabble score.
            score = 0
            for letter in word:
                score = score + scrabble.scores[letter]
            valid_words.append((score, word))

    for play in sorted(valid_words):
        print("%d %s" % (play[0], play[1]))
