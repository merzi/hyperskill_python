def object_with_beautiful_identity():
    max_number = 10_000
    for i in range(max_number):
        # Change the next line
        if str(id(i)).endswith('888'):
            return i

    return None
