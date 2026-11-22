import random
from words_list import words

hangman = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        " |\\",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "  \\"),
    6: (" o ",
          "/|\\",
          "/ \\")}

def display_man(wrong_guesses):
    print("==========================")
    for line in hangman[wrong_guesses]:
        print(line)
    print("==========================")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(f"The answer was: {answer}")

def reset():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    return answer, hint, wrong_guesses, guessed_letters

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    
    while True:
        print("=================================")
        print("Welcome to a Python Hangman Game!")
        print("=================================")
        max_guesses = input("Choose difficulty:\n1.Easy\n2.Medium\n3.Hard\n")
        if max_guesses == "1":
            max_guesses = 6
        elif max_guesses == "2":
            max_guesses = 4
        elif max_guesses == "3":
            max_guesses = 2
        else:
            print("Incorrect choice")
            continue
        remaining_guesses = max_guesses
        is_running = True
        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)
            print(f"Remaining Attempts: {remaining_guesses}")
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1:
                print("Use only 1 letter")
                continue
            if not guess.isalpha():
                print("Use letters only")
                continue
            if guess in guessed_letters:
                print("You used this letter already")
                continue
            elif guess not in guessed_letters:
                guessed_letters.add(guess)
            
            if guess in answer:
                for i in range(len(answer)):
                    if guess == answer[i]:
                        hint[i] = guess
            else:
                wrong_guesses += 1
                remaining_guesses -= 1
            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You won!")
                is_running = False
            elif remaining_guesses == 0:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You lost!")
                is_running = False

        while True:
            play_again = input("Do you want to play again? (Y/N): ").upper()

            while play_again != "Y" or "N":
                if play_again == "Y":
                    answer, hint, wrong_guesses, guessed_letters = reset()
                    break
                elif play_again == "N":
                    print("Exiting the program. Have a nice day!")
                    return 0
                else:
                    print("Incorrect choice")
            break
            
            
if __name__ == "__main__":
    main()