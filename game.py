from hangman_art import stages, logo, game_over
from hangman_words import words_list
import random

word = random.choice(words_list)
word_length = len(word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess_letter = input("Guess a letter : ").lower()

    if guess_letter in display:
        print(f"You've already guess {guess_letter}")

    for index in range(word_length):
        letter = word[index]
        if letter == guess_letter:
            display[index] = letter

    if guess_letter not in word:

        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        lives -= 1
    if lives == 0:
        end_of_game = True
        print(game_over)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
