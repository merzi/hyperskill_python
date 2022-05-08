sheep = 6769
cow = 3848
pig = 1296
goat = 678
chicken = 23

money = int(input())

if sheep <= money:
    count = money // sheep
    animal = 'sheep' if count > 1 else 'sheep'
    output = f"{count} {animal}"
elif cow <= money:
    count = money // cow
    animal = 'cows' if count > 1 else 'cow'
    output = f"{count} {animal}"
elif pig <= money:
    count = money // pig
    animal = 'pigs' if count > 1 else 'pig'
    output = f"{count} {animal}"
elif goat <= money:
    count = money // goat
    animal = 'goats' if count > 1 else 'goat'
    output = f"{count} {animal}"
elif chicken <= money:
    count = money // chicken
    animal = 'chickens' if count > 1 else 'chicken'
    output = f"{count} {animal}"
else:
    output = "None"

print(output)
