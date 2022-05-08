digits = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
phone = input()
for digit in phone:
    print(digits[int(digit)])
