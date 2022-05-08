import string


def get_percentage(num, precision=0):
    return_string = string.Template("$percentage%")
    if precision > 0:
        percentage = str(round(num * 100, precision))
    else:
        percentage = str(round(num * 100))
    return return_string.substitute(percentage=percentage)
