# regularExpressions (RegEx) 

## Overview
Introduction to Regular Expressions
Regular expressions, often abbreviated as RegEx, are sequences of characters that form search patterns. These patterns can be used for string matching, searching, replacing, and splitting text. They are incredibly useful for data validation, parsing text, and extracting specific information from strings.

Common Uses of Regular Expressions:

Validation: Check if a string follows a certain format (e.g., email addresses, phone numbers).

Searching: Find specific patterns within a string (e.g., finding all dates in a document).

Replacing: Replace parts of a string based on a pattern (e.g., replacing all occurrences of "cat" with "dog").

Splitting: Divide a string into substrings based on a pattern (e.g., splitting a sentence into words).


## Importing the re Module
Start by importing the re module in Python, which allows you to use regular expressions.

import re


## Basic Patterns-
Literal Characters: Matches the exact characters in the text.

## Metacharacters
Metacharacters are special characters in RegEx that have specific meanings and are used to define search patterns.

 Common Metacharacters:

. : Matches any single character except a newline.

^ : Matches the start of a string.

$ : Matches the end of a string.

'*' : Matches zero or more occurrences of the preceding character.
 
'+' : Matches one or more occurrences of the preceding character.
  
? : Matches zero or one occurrence of the preceding character.

\d : Matches any digit (equivalent to [0-9]).

\D : Matches any non-digit character.

\w : Matches any word character (letters, digits, and underscores).

\W : Matches any non-word character.

\s : Matches any whitespace character (spaces, tabs, newlines).

\S : Matches any non-whitespace character.


### Boundary Matchers
\b: Word boundary. Matches the position where a word starts or ends.

\B: Non-word boundary. Matches any position that is not the start or end of a word.

### Example:
text = "The cat sat on the mat."

pattern = r"\bcat\b"             # Matches 'cat' only as a full word


### Examples:
\d{3}-\d{2}-\d{4} : matches a Social Security number format like 123-45-6789.

\w+@\w+\.\w+ : matches an email address like example@domain.com.


## Functions in the re Module
Python's re module provides several functions for working with regular expressions:

re.match(pattern, string): Checks if the pattern matches the beginning of the string.

re.search(pattern, string): Searches the string for the first location where the pattern matches.

re.findall(pattern, string): Returns a list of all matches of the pattern in the string.

re.finditer(pattern, string): Returns an iterator yielding match objects for all matches in the string.

re.sub(pattern, repl, string): Replaces occurrences of the pattern in the string with repl.

re.split(pattern, string): Splits the string by the occurrences of the pattern.

Examples:

re.match(r"\d{3}-\d{3}-\d{4}", "123-456-7890"): Matches the phone number format at the beginning of the string.

re.search(r"dog", "The quick brown dog"): Finds the word "dog" in the string.

re.sub(r"cat", "dog", "The cat sat on the mat"): Replaces "cat" with "dog".


## Examples and Demonstrations
For your demonstration, you can walk through some examples using the above functions:

### Finding a Phone Number:

import re

text = "My phone number is 123-456-7890."

pattern = r"\d{3}-\d{3}-\d{4}"                   # The r before the string indicates a raw string, which tells Python to treat backslashes as literal characters and not as 
                                                           escape characters.
                                                           
result = re.search(pattern, text)

if result:
    print("Phone number found:", result.group())


    
### Replacing Text:

import re

text = "The cat sat on the mat."

pattern = r"\bcat\b"

replacement = "dog"

result = re.sub(pattern, replacement, text)

print("Updated text:", result)
