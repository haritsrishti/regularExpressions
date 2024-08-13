# Replace dates in the format DD/MM/YYYY with MM-DD-YYYY.

# Text : The deadlines are 31/12/2023 and 01/01/2024.


import re

text = 'The deadlines are 31/12/2023 and 01/02/2024.'
pattern = r'(\d{2})/(\d{2})/(\d{4})'
replacement = r'\2-\1-\3'
new_text = re.sub(pattern, replacement, text)
print(new_text)




