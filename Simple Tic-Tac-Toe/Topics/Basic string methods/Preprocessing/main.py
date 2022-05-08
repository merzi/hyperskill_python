replacements = [',', '.', '!', '?']
input_string = input().lower()

for punctuation in replacements:
    input_string = input_string.replace(punctuation, '')

print(input_string)
