# Hangman
# By Marco Redulla
# Day 7 (18/06/2024)
import random
import hangman_words
import hangman_art

logo = hangman_art.logo
states = hangman_art.stages
word_list = hangman_words.word_list

# Variable Defining
lives = 6
chosen_word = random.choice(word_list)
display = ["_" for _ in range(len(chosen_word))]
attempted = [] # list of attempted letters

# Main Game
print(logo)
while "_" in display and lives > 0:
    print(states[lives - 7])
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1:
        print("You might have made an error in your input. Try again.")
    else:
        if guess not in chosen_word and guess not in attempted:
            print(f"You guessed {guess}. That's not in the word. You lose a life.")
            attempted.append(guess)
            lives -= 1
        elif guess in attempted:
            print("You have already attempted this letter. Try again.")
        else:
            attempted.append(guess)
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
    print(display)
if lives == 0:
    print(states[0])
    print("Game over.")
    print(f"The word is: {chosen_word}")
else:
    print("You won!")