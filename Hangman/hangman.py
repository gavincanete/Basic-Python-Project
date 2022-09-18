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

# print(figlet_format("WELCOME TO HANGMAN"))

word_of_the_day = words[randint(0, words_length-1)]
missing_word = regex.sub(consonant_or_vowel[randint(0,1)], '#', word_of_the_day.lower())

letter_stack = []

print(f"Guess the letter of {missing_word}")
print(f"{word_of_the_day}")
while(missing_word.lower() != word_of_the_day.lower()):
    print(f"{missing_word}")
    guess_letter =  input("Input here: ")[0]

    if (not guess_letter.lower() in word_of_the_day.lower()):
        if(not guess_letter.lower() in letter_stack):
            lives -= 1
            print("".join(hangman_list[0:(hangman_count-lives)+1]))
            letter_stack.append(guess_letter.lower())
            print("Sorry, incorrect letter")
        else:
            print("letter is already inputted")
    else:
        if(not guess_letter.lower() in letter_stack):
            temp = ""
            for i in range(len(word_of_the_day)):                
                if(guess_letter.lower() == word_of_the_day[i].lower()):
                    temp += guess_letter.lower()
                else:
                    temp += missing_word[i].lower()
            missing_word = temp
            letter_stack.append(guess_letter.lower())

    if(lives == 0): break

if(lives > 0): print(f"Congratulations!, you have answered all the letters of {word_of_the_day}")
else: print("Sorry, you have lose all your lives. Just keep practicing!")


# for word in words:
#     # Pick either vowel or consonant sets to replace with _
#     missing_word = regex.sub(consonant_or_vowel[randint(0,1)], ' _ ', word.lower())
#     print(f"Next word: {missing_word}")
#     # Ask the user to guess the word
#     guess = input()

#     # Ask the user to guess different word
#     while(guess.lower() != word.lower()):
#         # Print out the lives remaining
#         print("".join(hangman_list[0:(hangman_count-lives)+1]))

#         lives -= 1
#         if(lives == 0): break

#         guess = input("Sorry, guess another word: ")

#     if(lives == 0): break

# if(lives > 0): print(f"Congratulations!, you have answered all {words_length} guess words")
# else: print("Sorry, you have lose all your lives. Just keep practicing!")