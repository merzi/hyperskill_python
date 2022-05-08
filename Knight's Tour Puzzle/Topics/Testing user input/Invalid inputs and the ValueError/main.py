def check() -> bool:
    try:
        number = int(input())
    except ValueError:
        print("Correct the error!")
        return False

    if 25 <= number <= 37:
        print(number)
        return True

    print("Correct the error!")
    return False
