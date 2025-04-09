# Student Name: Craig Kaseke
# Student Id: KSKTAN003
# Date: 08-04-2025
# Last Updated: 08-04-2025
# Description: Script that takes a paragraph as input and:
#             • Removes all punctuation marks (.,!?;:) from a paragraph.
#             • Counts and displays the number of unique words in a paragraph.

# Prompt the user for a single-line paragraph input
input_paragraph = input('Enter a paragraph of any length:\n')

# Set of punctuation marks to remove from the paragraph
flagged_punctuation_marks = {
    ".", ",", "!", "?", ";", ":"
}

# Dictionary to track unique words and their frequencies
words_frequency_tracker = {}

# List to collect characters that are not punctuation
original_paragraph_characters = []

# Loop through each character in the paragraph
for character in input_paragraph:
    # If the character is not a punctuation mark, keep it
    if character not in flagged_punctuation_marks:
        original_paragraph_characters.append(character)

# Join the characters into a cleaned paragraph string
paragraph_without_punctuation = "".join(original_paragraph_characters)

# Initialize a variable to build words character by character
current_word = ""

# Iterate through the cleaned paragraph to extract words
for character in paragraph_without_punctuation:
    if character == ' ':
        if current_word:
            # Add or update word count in the dictionary
            words_frequency_tracker[current_word] = words_frequency_tracker.get(current_word, 0) + 1
            current_word = ""
    else:
        current_word += character

# Add the final word if it exists
if current_word:
    words_frequency_tracker[current_word] = words_frequency_tracker.get(current_word, 0) + 1

# Display the results
print('A paragraph without punctuation:')
print(paragraph_without_punctuation)

print('The number of unique words in a paragraph:')
print(len(words_frequency_tracker))

print('The unique words are:')
print(list(words_frequency_tracker.keys()))