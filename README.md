Python Hangman Game

A classic Hangman word-guessing game built with Python. The player must guess a randomly selected word one letter at a time without running out of attempts.

Features

Random word selection from a separate word list.

Three difficulty levels:

Easy: 6 attempts

Medium: 4 attempts

Hard: 2 attempts

ASCII Hangman drawing that updates after incorrect guesses.

Displays correctly guessed letters and hides the remaining ones.

Prevents guessing the same letter more than once.

Input validation.

Win and lose conditions.

Option to play multiple rounds without restarting the program.

Requirements

Python 3.x

No external libraries required.

Installation and Usage

Clone this repository:

git clone YOUR_REPOSITORY_URL

Navigate to the project directory:

cd hangman-game

Run the game:

python main.py

Project Structure

hangman-game/
│
├── main.py
├── words_list.py
└── README.md

main.py – Contains the game logic, functions and user interaction.

words_list.py – Contains the list of possible words.

How to Play

Choose a difficulty level.

Guess one letter at a time.

Correct guesses reveal letters in the hidden word.

Incorrect guesses reduce your remaining attempts.

Guess the word before running out of attempts to win.

Choose whether to play another round.

Concepts Practiced

Functions and return values

Lists, tuples, sets and dictionaries

Loops and conditional statements

String methods and input validation

Random module

Variable scope

Working with multiple Python modules