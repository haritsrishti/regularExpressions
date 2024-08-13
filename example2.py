# Write a regex to validate a phone number in the format 123-456-7890.

import re

text = "My phone number is 123-456-7890."
pattern = r"\b\d{3}-\d{3}-\d{4}\b"
phone_number = re.findall(pattern, text)
print(phone_number)

#-----------------------------------------

txt = "My phone number is 880-013-8219"
pattern = r"\b\d{3}-\d{3}-\d{4}\b"
if re.findall(pattern, txt):
    print("Valid phn number")
else:
    print("Invalid phn number")

# \b : Word boundary, ensures that the phone number is not part of a longer sequence of digits (e.g., it prevents matching in "123-456-78901").
# \d{3}: Matches exactly three digits.
# -: Matches the literal hyphen "-".
# \d{3}: Matches the next three digits.
# -: Matches the second hyphen "-".
# \d{4}: Matches exactly four digits.
# \b : Word boundary

# Non-Word Boundary (\B):
#
# Within a Word: It matches a position where two word characters or two non-word characters are next to each other.
# Example: In "helloworld", \Bworld would match the "world" part because "world" is part of a larger word.

txt = "HelloWorld"
x = re.findall(r"\BWorld", txt)
print(x)


text1 = "hellooooWorllld, hello123"
pattern1 = r"(Worllld).*?(123)"
x = re.findall(pattern1, text1)
print(x)
