# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."


def get_calculation_parts():
    calc = input(msg_0)
    x, operation, y = calc.split()
    return x, operation, y


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def program():
    x = None
    y = None
    oper = None

    while x is None or y is None or oper is None:
        try:
            x, oper, y = get_calculation_parts()
        except ValueError:
            x = None

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)
            x = None
            y = None

        if oper not in ["+", "-", "*", "/"]:
            print(msg_2)
            oper = None

        if oper == "+":
            print(addition(x, y))
        elif oper == "-":
            print(subtraction(x, y))
        elif oper == "*":
            print(multiplication(x, y))
        elif oper == "/" and y != 0:
            print(division(x, y))
        else:
            x = None
            print(msg_3)

program()

