import random

from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

lives = 7
print(logo)
chosen_word = random.choice(word_list)

blanks = ""
word_lenght = len(chosen_word)
for i in range(word_lenght):
    blanks += "_"

print(blanks)



condition = False
correct_letter = []

while not condition:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letter:
        print(f"You have already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:

        lives -= 1
        print(f"You guessed {guess}, that's not in word. You lose a lfe.")
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("Your HANGMAN is DEAD. \n*******GAME OVER*******")
            print(f"Your word was {chosen_word}")
            exit()

    if "_" not in display:
        condition = True
        print("*******YOU WON********")
        print(f"Your word was {chosen_word}")
        exit()

    # print(stages[lives])

