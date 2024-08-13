# Find words starting with a specific leter

import re

def find_words_starting_with(text, letter):
    pattern = fr'\b{letter}\w*'
    return re.findall(pattern, text, re.IGNORECASE)

# Example usage
text = input("Enter the text: ")
letter = input("Enter the starting letter: ")
words = find_words_starting_with(text, letter)
print("Words starting with", letter, ":", words)
