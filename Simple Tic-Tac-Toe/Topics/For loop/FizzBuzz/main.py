start = 1
end = 100

words = ["Fizz", "Buzz"]

for num in range(start, end + 1):
    fizz_buzz = ""
    if num % 3 == 0:
        fizz_buzz = words[0]
    if num % 5 == 0:
        fizz_buzz += words[1]

    if fizz_buzz == "":
        print(num)
    else:
        print(fizz_buzz)
