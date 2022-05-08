def calculate(amount, interest_rate, time):
    # your code here
    interest = (amount * interest_rate * time) / 100
    total_amount = interest + amount
    return interest, total_amount


def print_result(interest, total_amount):
    # your code here
    output = f"""The interest is: {interest}
The total amount is: {total_amount}"""
    print(output)

