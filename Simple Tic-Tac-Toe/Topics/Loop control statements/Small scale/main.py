numbers = []

while True:
    number = input()
    if number == ".":
        break

    numbers.append(float(number))

print(min(numbers))
