# HANGMAN GAME

"""
* A user with 7 lives
* Goal: Guess the word
"""
from random import randint
import re as regex
from pyfiglet import figlet_format

# User Lives
lives = 7

# Used to printout the Hangman when a user guess incorrectly
hangman_list = ["H", "A", "N", "G", "M", "A", "N"]
hangman_count = len(hangman_list)

# Note: Used when performing static data
# words = ["Great", "Wax", "Male", "Sound"]

# Noted: Used when reading a candidates_words.txt file
words = []

with open("candidate_words.txt", "r") as file_name:
    words = [line.replace("\n", "") for line in file_name]

words_length = len(words)

consonant_or_vowel = ["[aeiou]", "[b-d]|[f-h]|[j-n]|[p-t]|[v-z]"]

print(figlet_format("WELCOME TO HANGMAN"))
for word in words:
    # Pick either vowel or consonant sets to replace with _
    missing_word = regex.sub(consonant_or_vowel[randint(0,1)], ' _ ', word.lower())
    print(f"Next word: {missing_word}")
    # Ask the user to guess the word
    guess = input()

    # Ask the user to guess different word
    while(guess.lower() != word.lower()):
        # Print out the lives remaining
        print("".join(hangman_list[0:(hangman_count-lives)+1]))

        lives -= 1
        if(lives == 0): break

        guess = input("Sorry, guess another word: ")

    if(lives == 0): break

if(lives > 0): print(f"Congratulations!, you have answered all {words_length} guess words")
else: print("Sorry, you have lose all your lives. Just keep practicing!")