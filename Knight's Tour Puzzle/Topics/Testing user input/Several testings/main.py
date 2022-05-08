def check(number: str):
    min_number = 202
    if number.isnumeric():
        if int(number) >= min_number:
            print(number)
        else:
            print("There are less than 202 apples! You cheated me!")
    else:
        print("It is not a number!")
