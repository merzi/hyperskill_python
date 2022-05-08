import re

text = input()
words = text.split()
for word in words:
    # finish the code here
    if re.search(r"^(www\.\w+)", word.lower()):
        print(word)
    elif re.search(r"^(https?://\w+)", word.lower()):
        print(word)
