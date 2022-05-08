def final_deposit_amount(*interest, amount=1000):
    for num in interest:
        amount = amount * ((100 + num) / 100)

    return round(amount, 2)

