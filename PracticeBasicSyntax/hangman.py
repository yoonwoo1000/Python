import random

words = [
    "apple",
    "banana",
    "orange",
    "computer",
    "python",
    "java",
    "music",
    "book",
    "game",
]


def draw_hangman(step):
    stages = [
        """
        +---+
        |   |
        |   |
        |   
        |
        |
        =========
        """,
        """
        +---+
        |   |
        |   |
        |   o
        |
        |
        =========
        """,
        """
        +---+
        |   |
        |   |
        |   o
        |   |
        |
        =========
        """,
        """
        +---+
        |   |
        |   |
        |   o
        |   |\\
        |
        =========
        """,
        """
        +---+
        |   |
        |   |
        |   o
        |  /|\\
        |
        =========
        """,
        """
        +---+
        |   |
        |   |
        |   o
        |  /|\\
        |    \\
        =========
        """,
        """
        +---+
        |   |
        |   |
        |   o
        |  /|\\
        |  / \\
        =========
        """,
    ]
    print(stages[step])


def get_guess():

    while True:
        userInput = input("Type an Alphabet : ")
        userInput = userInput.strip().lower()

        if len(userInput) != 1:
            print(f"{userInput} is not one word")
            continue
        elif not userInput.isalpha():
            print(f"type an alphabet")
            continue
        return userInput


def display_words(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_"

    return display.strip()


def playgame():
    target_word = random.choice(words)

    guessed_letters = []

    MAX_STEP = 6
    wrong_guesses = 0
    print(f"word length : {len(target_word)}")

    while wrong_guesses < MAX_STEP:
        print("-" * 30)
        draw_hangman(wrong_guesses)
        print(display_words(target_word, guessed_letters))
        print(f"wrong : {wrong_guesses} / total : {MAX_STEP}")
        print(f"guessed_letters : {guessed_letters}")
        guess = get_guess()

        if guess in guessed_letters:
            print("already on this list")
            continue

        guessed_letters.append(guess)

        if guess in target_word:
            print(f"{guess} is in target_word")
            result = check_word(target_word, guessed_letters)
            if result:
                print(display_words(target_word, guessed_letters))
                print(f"correct : {target_word}")
                return
        else:
            wrong_guesses += 1
            print(f"{guess} is not in target_word")

    draw_hangman(wrong_guesses)
    print(f"wrong : {wrong_guesses} / total : {MAX_STEP}")

    pass


def check_word(word, guessed_letters):

    for w in word:
        if w in guessed_letters:
            continue
        else:
            return False

    return True


def main():
    print("hangman game")

    playgame()
    print("end game")


if __name__ == "__main__":
    main()
