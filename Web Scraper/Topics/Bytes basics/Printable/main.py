def int_to_char(integer):
    if chr(integer).isprintable():
        return chr(integer)

    return False


print(int_to_char(int(input())))
