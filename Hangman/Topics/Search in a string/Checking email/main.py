def check_email(string):
    if " " in string or "@" not in string:
        return False

    domain = string.split("@")[1]
    return domain.find(".") > 0
