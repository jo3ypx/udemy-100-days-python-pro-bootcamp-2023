import random as r

word_list = ["aardvark", "baboon", "camel"]
# chosen_word = word_list[r.randint(0, len(word_list)-1)]
blank = ""
chosen_word = r.choice(word_list)
for n in range(len(chosen_word)):
    blank += "_"

    # while:
guess = input("Guess a letter:\n").lower()
for letter in chosen_word:
    if guess != letter:
        print()
        print("You guessed " + guess +
              ", that's not in the word. You lose a life.")
        print()

        # TODO-3 - Check if the letter the user guessed (guess)
        # is one of the letters in the chosen_word.
