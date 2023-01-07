import random as r
import hangman_art as art
import hangman_words as words

blank = ""
lives = 5
chosen_word = r.choice(words.word_list)
for n in range(len(chosen_word)):
    blank += " _"

print(art.logo)
while lives != 0:
    guess = input("Guess a letter:\n").lower()
    for letter in chosen_word:
        if guess != letter:
            print(blank)
            print("You guessed " + guess +
                  ", that's not in the word. You lose a life.")

        # TODO-3 - Check if the letter the user guessed (guess)
        # is one of the letters in the chosen_word.
