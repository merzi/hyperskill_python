numbers = input().split(" ")
new_list = []

for num in range(len(numbers)):
    new_list.append(numbers[len(numbers) - 1 - num])

print(" ".join(new_list))
