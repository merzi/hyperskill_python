pos_x = int(input())
pos_y = int(input())
possibilities = 0

if 1 < pos_x < 8 and 1 < pos_y < 8:
    possibilities = 8
elif pos_x == 1 == pos_y or pos_x == 1 and pos_y == 8:
    possibilities = 3
elif pos_x == 8 and pos_y == 1 or pos_x == 8 == pos_y:
    possibilities = 3
elif pos_x == 1 or pos_x == 8 and (1 < pos_y < 8):
    possibilities = 5
elif pos_y == 1 or pos_y == 8 and (1 < pos_x < 8):
    possibilities = 5

print(possibilities)
