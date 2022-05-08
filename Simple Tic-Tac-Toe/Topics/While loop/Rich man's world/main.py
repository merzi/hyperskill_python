max_amount = 700000
year_rate = 1.071
deposit_amount = int(input())
counter = 0

while deposit_amount < max_amount:
    deposit_amount *= year_rate
    counter += 1

print(counter)
