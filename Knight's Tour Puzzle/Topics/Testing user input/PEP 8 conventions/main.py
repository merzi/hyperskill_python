def check_name(name: str):
    if name in ["l", "I", "O"]:
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif name.islower():
        print("It is a common variable")
    elif name.isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
