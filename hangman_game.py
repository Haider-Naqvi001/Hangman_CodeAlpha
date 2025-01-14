import random

word_list = ["ability", "absurd", "achieve", "adapt", "advice", "agency", "amaze", "anchor", 
             "artist", "assist", "average", "beauty", "borrow", "bravery", "cactus", "camera"]

def get_word():
    return random.choice(word_list).upper()

def hangman_stages(tries):
    stages = [
        """
          +---+
          O   |
         /|\\  |
         / \\  |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
         /    |
             ===
        """,
        """
          +---+
          O   |
         /|\\  |
              |
             ===
        """,
        """
          +---+
          O   |
         /|   |
              |
             ===
        """,
        """
          +---+
          O   |
          |   |
              |
             ===
        """,
        """
          +---+
          O   |
              |
              |
             ===
        """,
        """
          +---+
              |
              |
              |
             ===
        """
    ]
    return stages[tries]

def play_word(word):
    word_length = "_" * len(word)
    guessed_words = []
    guessed_letters = []
    tries = 6
    guessed = False

    print("Welcome to Hangman!")
    print(hangman_stages(tries))
    print(word_length)

    while not guessed and tries > 0:
        guess = input("Enter a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_length)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_length = "".join(word_as_list)

                if "_" not in word_length:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_length = word

        else:
            print("Invalid guess. Please enter a valid letter or word.")

        print(hangman_stages(tries))
        print(word_length)
        print("\n")

    if guessed:
        print(f"Congratulations! You guessed the word '{word}'!")
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'.")

def main():
    word = get_word()
    play_word(word)
    while input("Play Again? (Y/N): ").strip().upper() == "Y":
        word = get_word()
        play_word(word)

if __name__ == "__main__":
    main()
