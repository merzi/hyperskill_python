list_ = [int(num) for num in input()]
new_list = list()
b = 0
for num in list_:
    if b == 0:
        b = num
    else:
        new_list.append((num + b) / 2)
        b = num

print(new_list)
