words = [word.capitalize() for word in input().split(" ")]
string = "".join(words)
print(string[0].lower() + string[1:])
