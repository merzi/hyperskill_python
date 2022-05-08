def check(x: int):
    lower_limit = 120
    upper_limit = 137
    if lower_limit < x < upper_limit:
        print(str(x))
    else:
        print("That's a bad present!")
