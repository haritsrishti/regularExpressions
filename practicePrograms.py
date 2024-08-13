# A RegEx, or Regular Expression, is a sequence of characters
# that forms a search pattern.

# RegEx can be used to check if a string contains the specified
# search pattern.

# Python has a built-in package called re
import re

txt = "The rain in Spain"
x = re.search("^T.*Spain$", txt)
print(x)
#-----------------------------------------

# METACHARACTERS are characters with a special meaning:

# 1. [] -> A set of characters -> "[a-z]"
txt = "The rain in Spain"
# Find all lower case characters alphabetically between "a" and "z":
x = re.findall("[a-z]", txt)
print(x)


# 2. \ -> Signals a special sequence
# \d is a metacharacter that matches any digit from 0 to 9.
text = "That will be 59 dollars"
x = re.search("\d", text)   #findall
print(x)


# 3. . -> Any character (except newline character) -> "he..o"


# 4. ^ -> Starts with -> "^helo"
txt = "Hello World"

#check if the string starts with 'hello':
x = re.findall("^Hello", txt)
#print(x)
if x:
    print("Yes, the string starts with the given pattern ")
else:
    print("No")


# 5. $ -> Ends with -> "world$"

txt = "hello world"

#check if the string ends with 'world':

x = re.findall("world$", txt)
#print(x)

if x:
    print("Yes, the string ends with 'world'")
else:
    print("No, the string ends with 'world'")

# 6. * -> Zero or more occurences -> "he.*o"

txt = "Hi Srishti"
# Search for a sequence that starts with "hi",
# followed by 0 or more  (any) characters, and an "s":

x = re.findall("Hi.*t", txt)
print(x)


# 7. + -> One or more occurrences -> "he.+o"
txt = "hello srishti"
x = re.findall("he.+i", txt)
print(x)

# 8. ? ->  Zero or one occurrences "he.?o"

txt = "hello sara"

#Search for a sequence that starts with "he",
# followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)

#This time we got no match, because there were not zero,
# not one, but two characters between "he" and the "o"


# 9.  {} -> Exactly the specified number of occurrences -> "he.{2}o"

txt = "Hello Saurabh"

#Search for a sequence that starts with "he",
# followed excactly 2 (any) characters, and an "o":
x = re.findall("He.{7}r", txt)
print(x)


# 10. | -> Either or -> "falls|stays"

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays"

x = re.findall("falls|stays", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


# 11. () -> Capture and group

#SPECIAL SEQUENCES
# A special sequence is a \ followed by one of the characters
# text = 'ABC 123 XYZ 456 @&! 100'
#
# pattern = re.compile(r'\d\d\d')
#
# #print(r'old\new')
#
# matches = pattern.finditer(text)
# for match in matches:
#    print(match.group())
# #print(matches)
#
# #-----------------------------------
#
# pattern = r"[A-Z]yclone"
# text = '''Cyclone is the state of having being or reality.
#         It is often contrasted with essence, since one can
#          understand the essential it features of something without
#         knowing whether it Dyclone exists. Ontology it studies existence and
#         differentiates between singular existence of Iyclone individual entities
#         and it general existence of concepts or universals. Entities present in
#         space and time have Zyclone concrete existence, in contrast to abstract entities,
#         like numbers and sets.'''
#
# # matches = re.search(pattern, text)
# # print(matches)
#
# matches = re.finditer(pattern, text)
# for match in matches:
#     print(match)
#     print(type(match))
#     print(match.span())
#
#
# matches = re.findall(pattern, text)
# print(matches)
#
# pattern1 = "it"
# matches = re.finditer(pattern1, text)
# for match in matches:
#     print(match)
