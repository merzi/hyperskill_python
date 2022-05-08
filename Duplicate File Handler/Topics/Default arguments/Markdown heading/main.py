def heading(char, count=1):
    if count < 1:
        count = 1
    elif count > 6:
        count = 6
    head = "#" * count
    return head + " " + char
