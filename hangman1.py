import random 
# List of possible words
words = ['python', 'hangman', 'coding', 'programming', 'developer', 'challenge', 'game']
def get_random_word():
    return random.choice(words)
 
def display_word(word, guessed_letters): 
    return ''.join([letter if letter in guessed_letters else '_' for letter in word]) 
 
def hangman(): 
    word = get_random_word()
    guessed_letters = set()
    attempts = 6  # Number of allowed incorrect guesses
    wrong_guesses = 0
    print("Welcome to Hangman!")
    print(f"You have {attempts} attempts to guess the word.\n")

    while wrong_guesses < attempts:
        print(f"Word: {display_word(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.\n")
            continue  

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue 
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.\n")

            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                
                break
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts - wrong_guesses} attempts left.\n")
        if wrong_guesses == attempts:
            print(f"You've run out of attempts! The word was: {word}")
if __name__ == "__main__":
    hangman()
