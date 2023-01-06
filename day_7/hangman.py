import random as r

word_list = ["aardvark", "baboon", "camel"]
blank = ""
chosen_word = r.choice(word_list)
for n in range(len(chosen_word)):
    blank += "_"

# while:
guess = input("Guess a letter:\n").lower()
for letter in chosen_word:
    if guess != letter:
        print(blank)
        print("You guessed " + guess +
              ", that's not in the word. You lose a life.")

        # TODO-3 - Check if the letter the user guessed (guess)
        # is one of the letters in the chosen_word.
