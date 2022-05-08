string = input()
output = ""

for char in string:
    if char.isupper():
        output = f"{output}_{char.lower()}"
    else:
        output += char

print(output)
