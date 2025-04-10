# Student Name: Craig Kaseke
# Student Id: KSKTAN003
# Date: 08-04-2025
# Last Updated: 08-04-2025
# Description: Script that asks the user to input a sentence and a
# word to find. The program should:
# • Display whether the word is present in the sentence or not.
# • If found, show the index where the word first appears in the sentence.
#
# sentence = input('Enter a sentence:\n').lower()
# word_to_find = input('Enter the word to find:\n').lower()


sentence = "The Quick Brown Fox Jumped Over The Lazy Dog".lower()
word_to_find  = "brown".lower()

words = sentence.split(" ")
found = False
first_char_index = 0

for i, word in enumerate(words):
    if word == word_to_find:
        print(f"The word '{word}' is in the sentence.")
        print(f"It first appears at index {first_char_index}.\n")
        found = True
        break
    print(first_char_index)
    first_char_index += len(word) + 1  # +1 for the space

if not found:
    print(f"The word '{word_to_find}' is NOT in the sentence.\n")