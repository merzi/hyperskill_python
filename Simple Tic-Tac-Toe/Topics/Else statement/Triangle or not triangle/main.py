angle_a = int(input())
angle_b = int(input())
angle_c = int(input())
angle_sum = 180
if sum((angle_a, angle_b, angle_c)) == angle_sum:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
