# put your python code here
number_students_1 = int(input())
number_students_2 = int(input())
number_students_3 = int(input())

desks_room_1 = (number_students_1 // 2 + number_students_1 % 2)
desks_room_2 = (number_students_2 // 2 + number_students_2 % 2)
desks_room_3 = (number_students_3 // 2 + number_students_3 % 2)

print(sum((desks_room_1, desks_room_2, desks_room_3)))
