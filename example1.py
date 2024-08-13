# Write a regex to extract all email addresses from a string.
#  string: "Contact us at support@example.com or sales@example.co.uk"

import re

text = "Contact us at support@example.com or sales@example.co.uk"
pattern = r"\S+@\S+\.\S+"
emails = re.match(pattern,text)
print(emails)
#-------------------------------------------


text1 = "my mail is haritsrishti@gmail.com"
pattern = r"haritsrishti@gmail.com"
x = re.findall(pattern,text1)
print(x)



# r"\S+@\S+\.\S+"

#1. \S+ = matches one or more non-whitespace characters.
#2. @ = matches the literal "@" symbol.
#3. \S+ = after @ matches one or more non-whitespace characters (like the domain name).
#4. \. = matches the literal dot ".".
#5. \S+ = after the dot matches one or more non-whitespace characters (like the domain extension .com, .uk, etc.).

#  How It Matches "support@example.com":
# support: The first \S+ matches the word "support" because it's a sequence of non-whitespace characters.
# @: The @ matches the literal "@" in the email.
# example: The second \S+ matches "example".
# .: The \. matches the dot ".".
# com: The last \S+ matches "com".

# Why It Doesn't Match "contact":
# The pattern r"\S+@\S+\.\S+" requires the presence of the "@" symbol and a domain extension (e.g., .com, .uk) to be valid.
# "contact" by itself doesn't contain the "@" symbol or a domain extension, so it doesn't match.
# 4. Stopping at .com or .uk:
# The pattern is designed to stop at the end of the string that fits the email structure, which includes:
# The local part before the "@".
# The domain name after the "@".
# The domain extension after the final dot.

# For instance, in "support@example.com", \S+ after the dot matches "com". It stops here
# because the regex pattern only expects non-whitespace characters following the dot,
# which ends with "com" in this example.

# Why It Stops After the Domain Extension:
# The pattern r"\S+@\S+\.\S+" only matches up to the last \S+ after the dot.
# So, if the string ends after .com or .uk, the pattern stops matching there
# because it's the end of the email format that the pattern expects.
# If there are more characters after .com, it would continue matching if
# they are non-whitespace. For example, "support@example.comextra" would
# match the whole string because it doesn't contain whitespace to stop the match.
