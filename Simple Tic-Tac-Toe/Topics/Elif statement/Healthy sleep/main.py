A = int(input())  # min sleeping hours a day
B = int(input())  # max sleeping hours a day
H = int(input())  # actual sleeping hours a day

if H < A:
    print("Deficiency")
elif H > B:
    print("Excess")
else:
    print("Normal")
