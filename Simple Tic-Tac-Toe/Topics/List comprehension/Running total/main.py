number_list = [int(digit) for digit in input()]
print([sum(number_list[:i + 1]) for i in range(len(number_list))])
