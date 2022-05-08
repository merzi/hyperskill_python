sentence = input()
new_sentence = ""
for char in sentence:
    new_sentence += chr(ord(char) + 1)

print(new_sentence)
