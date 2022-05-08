A = int(input())  # recommended sleep
B = int(input())  # max sleep
H = int(input())  # current sleep

if H < A:
    print("Deficiency")
elif H > B:
    print("Excess")
else:
    print("Normal")
