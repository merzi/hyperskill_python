pos_x = float(input())
pos_y = float(input())
sector = ""
if pos_x == 0 and pos_y == 0:
    sector = "It's the origin!"
elif pos_x == 0 or pos_y == 0:
    sector = "One of the coordinates is equal to zero!"
elif pos_x > 0 and pos_y > 0:
    sector = 'I'
elif pos_y < 0 < pos_x:
    sector = 'IV'
elif pos_x < 0 < pos_y:
    sector = 'II'
else:
    sector = 'III'

print(sector)
