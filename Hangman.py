import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'code', 'programming', 'openai', 'developer']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        '''
    ]
    return stages[6 - tries]

def play():
    word = get_random_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("🕹️ Welcome to Hangman!")
    print(display_hangman(tries))
    print("_ " * len(word))

    while tries > 0 and word_letters:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Good guess!")
        else:
            tries -= 1
            print(f"❌ Wrong! You have {tries} tries left.")

        # Display current word state
        current_state = [letter if letter in guessed_letters else "_" for letter in word]
        print(display_hangman(tries))
        print("Word: " + " ".join(current_state))

    if not word_letters:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game over! The word was:", word)

if __name__ == "__main__":
    play()
