A = int(input())
B = int(input())
C = int(input())
X = int(input())
Y = int(input())

door = X * Y

if (A * B) < door > (A * C) or (B * C) < door:
    print("The box can be carried")
else:
    print("The box cannot be carried")
