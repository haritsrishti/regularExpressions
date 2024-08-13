# Find all words in a string that start with the
# letter "b" and end with "t".
# Example string: "The bat and bet were not in the basket."

import re

text = "The bat and bet were not in the basket."
pattern = r"\bb\w*t\b"
x = re.findall(pattern, text)
print(x)

# \w*: Matches zero or more word characters
# (letters, digits, or underscores). This allows for any
# characters to be between the starting 'b' and the ending 't'.

# Replace all occurrences of the word "cat" with "dog" in a string.

text = "The cat sat on the mat. The cat alog is in the cat acomb."
pattern = r"\bcat\b"
replacement = "dog"
x = re.sub(pattern, replacement, text)
print(x)

# Use re.sub() to replace occurrences of a pattern with a replacement string.
# re.findall() is for finding all matches, not for replacing.


# Split a string into a list of words, removing all punctuation.
# Example string: "Hello, world! How's everything going?"

text = "Hello, world! How's everything going?"
pattern = r"\W+"
x = re.split(pattern, text)
x = [word for word in x if word]
# The general syntax for a list comprehension is:
# [expression for item in iterable if condition]

# word for word in x:
# ------------------
# word: This is the item that will be included in the new list.
# for word in x: This iterates over each item in the existing list x.

# if word:
# --------
# if word: This is a condition that filters items from the original list. Only items that evaluate to True (i.e., non-empty strings in this case) are included in the new list.

# In Python, non-empty strings are considered True,
# while empty strings are considered False.

print(x)


# EXAMPLE

# x = ["hello", "", "world", "", "python"]

# # Apply the list comprehension
# x = [word for word in x if word]
# print(x)

# Output: ['hello', 'world', 'python']


# Original List (x): ["hello", "", "world", "", "python"]

# Filter Operation:
# "hello" is included because it’s non-empty.
# "" (empty string) is excluded because it evaluates to False.
# "world" is included because it’s non-empty.
# "" (empty string) is excluded because it evaluates to False.
# "python" is included because it’s non-empty.
# Result: The final list contains only non-empty strings: ['hello', 'world', 'python'].



# List Comprehension: A concise way to create a new list by
# iterating over an existing list and applying a filter condition.
# x = [word for word in x if word]: This expression creates a new list from x,
# including only the items that are non-empty strings.
