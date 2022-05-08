quantity = int(input())
final_quantity = int(input())
half_life = 12
counter = 0


while quantity >= final_quantity:
    quantity /= 2
    counter += 1

print(counter * half_life)
