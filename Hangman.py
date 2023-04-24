import random

# List of words for the game
words = ["python", "java", "ruby", "javascript", "php", "html", "css", "swift"]

# Choose a random word from the list
word = random.choice(words)

# Create a list of underscores to represent the letters in the word
hidden_word = ["_" for letter in word]

# Keep track of guessed letters
guessed_letters = []

# Game loop
while "_" in hidden_word:
    # Print the current state of the hidden word
    print(" ".join(hidden_word))

    # Get a guess from the player
    guess = input("Guess a letter: ").lower()

    # If the guess has already been made, prompt the user to guess again
    if guess in guessed_letters:
        print("You already guessed that letter, try again!")
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in word:
        print("Correct!")

        # Update the hidden word with the guessed letter(s)
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
    else:
        print("Incorrect, try again.")

# If the player has guessed all the letters in the word, they win!
print(f"Congratulations, you guessed the word '{word}'!")


