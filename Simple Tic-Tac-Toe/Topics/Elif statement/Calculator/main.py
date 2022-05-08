# put your python code here
first_number = float(input())
second_number = float(input())
arithmetic_operation = input()
division_operations = ["/", "mod", "div"]
simple_operations = ["+", "-", "*", "/"]

if arithmetic_operation in division_operations and second_number == 0:
    print("Division by 0!")
else:
    if arithmetic_operation in simple_operations:
        print(float(eval(f"{first_number} {arithmetic_operation} {second_number}")))
    elif arithmetic_operation == "pow":
        print(float(first_number ** second_number))
    elif arithmetic_operation == "mod":
        print(float(first_number % second_number))
    elif arithmetic_operation == "div":
        print(float(first_number // second_number))
    else:
        print("unknown operation")
