grade_a = [90, 100]
grade_b = [80, 90]
grade_c = [70, 80]
grade_d = [60, 70]

result = int(input()) / int(input()) * 100

if grade_a[0] <= result:
    print("A")
elif grade_b[0] <= result < grade_b[1]:
    print("B")
elif grade_c[0] <= result < grade_c[1]:
    print("C")
elif grade_d[0] <= result < grade_d[1]:
    print("D")
else:
    print("F")
