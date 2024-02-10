import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Incorrect! Attempts left: {max_attempts - attempts}")

        print(display_word(word_to_guess, guessed_letters))

        if set(guessed_letters) >= set(word_to_guess):
            print("Congratulations! You've guessed the word.")
            break

        if attempts == max_attempts:
            print("Sorry, you've run out of attempts. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
