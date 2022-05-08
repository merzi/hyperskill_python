# put your python code here
numbers = []

while True:
    numbers.append(int(input()))
    if sum(numbers) == 0:
        break

print(sum([num ** 2 for num in numbers]))
