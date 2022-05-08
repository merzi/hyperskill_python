numbers = []
num = input()
while num != ".":
    numbers.append(int(num))
    num = input()

print(sum(numbers) / len(numbers))
