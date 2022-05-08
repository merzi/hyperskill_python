tax_rates = ([0, 15527],
             [15, 42707],
             [25, 132406],
             [28, 99999999999999999999999])

income = int(input())
percent = 28
for rate in tax_rates:
    if income <= rate[1]:
        percent = rate[0]
        break

calculated_tax = round(income * percent / 100)

print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
