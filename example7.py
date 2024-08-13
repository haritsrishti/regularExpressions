# Find all words in the text that start with the letter "a".

# Text: Apple and apricot are amazing fruits that are often enjoyed.

import re

text = "Apple and apricot123 are amazing fruits that are often enjoyed."
pattern = r'\ba\w*'
words = re.findall(pattern, text, re.IGNORECASE)
print(words)

# Extract all numbers from the text.

#Text: There are 42 apples, 37 oranges, and 5 bananas.

import re

text = "There are 42 apples, 37 oranges, and 5 bananas."
pattern = r'\d+'
numbers = re.findall(pattern, text)
print(numbers)


# Find all words that are exactly 4 letters long.

# Text: This is a test with many four-letter words like test and many.

import re

text = "This is a test with many four-letter words like test and many."
pattern = r'\b\w{4}\b'
words = re.findall(pattern, text)
print(words)


# Find all vowels in the text.

# [aeiouAEIOU]: This pattern is a character class that matches any single character
# that is either a lowercase vowel (a, e, i, o, u) or an uppercase vowel (A, E, I, O, U).

# Text: The quick brown fox jumps over the lazy dog.

import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r'[aeiou]'
vowels = re.findall(pattern, text)
print(vowels)


# Replace every occurrence of the word "bad" with "good" in the text.

# Text: This is a bad day. It has been a bad experience.

import re

text = "This is a bad day. It has been a bad experience."
pattern = r'\bbad\b'
replacement = 'good'
new_text = re.sub(pattern, replacement, text)
print(new_text)


# Check if the text contains the word "hello".

# Text : Hello there! How are you today?

import re

text = "Hello there! How are you today?"
pattern = r'\bhello\b'
match = re.search(pattern, text, re.IGNORECASE)
print("Found" if match else "Not found")


# Find all words that end with "ing".

# Text: The children are playing and laughing while singing.

import re

text = "The children are playing and laughing while singing."
pattern = r'\b\w+ing\b'
words = re.findall(pattern, text)
print(words)

