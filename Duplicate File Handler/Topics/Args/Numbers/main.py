# put your python code here
def multiply(*number_values):
    sum_value = 0
    for num in number_values:
        if sum_value == 0:
            sum_value = num
            continue
        sum_value *= num
    return sum_value
