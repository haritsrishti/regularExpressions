# Extract URLs from the given text.

# Text: Visit our site at https://www.example.com or http://example.org for more details.

import re

text = "Visit our site at https://www.example.com or http://example.org for more details."
pattern = r"(https?://\S+)"
urls = re.findall(pattern, text)
print(urls)
