# put your code here
number = 0
numbers = []
searched_number = 55

number = int(input())
while number != searched_number:
    numbers.append(number)
    number = int(input())

print(len(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers)))
