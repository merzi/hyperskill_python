search_string = "old"
string = input()
pos_1 = string.find(search_string)
pos_2 = string.rfind(search_string)
print(pos_1 if pos_2 < pos_1 else pos_2)
